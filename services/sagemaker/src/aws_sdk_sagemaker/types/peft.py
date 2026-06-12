"""Generated from Smithy shape ``com.amazonaws.sagemaker#Peft``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

Peft: TypeAlias = Literal["LORA",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LORA",))


def serialize_aws_json_1_1(value: Peft) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Peft:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Peft value: {data!r}")
    return cast(Peft, data)
