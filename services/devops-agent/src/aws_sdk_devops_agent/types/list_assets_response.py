"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_list
    import aws_sdk_devops_agent.types.next_token


class ListAssetsResponse(TypedDict, closed=True):
    items: "aws_sdk_devops_agent.types.asset_list.AssetList"
    """<p>The list of assets for the agent space</p>"""
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token to retrieve the next page of results. Absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.asset_list

    out["items"] = aws_sdk_devops_agent.types.asset_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetsResponse:
    out: ListAssetsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_devops_agent.types.asset_list

        out["items"] = aws_sdk_devops_agent.types.asset_list.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListAssetsResponse.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
