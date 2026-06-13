"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssetTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_type_list
    import aws_sdk_devops_agent.types.next_token


class ListAssetTypesResponse(TypedDict):
    items: "aws_sdk_devops_agent.types.asset_type_list.AssetTypeList"
    """<p>The list of supported asset types</p>"""
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token to retrieve the next page of results. Absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetTypesResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.asset_type_list

    out["items"] = aws_sdk_devops_agent.types.asset_type_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetTypesResponse:
    out: ListAssetTypesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_devops_agent.types.asset_type_list

        out["items"] = aws_sdk_devops_agent.types.asset_type_list.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListAssetTypesResponse.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
