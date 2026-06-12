"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeReservedInstancesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.reserved_instance_list
    import aws_sdk_opensearch.types.string


class DescribeReservedInstancesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""
    reserved_instances: NotRequired[
        "aws_sdk_opensearch.types.reserved_instance_list.ReservedInstanceList"
    ]
    """<p>List of Reserved Instances in the current Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservedInstancesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_instances" in value:
        import aws_sdk_opensearch.types.reserved_instance_list

        out["ReservedInstances"] = (
            aws_sdk_opensearch.types.reserved_instance_list.serialize_json(
                value["reserved_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeReservedInstancesResponse:
    out: DescribeReservedInstancesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ReservedInstances" in data:
        import aws_sdk_opensearch.types.reserved_instance_list

        out["reserved_instances"] = (
            aws_sdk_opensearch.types.reserved_instance_list.deserialize_json(
                data["ReservedInstances"]
            )
        )
    return out
