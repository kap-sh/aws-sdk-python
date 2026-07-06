"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.action_source
    import aws_sdk_sagemaker.types.action_status
    import aws_sdk_sagemaker.types.experiment_description
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.lineage_entity_parameters
    import aws_sdk_sagemaker.types.metadata_properties
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.tag_list


class CreateActionRequest(TypedDict, closed=True):
    action_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the action. Must be unique to your account in an Amazon Web Services Region.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.action_source.ActionSource"]
    """<p>The source type, ID, and URI.</p>"""
    action_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The action type.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the action.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.action_status.ActionStatus"]
    """<p>The status of the action.</p>"""
    properties: NotRequired[
        "aws_sdk_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>A list of properties to add to the action.</p>"""
    metadata_properties: NotRequired[
        "aws_sdk_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateActionRequest) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "source" in value:
        import aws_sdk_sagemaker.types.action_source

        out["Source"] = aws_sdk_sagemaker.types.action_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "action_type" in value:
        out["ActionType"] = value["action_type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_sagemaker.types.action_status

        out["Status"] = aws_sdk_sagemaker.types.action_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "properties" in value:
        import aws_sdk_sagemaker.types.lineage_entity_parameters

        out["Properties"] = (
            aws_sdk_sagemaker.types.lineage_entity_parameters.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "metadata_properties" in value:
        import aws_sdk_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            aws_sdk_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateActionRequest:
    out: CreateActionRequest = {}  # type: ignore[typeddict-item]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.action_source

        out["source"] = aws_sdk_sagemaker.types.action_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ActionType" in data:
        out["action_type"] = data["ActionType"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.action_status

        out["status"] = aws_sdk_sagemaker.types.action_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Properties" in data:
        import aws_sdk_sagemaker.types.lineage_entity_parameters

        out["properties"] = (
            aws_sdk_sagemaker.types.lineage_entity_parameters.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "MetadataProperties" in data:
        import aws_sdk_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            aws_sdk_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
