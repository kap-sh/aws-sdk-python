"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

PartnerAppType: TypeAlias = Literal[
    "lakera-guard",
    "comet",
    "deepchecks-llm-evaluation",
    "fiddler",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lakera-guard",
        "comet",
        "deepchecks-llm-evaluation",
        "fiddler",
    )
)


def serialize_aws_json_1_1(value: PartnerAppType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartnerAppType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartnerAppType value: {data!r}")
    return cast(PartnerAppType, data)
