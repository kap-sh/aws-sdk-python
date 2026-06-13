"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterOutputErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.batch_get_router_output_error

BatchGetRouterOutputErrorList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.batch_get_router_output_error.BatchGetRouterOutputError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterOutputErrorList) -> list:
    import aws_sdk_mediaconnect.types.batch_get_router_output_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.batch_get_router_output_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetRouterOutputErrorList:
    import aws_sdk_mediaconnect.types.batch_get_router_output_error

    out: BatchGetRouterOutputErrorList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.batch_get_router_output_error.deserialize_json(
                item
            )
        )
    return out
