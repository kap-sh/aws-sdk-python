"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowOutputsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_output


class AddFlowOutputsResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that these outputs were added to.</p>"""
    outputs: NotRequired["capo_mediaconnect.types.__list_of_output.__listOfOutput"]
    """<p> The details of the newly added outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowOutputsResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "outputs" in value:
        import capo_mediaconnect.types.__list_of_output

        out["outputs"] = capo_mediaconnect.types.__list_of_output.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> AddFlowOutputsResponse:
    out: AddFlowOutputsResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "outputs" in data:
        import capo_mediaconnect.types.__list_of_output

        out["outputs"] = capo_mediaconnect.types.__list_of_output.deserialize_json(
            data["outputs"]
        )
    return out
