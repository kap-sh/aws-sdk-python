"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySortName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

OpportunitySortName: TypeAlias = Literal[
    "LastModifiedDate",
    "Identifier",
    "CustomerCompanyName",
    "CreatedDate",
    "TargetCloseDate",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LastModifiedDate",
        "Identifier",
        "CustomerCompanyName",
        "CreatedDate",
        "TargetCloseDate",
    )
)


def serialize_aws_json_1_0(value: OpportunitySortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpportunitySortName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpportunitySortName value: {data!r}")
    return cast(OpportunitySortName, data)
