"""Generated from Smithy shape ``com.amazonaws.kendra#IssueSubEntity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

IssueSubEntity: TypeAlias = Literal[
    "COMMENTS",
    "ATTACHMENTS",
    "WORKLOGS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMMENTS",
        "ATTACHMENTS",
        "WORKLOGS",
    )
)


def serialize_aws_json_1_1(value: IssueSubEntity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IssueSubEntity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IssueSubEntity value: {data!r}")
    return cast(IssueSubEntity, data)
