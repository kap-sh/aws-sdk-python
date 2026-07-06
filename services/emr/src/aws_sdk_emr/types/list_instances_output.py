"""Generated from Smithy shape ``com.amazonaws.emr#ListInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_list
    import aws_sdk_emr.types.marker


class ListInstancesOutput(TypedDict, closed=True):
    instances: NotRequired["aws_sdk_emr.types.instance_list.InstanceList"]
    """<p>The list of instances for the cluster and given filters.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstancesOutput) -> dict:
    out: dict = {}
    if "instances" in value:
        import aws_sdk_emr.types.instance_list

        out["Instances"] = aws_sdk_emr.types.instance_list.serialize_aws_json_1_1(
            value["instances"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstancesOutput:
    out: ListInstancesOutput = {}  # type: ignore[typeddict-item]
    if "Instances" in data:
        import aws_sdk_emr.types.instance_list

        out["instances"] = aws_sdk_emr.types.instance_list.deserialize_aws_json_1_1(
            data["Instances"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
