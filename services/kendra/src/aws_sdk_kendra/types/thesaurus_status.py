"""Generated from Smithy shape ``com.amazonaws.kendra#ThesaurusStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ThesaurusStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "UPDATING",
    "ACTIVE_BUT_UPDATE_FAILED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "UPDATING",
        "ACTIVE_BUT_UPDATE_FAILED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ThesaurusStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThesaurusStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThesaurusStatus value: {data!r}")
    return cast(ThesaurusStatus, data)
