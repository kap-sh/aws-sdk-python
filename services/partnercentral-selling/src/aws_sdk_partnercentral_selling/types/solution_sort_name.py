"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionSortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

SolutionSortName: TypeAlias = Literal[
    "Identifier",
    "Name",
    "Status",
    "Category",
    "CreatedDate",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Identifier",
        "Name",
        "Status",
        "Category",
        "CreatedDate",
    )
)


def serialize_aws_json_1_0(value: SolutionSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SolutionSortName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SolutionSortName value: {data!r}")
    return cast(SolutionSortName, data)
