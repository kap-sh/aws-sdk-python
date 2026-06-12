"""Generated from Smithy shape ``com.amazonaws.directconnect#NniPartnerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

NniPartnerType: TypeAlias = Literal[
    "v1",
    "v2",
    "nonPartner",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "v1",
        "v2",
        "nonPartner",
    )
)


def serialize_aws_json_1_1(value: NniPartnerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NniPartnerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NniPartnerType value: {data!r}")
    return cast(NniPartnerType, data)
