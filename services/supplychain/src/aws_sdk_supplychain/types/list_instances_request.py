"""Generated from Smithy shape ``com.amazonaws.supplychain#ListInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.instance_max_results
    import aws_sdk_supplychain.types.instance_name_list
    import aws_sdk_supplychain.types.instance_next_token
    import aws_sdk_supplychain.types.instance_state_list


class ListInstancesRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_supplychain.types.instance_next_token.InstanceNextToken"
    ]
    """<p>The pagination token to fetch the next page of instances.</p>"""
    max_results: "aws_sdk_supplychain.types.instance_max_results.InstanceMaxResults"
    """<p>Specify the maximum number of instances to fetch in this paginated request.</p>"""
    instance_name_filter: NotRequired[
        "aws_sdk_supplychain.types.instance_name_list.InstanceNameList"
    ]
    """<p>The filter to ListInstances based on their names.</p>"""
    instance_state_filter: NotRequired[
        "aws_sdk_supplychain.types.instance_state_list.InstanceStateList"
    ]
    """<p>The filter to ListInstances based on their state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInstancesRequest:
    out: ListInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
