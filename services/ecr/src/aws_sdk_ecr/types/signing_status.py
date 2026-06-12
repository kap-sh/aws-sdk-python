"""Generated from Smithy shape ``com.amazonaws.ecr#SigningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

"""<p>The image signing status. Possible values include <code>IN_PROGRESS</code>, <code>COMPLETE</code>, and <code>FAILED</code>.</p>"""
SigningStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: SigningStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SigningStatus value: {data!r}")
    return cast(SigningStatus, data)
