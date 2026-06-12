"""Generated from Smithy shape ``com.amazonaws.dlm#ExecutionHandlerServiceValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

ExecutionHandlerServiceValues: TypeAlias = Literal["AWS_SYSTEMS_MANAGER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS_SYSTEMS_MANAGER",))


def serialize_json(value: ExecutionHandlerServiceValues) -> str:
    return value


def deserialize_json(data: str) -> ExecutionHandlerServiceValues:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExecutionHandlerServiceValues value: {data!r}"
        )
    return cast(ExecutionHandlerServiceValues, data)
