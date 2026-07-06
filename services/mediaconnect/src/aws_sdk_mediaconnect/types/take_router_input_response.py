"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TakeRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_output_arn
    import aws_sdk_mediaconnect.types.router_output_routed_state


class TakeRouterInputResponse(TypedDict, closed=True):
    routed_state: (
        "aws_sdk_mediaconnect.types.router_output_routed_state.RouterOutputRoutedState"
    )
    """<p>The state of the association between the router input and output.</p>"""
    router_output_arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The ARN of the associated router output.</p>"""
    router_output_name: "str"
    """<p>The name of the associated router output.</p>"""
    router_input_arn: NotRequired[
        "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
    ]
    """<p>The ARN of the associated router input.</p>"""
    router_input_name: NotRequired["str"]
    """<p>The name of the associated router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TakeRouterInputResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_output_routed_state

    out["routedState"] = (
        aws_sdk_mediaconnect.types.router_output_routed_state.serialize_json(
            value["routed_state"]
        )
    )
    out["routerOutputArn"] = value["router_output_arn"]
    out["routerOutputName"] = value["router_output_name"]
    if "router_input_arn" in value:
        out["routerInputArn"] = value["router_input_arn"]
    if "router_input_name" in value:
        out["routerInputName"] = value["router_input_name"]
    return out


def deserialize_json(data: dict) -> TakeRouterInputResponse:
    out: TakeRouterInputResponse = {}  # type: ignore[typeddict-item]
    if "routedState" in data:
        import aws_sdk_mediaconnect.types.router_output_routed_state

        out["routed_state"] = (
            aws_sdk_mediaconnect.types.router_output_routed_state.deserialize_json(
                data["routedState"]
            )
        )
    else:
        raise DeserializationError("TakeRouterInputResponse.routed_state required")
    if "routerOutputArn" in data:
        out["router_output_arn"] = data["routerOutputArn"]
    else:
        raise DeserializationError("TakeRouterInputResponse.router_output_arn required")
    if "routerOutputName" in data:
        out["router_output_name"] = data["routerOutputName"]
    else:
        raise DeserializationError(
            "TakeRouterInputResponse.router_output_name required"
        )
    if "routerInputArn" in data:
        out["router_input_arn"] = data["routerInputArn"]
    if "routerInputName" in data:
        out["router_input_name"] = data["routerInputName"]
    return out
