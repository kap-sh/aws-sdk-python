"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.action_status
    import aws_sdk_sagemaker.types.experiment_description
    import aws_sdk_sagemaker.types.experiment_entity_name
    import aws_sdk_sagemaker.types.lineage_entity_parameters
    import aws_sdk_sagemaker.types.list_lineage_entity_parameter_key


class UpdateActionRequest(TypedDict):
    action_name: NotRequired[
        "aws_sdk_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the action to update.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The new description for the action.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.action_status.ActionStatus"]
    """<p>The new status for the action.</p>"""
    properties: NotRequired[
        "aws_sdk_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>The new list of properties. Overwrites the current property list.</p>"""
    properties_to_remove: NotRequired[
        "aws_sdk_sagemaker.types.list_lineage_entity_parameter_key.ListLineageEntityParameterKey"
    ]
    """<p>A list of properties to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateActionRequest) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
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
    if "properties_to_remove" in value:
        import aws_sdk_sagemaker.types.list_lineage_entity_parameter_key

        out["PropertiesToRemove"] = (
            aws_sdk_sagemaker.types.list_lineage_entity_parameter_key.serialize_aws_json_1_1(
                value["properties_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateActionRequest:
    out: UpdateActionRequest = {}  # type: ignore[typeddict-item]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
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
    if "PropertiesToRemove" in data:
        import aws_sdk_sagemaker.types.list_lineage_entity_parameter_key

        out["properties_to_remove"] = (
            aws_sdk_sagemaker.types.list_lineage_entity_parameter_key.deserialize_aws_json_1_1(
                data["PropertiesToRemove"]
            )
        )
    return out
