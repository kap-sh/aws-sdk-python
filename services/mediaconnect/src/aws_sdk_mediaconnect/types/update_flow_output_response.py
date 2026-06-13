"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateFlowOutputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.output


class UpdateFlowOutputResponse(TypedDict):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that is associated with the updated output.</p>"""
    output: NotRequired["aws_sdk_mediaconnect.types.output.Output"]
    """<p> The new settings of the output that you updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowOutputResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "output" in value:
        import aws_sdk_mediaconnect.types.output

        out["output"] = aws_sdk_mediaconnect.types.output.serialize_json(
            value["output"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowOutputResponse:
    out: UpdateFlowOutputResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "output" in data:
        import aws_sdk_mediaconnect.types.output

        out["output"] = aws_sdk_mediaconnect.types.output.deserialize_json(
            data["output"]
        )
    return out
