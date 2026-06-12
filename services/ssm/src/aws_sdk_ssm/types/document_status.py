"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

"""<p>The status of a document.</p>"""
DocumentStatus: TypeAlias = Literal[
    "Creating",
    "Active",
    "Updating",
    "Deleting",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Active",
        "Updating",
        "Deleting",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: DocumentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentStatus value: {data!r}")
    return cast(DocumentStatus, data)
