"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_source


class AddFlowSourcesResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that these sources were added to.</p>"""
    sources: NotRequired["aws_sdk_mediaconnect.types.__list_of_source.__listOfSource"]
    """<p> The details of the newly added sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowSourcesResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "sources" in value:
        import aws_sdk_mediaconnect.types.__list_of_source

        out["sources"] = aws_sdk_mediaconnect.types.__list_of_source.serialize_json(
            value["sources"]
        )
    return out


def deserialize_json(data: dict) -> AddFlowSourcesResponse:
    out: AddFlowSourcesResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "sources" in data:
        import aws_sdk_mediaconnect.types.__list_of_source

        out["sources"] = aws_sdk_mediaconnect.types.__list_of_source.deserialize_json(
            data["sources"]
        )
    return out
