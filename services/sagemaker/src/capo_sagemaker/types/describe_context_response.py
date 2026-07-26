"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeContextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.context_arn
    import capo_sagemaker.types.context_name
    import capo_sagemaker.types.context_source
    import capo_sagemaker.types.experiment_description
    import capo_sagemaker.types.lineage_entity_parameters
    import capo_sagemaker.types.lineage_group_arn
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribeContextResponse(TypedDict, closed=True):
    context_name: NotRequired["capo_sagemaker.types.context_name.ContextName"]
    """<p>The name of the context.</p>"""
    context_arn: NotRequired["capo_sagemaker.types.context_arn.ContextArn"]
    """<p>The Amazon Resource Name (ARN) of the context.</p>"""
    source: NotRequired["capo_sagemaker.types.context_source.ContextSource"]
    """<p>The source of the context.</p>"""
    context_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The type of the context.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the context.</p>"""
    properties: NotRequired[
        "capo_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>A list of the context's properties.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the context was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the context was last modified.</p>"""
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    lineage_group_arn: NotRequired[
        "capo_sagemaker.types.lineage_group_arn.LineageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContextResponse) -> dict:
    out: dict = {}
    if "context_name" in value:
        out["ContextName"] = value["context_name"]
    if "context_arn" in value:
        out["ContextArn"] = value["context_arn"]
    if "source" in value:
        import capo_sagemaker.types.context_source

        out["Source"] = capo_sagemaker.types.context_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "context_type" in value:
        out["ContextType"] = value["context_type"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "lineage_group_arn" in value:
        out["LineageGroupArn"] = value["lineage_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContextResponse:
    out: DescribeContextResponse = {}  # type: ignore[typeddict-item]
    if "ContextName" in data:
        out["context_name"] = data["ContextName"]
    if "ContextArn" in data:
        out["context_arn"] = data["ContextArn"]
    if "Source" in data:
        import capo_sagemaker.types.context_source

        out["source"] = capo_sagemaker.types.context_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ContextType" in data:
        out["context_type"] = data["ContextType"]
    if "Description" in data:
        out["description"] = data["Description"]
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
    if "LineageGroupArn" in data:
        out["lineage_group_arn"] = data["LineageGroupArn"]
    return out
