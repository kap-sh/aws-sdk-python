"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutotuneMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutotuneMode: TypeAlias = Literal["Enabled",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Enabled",))


def serialize_aws_json_1_1(value: AutotuneMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutotuneMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutotuneMode value: {data!r}")
    return cast(AutotuneMode, data)
