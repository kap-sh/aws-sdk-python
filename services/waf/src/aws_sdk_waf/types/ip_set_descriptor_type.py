"""Generated from Smithy shape ``com.amazonaws.waf#IPSetDescriptorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

IPSetDescriptorType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
    )
)


def serialize_aws_json_1_1(value: IPSetDescriptorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IPSetDescriptorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IPSetDescriptorType value: {data!r}")
    return cast(IPSetDescriptorType, data)
