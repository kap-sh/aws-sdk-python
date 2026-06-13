"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow


class CreateFlowResponse(TypedDict):
    flow: NotRequired["aws_sdk_mediaconnect.types.flow.Flow"]
    """<p> The flow that you created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowResponse) -> dict:
    out: dict = {}
    if "flow" in value:
        import aws_sdk_mediaconnect.types.flow

        out["flow"] = aws_sdk_mediaconnect.types.flow.serialize_json(value["flow"])
    return out


def deserialize_json(data: dict) -> CreateFlowResponse:
    out: CreateFlowResponse = {}  # type: ignore[typeddict-item]
    if "flow" in data:
        import aws_sdk_mediaconnect.types.flow

        out["flow"] = aws_sdk_mediaconnect.types.flow.deserialize_json(data["flow"])
    return out
