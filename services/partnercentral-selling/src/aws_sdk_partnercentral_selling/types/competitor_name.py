"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CompetitorName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

CompetitorName: TypeAlias = Literal[
    "Oracle Cloud",
    "On-Prem",
    "Co-location",
    "Akamai",
    "AliCloud",
    "Google Cloud Platform",
    "IBM Softlayer",
    "Microsoft Azure",
    "Other- Cost Optimization",
    "No Competition",
    "*Other",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Oracle Cloud",
        "On-Prem",
        "Co-location",
        "Akamai",
        "AliCloud",
        "Google Cloud Platform",
        "IBM Softlayer",
        "Microsoft Azure",
        "Other- Cost Optimization",
        "No Competition",
        "*Other",
    )
)


def serialize_aws_json_1_0(value: CompetitorName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CompetitorName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompetitorName value: {data!r}")
    return cast(CompetitorName, data)
