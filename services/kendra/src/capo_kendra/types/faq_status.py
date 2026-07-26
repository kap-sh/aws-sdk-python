"""Generated from Smithy shape ``com.amazonaws.kendra#FaqStatus``."""

from typing import Literal, TypeAlias, cast

FaqStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaqStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaqStatus:
    return cast(FaqStatus, data)
