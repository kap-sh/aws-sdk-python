"""Generated from Smithy shape ``com.amazonaws.dlm#ExecutionHandlerServiceValues``."""

from typing import Literal, TypeAlias, cast

ExecutionHandlerServiceValues: TypeAlias = Literal["AWS_SYSTEMS_MANAGER",]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionHandlerServiceValues) -> str:
    return value


def deserialize_json(data: str) -> ExecutionHandlerServiceValues:
    return cast(ExecutionHandlerServiceValues, data)
