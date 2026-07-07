"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeLineageGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_description
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.lineage_group_arn
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.user_context


class DescribeLineageGroupResponse(TypedDict, closed=True):
    lineage_group_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the lineage group.</p>"""
    lineage_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The display name of the lineage group.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the lineage group.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of lineage group.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last modified time of the lineage group.</p>"""
    last_modified_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLineageGroupResponse) -> dict:
    out: dict = {}
    if "lineage_group_name" in value:
        out["LineageGroupName"] = value["lineage_group_name"]
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_modified_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLineageGroupResponse:
    out: DescribeLineageGroupResponse = {}  # type: ignore[typeddict-item]
    if "LineageGroupName" in data:
        out["lineage_group_name"] = data["LineageGroupName"]
    if "LineageGroupArn" in data:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["last_modified_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    return out
