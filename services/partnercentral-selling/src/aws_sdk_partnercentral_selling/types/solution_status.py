"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

SolutionStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
    "Draft",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
        "Draft",
    )
)


def serialize_aws_json_1_0(value: SolutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SolutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SolutionStatus value: {data!r}")
    return cast(SolutionStatus, data)
