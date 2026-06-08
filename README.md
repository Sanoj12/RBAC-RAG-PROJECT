Installation
1. Install uv
curl -Ls https://astral.sh/uv/install.sh | sh

or

pip install uv
2. Clone the repository
git clone https://github.com/your-username/project-name.git
cd project-name
3. Create virtual environment
uv venv

Activate it:

Linux / Mac

source .venv/bin/activate

Windows

.venv\Scripts\activate
4. Install dependencies

Using requirements file:

uv pip install -r requirements.txt