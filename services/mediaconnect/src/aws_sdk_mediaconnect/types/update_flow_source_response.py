"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateFlowSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.source


class UpdateFlowSourceResponse(TypedDict):
    flow_arn: NotRequired["str"]
    """<p>The ARN of the flow that you updated.</p>"""
    source: NotRequired["aws_sdk_mediaconnect.types.source.Source"]
    """<p>The details of the sources that are assigned to the flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowSourceResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "source" in value:
        import aws_sdk_mediaconnect.types.source

        out["source"] = aws_sdk_mediaconnect.types.source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowSourceResponse:
    out: UpdateFlowSourceResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "source" in data:
        import aws_sdk_mediaconnect.types.source

        out["source"] = aws_sdk_mediaconnect.types.source.deserialize_json(
            data["source"]
        )
    return out
