"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowOutputsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_add_output_request
    import capo_mediaconnect.types.flow_arn


class AddFlowOutputsRequest(TypedDict, closed=True):
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to add outputs to.</p>"""
    outputs: NotRequired[
        "capo_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest"
    ]
    """<p> A list of outputs that you want to add to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowOutputsRequest) -> dict:
    out: dict = {}
    if "outputs" in value:
        import capo_mediaconnect.types.__list_of_add_output_request

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_add_output_request.serialize_json(
                value["outputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddFlowOutputsRequest:
    out: AddFlowOutputsRequest = {}  # type: ignore[typeddict-item]
    if "outputs" in data:
        import capo_mediaconnect.types.__list_of_add_output_request

        out["outputs"] = (
            capo_mediaconnect.types.__list_of_add_output_request.deserialize_json(
                data["outputs"]
            )
        )
    return out
