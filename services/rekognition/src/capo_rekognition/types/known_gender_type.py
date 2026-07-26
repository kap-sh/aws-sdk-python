"""Generated from Smithy shape ``com.amazonaws.rekognition#KnownGenderType``."""

from typing import Literal, TypeAlias, cast

"""<p>A list of enum string of possible gender values that Celebrity returns.</p>"""
KnownGenderType: TypeAlias = Literal[
    "Male",
    "Female",
    "Nonbinary",
    "Unlisted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KnownGenderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KnownGenderType:
    return cast(KnownGenderType, data)
