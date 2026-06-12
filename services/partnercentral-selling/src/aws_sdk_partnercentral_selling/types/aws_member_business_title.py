"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsMemberBusinessTitle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

AwsMemberBusinessTitle: TypeAlias = Literal[
    "AWSSalesRep",
    "AWSAccountOwner",
    "WWPSPDM",
    "PDM",
    "PSM",
    "ISVSM",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWSSalesRep",
        "AWSAccountOwner",
        "WWPSPDM",
        "PDM",
        "PSM",
        "ISVSM",
    )
)


def serialize_aws_json_1_0(value: AwsMemberBusinessTitle) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsMemberBusinessTitle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AwsMemberBusinessTitle value: {data!r}")
    return cast(AwsMemberBusinessTitle, data)
