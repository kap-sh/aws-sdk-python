"""Generated from Smithy shape ``com.amazonaws.kafka#ListNodesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_node_info
    import aws_sdk_kafka.types.__string


class ListNodesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a ListNodes operation is truncated, the call returns NextToken in the response. To get another batch of nodes, provide this token in your next request.</p>"""
    node_info_list: NotRequired[
        "aws_sdk_kafka.types.__list_of_node_info.__listOfNodeInfo"
    ]
    """<p>List containing a NodeInfo object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "node_info_list" in value:
        import aws_sdk_kafka.types.__list_of_node_info

        out["nodeInfoList"] = aws_sdk_kafka.types.__list_of_node_info.serialize_json(
            value["node_info_list"]
        )
    return out


def deserialize_json(data: dict) -> ListNodesResponse:
    out: ListNodesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "nodeInfoList" in data:
        import aws_sdk_kafka.types.__list_of_node_info

        out["node_info_list"] = (
            aws_sdk_kafka.types.__list_of_node_info.deserialize_json(
                data["nodeInfoList"]
            )
        )
    return out
