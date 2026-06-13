"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterInputsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_router_input_list


class ListRouterInputsResponse(TypedDict):
    router_inputs: (
        "aws_sdk_mediaconnect.types.listed_router_input_list.ListedRouterInputList"
    )
    """<p>The summary information for the retrieved router inputs.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterInputsResponse) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.listed_router_input_list

    out["routerInputs"] = (
        aws_sdk_mediaconnect.types.listed_router_input_list.serialize_json(
            value["router_inputs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRouterInputsResponse:
    out: ListRouterInputsResponse = {}  # type: ignore[typeddict-item]
    if "routerInputs" in data:
        import aws_sdk_mediaconnect.types.listed_router_input_list

        out["router_inputs"] = (
            aws_sdk_mediaconnect.types.listed_router_input_list.deserialize_json(
                data["routerInputs"]
            )
        )
    else:
        raise DeserializationError("ListRouterInputsResponse.router_inputs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
