pytest -v schema-testing.py --tb=short --workers 4 --html=report.html --css=highcontrast.css
pytest -v schema-testing-neg.py --tb=short --workers 4 --html=report-neg.html --css=highcontrast.css
