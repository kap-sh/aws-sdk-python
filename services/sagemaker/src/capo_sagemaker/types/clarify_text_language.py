"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClarifyTextLanguage``."""

from typing import Literal, TypeAlias, cast

ClarifyTextLanguage: TypeAlias = Literal[
    "af",
    "sq",
    "ar",
    "hy",
    "eu",
    "bn",
    "bg",
    "ca",
    "zh",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "et",
    "fi",
    "fr",
    "de",
    "el",
    "gu",
    "he",
    "hi",
    "hu",
    "is",
    "id",
    "ga",
    "it",
    "kn",
    "ky",
    "lv",
    "lt",
    "lb",
    "mk",
    "ml",
    "mr",
    "ne",
    "nb",
    "fa",
    "pl",
    "pt",
    "ro",
    "ru",
    "sa",
    "sr",
    "tn",
    "si",
    "sk",
    "sl",
    "es",
    "sv",
    "tl",
    "ta",
    "tt",
    "te",
    "tr",
    "uk",
    "ur",
    "yo",
    "lij",
    "xx",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClarifyTextLanguage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClarifyTextLanguage:
    return cast(ClarifyTextLanguage, data)
