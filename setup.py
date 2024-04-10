from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Swati",
    description="A demo for face recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swatishayna/Bollywood-Celebrity-Face-Similarity",
    author_email="swati308mmu@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'mtcnn',
        'tensorflow',
        'keras',
        'keras-vggface==0.6',
        'keras_applications',
        'PyYAML',
        'tqdm',
        'scikit-learn',
        'streamlit',
        'bing-image-downloader'
    ]
)
