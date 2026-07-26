"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_set_source_request
    import capo_mediaconnect.types.flow_arn


class AddFlowSourcesRequest(TypedDict, closed=True):
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>"""
    sources: NotRequired[
        "capo_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest"
    ]
    """<p> A list of sources that you want to add to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowSourcesRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_mediaconnect.types.__list_of_set_source_request

        out["sources"] = (
            capo_mediaconnect.types.__list_of_set_source_request.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddFlowSourcesRequest:
    out: AddFlowSourcesRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import capo_mediaconnect.types.__list_of_set_source_request

        out["sources"] = (
            capo_mediaconnect.types.__list_of_set_source_request.deserialize_json(
                data["sources"]
            )
        )
    return out
