"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeLineageGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_entity_name


class DescribeLineageGroupRequest(TypedDict, closed=True):
    lineage_group_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the lineage group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLineageGroupRequest) -> dict:
    out: dict = {}
    if "lineage_group_name" in value:
        out["LineageGroupName"] = value["lineage_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLineageGroupRequest:
    out: DescribeLineageGroupRequest = {}  # type: ignore[typeddict-item]
    if "LineageGroupName" in data:
        out["lineage_group_name"] = data["LineageGroupName"]
    return out
