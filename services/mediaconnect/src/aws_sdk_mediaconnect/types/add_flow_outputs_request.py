"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowOutputsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_add_output_request
    import aws_sdk_mediaconnect.types.flow_arn


class AddFlowOutputsRequest(TypedDict):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to add outputs to.</p>"""
    outputs: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest"
    ]
    """<p> A list of outputs that you want to add to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowOutputsRequest) -> dict:
    out: dict = {}
    if "outputs" in value:
        import aws_sdk_mediaconnect.types.__list_of_add_output_request

        out["outputs"] = (
            aws_sdk_mediaconnect.types.__list_of_add_output_request.serialize_json(
                value["outputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddFlowOutputsRequest:
    out: AddFlowOutputsRequest = {}  # type: ignore[typeddict-item]
    if "outputs" in data:
        import aws_sdk_mediaconnect.types.__list_of_add_output_request

        out["outputs"] = (
            aws_sdk_mediaconnect.types.__list_of_add_output_request.deserialize_json(
                data["outputs"]
            )
        )
    return out
