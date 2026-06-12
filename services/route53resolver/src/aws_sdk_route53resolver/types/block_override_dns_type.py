"""Generated from Smithy shape ``com.amazonaws.route53resolver#BlockOverrideDnsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

BlockOverrideDnsType: TypeAlias = Literal["CNAME",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CNAME",))


def serialize_aws_json_1_1(value: BlockOverrideDnsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockOverrideDnsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockOverrideDnsType value: {data!r}")
    return cast(BlockOverrideDnsType, data)
