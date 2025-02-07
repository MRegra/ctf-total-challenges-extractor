# ctf-total-challenges-extractor
A script that extracts &amp; processes all CTF challenges and saves them in a db with the mark solved, not solved, published writeup not published writeup, published video not published video

# Creating & Activivating new environment:

    python3 -m venv myenv
    source ./myenv/bin/activate
    pip install mysql-connector-python sqlalchemy sqlalchemy-utils

# Deactivating new environment:

    deactivate

# Start & Enable DB:

    sudo systemctl enable mariadb
    sudo systemctl start mariadb

# Restart MariaDB

    sudo systemctl restart mariadb

# Create user & granting access on MariaDB

    CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
    GRANT ALL PRIVILEGES ON ctf.* TO 'myuser'@'localhost';
    FLUSH PRIVILEGES;

# Freeze repo requirements

    pip freeze > requirements.txt

# Install packages based on requirements

    pip install -r requirements.txt
