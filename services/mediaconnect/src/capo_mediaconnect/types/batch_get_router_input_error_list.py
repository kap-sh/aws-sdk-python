"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterInputErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_router_input_error

BatchGetRouterInputErrorList: TypeAlias = list[
    "capo_mediaconnect.types.batch_get_router_input_error.BatchGetRouterInputError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterInputErrorList) -> list:
    import capo_mediaconnect.types.batch_get_router_input_error

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.batch_get_router_input_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetRouterInputErrorList:
    import capo_mediaconnect.types.batch_get_router_input_error

    out: BatchGetRouterInputErrorList = []
    for item in data:
        out.append(
            capo_mediaconnect.types.batch_get_router_input_error.deserialize_json(item)
        )
    return out
