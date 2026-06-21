"""Generated from Smithy shape ``com.amazonaws.kendra#ThesaurusStatus``."""

from typing import Literal, TypeAlias, cast

ThesaurusStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "UPDATING",
    "ACTIVE_BUT_UPDATE_FAILED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThesaurusStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThesaurusStatus:
    return cast(ThesaurusStatus, data)
