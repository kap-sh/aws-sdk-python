"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#NationalSecurity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

NationalSecurity: TypeAlias = Literal[
    "Yes",
    "No",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Yes",
        "No",
    )
)


def serialize_aws_json_1_0(value: NationalSecurity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NationalSecurity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NationalSecurity value: {data!r}")
    return cast(NationalSecurity, data)
