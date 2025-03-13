from database import db

class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Subject {self.name}>"
    
class Chapter(db.Model):
    __tablename__ = "chapter"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    subject = db.relationship("Subject", backref=db.backref("chapters", lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return f"<Chapter {self.name}>"
    
class Quiz(db.Model):
    __tablename__ = "quiz"
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.String, db.ForeignKey("chapter.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    chapter = db.relationship("Chapter", backref=db.backref("quizzes", lazy=True, cascade="all, delete-orphan"))
    date_of_quiz = db.Column(db.Date, nullable=False)
    time_duaration = db.Column(db.String(5), nullable=False)
    remarks = db.Column(db.Text)

    def __repr__(self):
        return f"<Quiz {self.id}>"

class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    quiz = db.relationship("Quiz", backref=db.backref("questions", lazy=True, cascade="all, delete-orphan"))
    question_statement = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Question {self.id}>"
    
class Option(db.Model):
    __tablename__ = "option"
    id = db.Column(db.Integer, primary_key=True)
    option_text = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    question = db.relationship("Question", backref=db.backref("options", lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return f"<Option {self.id}>"
    
class CorrectOption(db.Model):
    __tablename__ = "correct_option"
    question_id = db.Column(db.Integer, db.ForeignKey("question.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    option_id = db.Column(db.Integer, db.ForeignKey("option.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    question = db.relationship("Question", backref=db.backref("correct_options", lazy=True, cascade="all, delete-orphan"))
    option = db.relationship("Option")

    def __repr__(self):
        return f"<CorrectOption question_id={self.question_id}, option_id={self.option_id}>"
