"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.batch_get_router_input_error_list
    import aws_sdk_mediaconnect.types.router_input_list


class BatchGetRouterInputResponse(TypedDict, closed=True):
    router_inputs: "aws_sdk_mediaconnect.types.router_input_list.RouterInputList"
    """<p>An array of router inputs that were successfully retrieved.</p>"""
    errors: "aws_sdk_mediaconnect.types.batch_get_router_input_error_list.BatchGetRouterInputErrorList"
    """<p>An array of errors that occurred when retrieving the requested router inputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterInputResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_input_list

    out["routerInputs"] = aws_sdk_mediaconnect.types.router_input_list.serialize_json(
        value["router_inputs"]
    )
    import aws_sdk_mediaconnect.types.batch_get_router_input_error_list

    out["errors"] = (
        aws_sdk_mediaconnect.types.batch_get_router_input_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetRouterInputResponse:
    out: BatchGetRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "routerInputs" in data:
        import aws_sdk_mediaconnect.types.router_input_list

        out["router_inputs"] = (
            aws_sdk_mediaconnect.types.router_input_list.deserialize_json(
                data["routerInputs"]
            )
        )
    else:
        raise DeserializationError("BatchGetRouterInputResponse.router_inputs required")
    if "errors" in data:
        import aws_sdk_mediaconnect.types.batch_get_router_input_error_list

        out["errors"] = (
            aws_sdk_mediaconnect.types.batch_get_router_input_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetRouterInputResponse.errors required")
    return out
