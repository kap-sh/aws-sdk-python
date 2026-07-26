"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.action_arn
    import capo_sagemaker.types.action_source
    import capo_sagemaker.types.action_status
    import capo_sagemaker.types.experiment_description
    import capo_sagemaker.types.experiment_entity_name_or_arn
    import capo_sagemaker.types.lineage_entity_parameters
    import capo_sagemaker.types.lineage_group_arn
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribeActionResponse(TypedDict, closed=True):
    action_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name_or_arn.ExperimentEntityNameOrArn"
    ]
    """<p>The name of the action.</p>"""
    action_arn: NotRequired["capo_sagemaker.types.action_arn.ActionArn"]
    """<p>The Amazon Resource Name (ARN) of the action.</p>"""
    source: NotRequired["capo_sagemaker.types.action_source.ActionSource"]
    """<p>The source of the action.</p>"""
    action_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The type of the action.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the action.</p>"""
    status: NotRequired["capo_sagemaker.types.action_status.ActionStatus"]
    """<p>The status of the action.</p>"""
    properties: NotRequired[
        "capo_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>A list of the action's properties.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the action was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the action was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    lineage_group_arn: NotRequired[
        "capo_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeActionResponse) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "action_arn" in value:
        out["ActionArn"] = value["action_arn"]
    if "source" in value:
        import capo_sagemaker.types.action_source

        out["Source"] = capo_sagemaker.types.action_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "action_type" in value:
        out["ActionType"] = value["action_type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_sagemaker.types.action_status

        out["Status"] = capo_sagemaker.types.action_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "properties" in value:
        import capo_sagemaker.types.lineage_entity_parameters

        out["Properties"] = (
            capo_sagemaker.types.lineage_entity_parameters.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "metadata_properties" in value:
        import capo_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            capo_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeActionResponse:
    out: DescribeActionResponse = {}  # type: ignore[typeddict-item]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    if "ActionArn" in data:
        out["action_arn"] = data["ActionArn"]
    if "Source" in data:
        import capo_sagemaker.types.action_source

        out["source"] = capo_sagemaker.types.action_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ActionType" in data:
        out["action_type"] = data["ActionType"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_sagemaker.types.action_status

        out["status"] = capo_sagemaker.types.action_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Properties" in data:
        import capo_sagemaker.types.lineage_entity_parameters

        out["properties"] = (
            capo_sagemaker.types.lineage_entity_parameters.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastModifiedBy" in data:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if "MetadataProperties" in data:
        import capo_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            capo_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "LineageGroupArn" in data:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    return out
