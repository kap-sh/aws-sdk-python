"""Generated from Smithy shape ``com.amazonaws.inspector#AssetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

AssetType: TypeAlias = Literal["ec2-instance",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ec2-instance",))


def serialize_aws_json_1_1(value: AssetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetType value: {data!r}")
    return cast(AssetType, data)
