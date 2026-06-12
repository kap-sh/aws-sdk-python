"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

OpsItemEventFilterKey: TypeAlias = Literal["OpsItemId",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OpsItemId",))


def serialize_aws_json_1_1(value: OpsItemEventFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemEventFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpsItemEventFilterKey value: {data!r}")
    return cast(OpsItemEventFilterKey, data)
