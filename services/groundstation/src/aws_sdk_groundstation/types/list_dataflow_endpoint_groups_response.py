"""Generated from Smithy shape ``com.amazonaws.groundstation#ListDataflowEndpointGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.dataflow_endpoint_group_list
    import aws_sdk_groundstation.types.pagination_token


class ListDataflowEndpointGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token returned in the response of a previous <code>ListDataflowEndpointGroups</code> call. Used to get the next page of results.</p>"""
    dataflow_endpoint_group_list: NotRequired[
        "aws_sdk_groundstation.types.dataflow_endpoint_group_list.DataflowEndpointGroupList"
    ]
    """<p>A list of dataflow endpoint groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataflowEndpointGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "dataflow_endpoint_group_list" in value:
        import aws_sdk_groundstation.types.dataflow_endpoint_group_list

        out["dataflowEndpointGroupList"] = (
            aws_sdk_groundstation.types.dataflow_endpoint_group_list.serialize_json(
                value["dataflow_endpoint_group_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDataflowEndpointGroupsResponse:
    out: ListDataflowEndpointGroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "dataflowEndpointGroupList" in data:
        import aws_sdk_groundstation.types.dataflow_endpoint_group_list

        out["dataflow_endpoint_group_list"] = (
            aws_sdk_groundstation.types.dataflow_endpoint_group_list.deserialize_json(
                data["dataflowEndpointGroupList"]
            )
        )
    return out
