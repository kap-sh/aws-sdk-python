"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowOutputsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_output


class AddFlowOutputsResponse(TypedDict):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that these outputs were added to.</p>"""
    outputs: NotRequired["aws_sdk_mediaconnect.types.__list_of_output.__listOfOutput"]
    """<p> The details of the newly added outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowOutputsResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "outputs" in value:
        import aws_sdk_mediaconnect.types.__list_of_output

        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_output.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> AddFlowOutputsResponse:
    out: AddFlowOutputsResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "outputs" in data:
        import aws_sdk_mediaconnect.types.__list_of_output

        out["outputs"] = aws_sdk_mediaconnect.types.__list_of_output.deserialize_json(
            data["outputs"]
        )
    return out
