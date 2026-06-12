"""Generated from Smithy shape ``com.amazonaws.emr#ListInstanceGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_group_list
    import aws_sdk_emr.types.marker


class ListInstanceGroupsOutput(TypedDict):
    instance_groups: NotRequired[
        "aws_sdk_emr.types.instance_group_list.InstanceGroupList"
    ]
    """<p>The list of instance groups for the cluster and given filters.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstanceGroupsOutput) -> dict:
    out: dict = {}
    if "instance_groups" in value:
        import aws_sdk_emr.types.instance_group_list

        out["InstanceGroups"] = (
            aws_sdk_emr.types.instance_group_list.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstanceGroupsOutput:
    out: ListInstanceGroupsOutput = {}  # type: ignore[typeddict-item]
    if "InstanceGroups" in data:
        import aws_sdk_emr.types.instance_group_list

        out["instance_groups"] = (
            aws_sdk_emr.types.instance_group_list.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
