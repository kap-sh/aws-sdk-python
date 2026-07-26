"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.action_source
    import capo_sagemaker.types.action_status
    import capo_sagemaker.types.experiment_description
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.lineage_entity_parameters
    import capo_sagemaker.types.metadata_properties
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.tag_list


class CreateActionRequest(TypedDict, closed=True):
    action_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the action. Must be unique to your account in an Amazon Web Services Region.</p>"""
    source: NotRequired["capo_sagemaker.types.action_source.ActionSource"]
    """<p>The source type, ID, and URI.</p>"""
    action_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The action type.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The description of the action.</p>"""
    status: NotRequired["capo_sagemaker.types.action_status.ActionStatus"]
    """<p>The status of the action.</p>"""
    properties: NotRequired[
        "capo_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>A list of properties to add to the action.</p>"""
    metadata_properties: NotRequired[
        "capo_sagemaker.types.metadata_properties.MetadataProperties"
    ]
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateActionRequest) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
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
    if "metadata_properties" in value:
        import capo_sagemaker.types.metadata_properties

        out["MetadataProperties"] = (
            capo_sagemaker.types.metadata_properties.serialize_aws_json_1_1(
                value["metadata_properties"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateActionRequest:
    out: CreateActionRequest = {}  # type: ignore[typeddict-item]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
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
    if "MetadataProperties" in data:
        import capo_sagemaker.types.metadata_properties

        out["metadata_properties"] = (
            capo_sagemaker.types.metadata_properties.deserialize_aws_json_1_1(
                data["MetadataProperties"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
