"""Generated from Smithy shape ``com.amazonaws.connect#ListRoutingProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.routing_profile_summary_list


class ListRoutingProfilesResponse(TypedDict):
    routing_profile_summary_list: NotRequired[
        "aws_sdk_connect.types.routing_profile_summary_list.RoutingProfileSummaryList"
    ]
    """<p>Information about the routing profiles.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutingProfilesResponse) -> dict:
    out: dict = {}
    if "routing_profile_summary_list" in value:
        import aws_sdk_connect.types.routing_profile_summary_list

        out["RoutingProfileSummaryList"] = (
            aws_sdk_connect.types.routing_profile_summary_list.serialize_json(
                value["routing_profile_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoutingProfilesResponse:
    out: ListRoutingProfilesResponse = {}  # type: ignore[typeddict-item]
    if "RoutingProfileSummaryList" in data:
        import aws_sdk_connect.types.routing_profile_summary_list

        out["routing_profile_summary_list"] = (
            aws_sdk_connect.types.routing_profile_summary_list.deserialize_json(
                data["RoutingProfileSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
