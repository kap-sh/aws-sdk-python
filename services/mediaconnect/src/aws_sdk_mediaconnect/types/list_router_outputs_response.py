"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterOutputsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_router_output_list


class ListRouterOutputsResponse(TypedDict):
    router_outputs: (
        "aws_sdk_mediaconnect.types.listed_router_output_list.ListedRouterOutputList"
    )
    """<p>The summary information for the retrieved router outputs.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterOutputsResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.listed_router_output_list

    out["routerOutputs"] = (
        aws_sdk_mediaconnect.types.listed_router_output_list.serialize_json(
            value["router_outputs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRouterOutputsResponse:
    out: ListRouterOutputsResponse = {}  # type: ignore[typeddict-item]
    if "routerOutputs" in data:
        import aws_sdk_mediaconnect.types.listed_router_output_list

        out["router_outputs"] = (
            aws_sdk_mediaconnect.types.listed_router_output_list.deserialize_json(
                data["routerOutputs"]
            )
        )
    else:
        raise DeserializationError("ListRouterOutputsResponse.router_outputs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
