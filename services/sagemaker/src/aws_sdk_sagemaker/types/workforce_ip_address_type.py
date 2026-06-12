"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceIpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

WorkforceIpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ipv4",
        "dualstack",
    )
)


def serialize_aws_json_1_1(value: WorkforceIpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkforceIpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkforceIpAddressType value: {data!r}")
    return cast(WorkforceIpAddressType, data)
