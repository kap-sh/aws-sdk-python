"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ReviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

ReviewStatus: TypeAlias = Literal[
    "Pending Submission",
    "Submitted",
    "In review",
    "Approved",
    "Rejected",
    "Action Required",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending Submission",
        "Submitted",
        "In review",
        "Approved",
        "Rejected",
        "Action Required",
    )
)


def serialize_aws_json_1_0(value: ReviewStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewStatus value: {data!r}")
    return cast(ReviewStatus, data)
