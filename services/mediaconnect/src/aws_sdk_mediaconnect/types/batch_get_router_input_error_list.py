"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterInputErrorList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.batch_get_router_input_error

BatchGetRouterInputErrorList: TypeAlias = list["aws_sdk_mediaconnect.types.batch_get_router_input_error.BatchGetRouterInputError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterInputErrorList) -> list:
    import aws_sdk_mediaconnect.types.batch_get_router_input_error
    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.batch_get_router_input_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetRouterInputErrorList:
    import aws_sdk_mediaconnect.types.batch_get_router_input_error
    out: BatchGetRouterInputErrorList = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.batch_get_router_input_error.deserialize_json(item))
    return out