"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterOutputsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_filter_list


class ListRouterOutputsRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of router outputs to return in the response.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used to retrieve the next page of results.</p>"""
    filters: NotRequired[
        "aws_sdk_mediaconnect.types.router_output_filter_list.RouterOutputFilterList"
    ]
    """<p>The filters to apply when retrieving the list of router outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterOutputsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_mediaconnect.types.router_output_filter_list

        out["filters"] = (
            aws_sdk_mediaconnect.types.router_output_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRouterOutputsRequest:
    out: ListRouterOutputsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_mediaconnect.types.router_output_filter_list

        out["filters"] = (
            aws_sdk_mediaconnect.types.router_output_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out
