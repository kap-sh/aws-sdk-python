"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionResponseType``."""

from typing import Literal, TypeAlias, cast

FunctionResponseType: TypeAlias = Literal["ReportBatchItemFailures",]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionResponseType) -> str:
    return value


def deserialize_json(data: str) -> FunctionResponseType:
    return cast(FunctionResponseType, data)
