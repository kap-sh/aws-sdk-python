"""Generated from Smithy shape ``com.amazonaws.sagemaker#LineageGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.lineage_group_arn
    import capo_sagemaker.types.timestamp


class LineageGroupSummary(TypedDict, closed=True):
    lineage_group_arn: NotRequired[
        "capo_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group resource.</p>"""
    lineage_group_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the lineage group.</p>"""
    display_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The display name of the lineage group summary.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the lineage group summary.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The last modified time of the lineage group summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineageGroupSummary) -> dict:
    out: dict = {}
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    if "lineage_group_name" in value:
        out["LineageGroupName"] = value["lineage_group_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LineageGroupSummary:
    out: LineageGroupSummary = {}  # type: ignore[typeddict-item]
    if "LineageGroupArn" in data:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    if "LineageGroupName" in data:
        out["lineage_group_name"] = data["LineageGroupName"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
