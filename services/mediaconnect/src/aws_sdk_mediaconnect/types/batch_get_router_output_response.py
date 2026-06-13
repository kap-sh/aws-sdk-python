"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterOutputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.batch_get_router_output_error_list
    import aws_sdk_mediaconnect.types.router_output_list


class BatchGetRouterOutputResponse(TypedDict):
    router_outputs: "aws_sdk_mediaconnect.types.router_output_list.RouterOutputList"
    """<p>An array of router outputs that were successfully retrieved.</p>"""
    errors: "aws_sdk_mediaconnect.types.batch_get_router_output_error_list.BatchGetRouterOutputErrorList"
    """<p>An array of errors that occurred when retrieving the requested router outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterOutputResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_output_list

    out["routerOutputs"] = aws_sdk_mediaconnect.types.router_output_list.serialize_json(
        value["router_outputs"]
    )
    import aws_sdk_mediaconnect.types.batch_get_router_output_error_list

    out["errors"] = (
        aws_sdk_mediaconnect.types.batch_get_router_output_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetRouterOutputResponse:
    out: BatchGetRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if "routerOutputs" in data:
        import aws_sdk_mediaconnect.types.router_output_list

        out["router_outputs"] = (
            aws_sdk_mediaconnect.types.router_output_list.deserialize_json(
                data["routerOutputs"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetRouterOutputResponse.router_outputs required"
        )
    if "errors" in data:
        import aws_sdk_mediaconnect.types.batch_get_router_output_error_list

        out["errors"] = (
            aws_sdk_mediaconnect.types.batch_get_router_output_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetRouterOutputResponse.errors required")
    return out
