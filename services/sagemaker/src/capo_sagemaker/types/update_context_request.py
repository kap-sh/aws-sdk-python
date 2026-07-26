"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateContextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.context_name
    import capo_sagemaker.types.experiment_description
    import capo_sagemaker.types.lineage_entity_parameters
    import capo_sagemaker.types.list_lineage_entity_parameter_key


class UpdateContextRequest(TypedDict, closed=True):
    context_name: NotRequired["capo_sagemaker.types.context_name.ContextName"]
    """<p>The name of the context to update.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.experiment_description.ExperimentDescription"
    ]
    """<p>The new description for the context.</p>"""
    properties: NotRequired[
        "capo_sagemaker.types.lineage_entity_parameters.LineageEntityParameters"
    ]
    """<p>The new list of properties. Overwrites the current property list.</p>"""
    properties_to_remove: NotRequired[
        "capo_sagemaker.types.list_lineage_entity_parameter_key.ListLineageEntityParameterKey"
    ]
    """<p>A list of properties to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContextRequest) -> dict:
    out: dict = {}
    if "context_name" in value:
        out["ContextName"] = value["context_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "properties" in value:
        import capo_sagemaker.types.lineage_entity_parameters

        out["Properties"] = (
            capo_sagemaker.types.lineage_entity_parameters.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "properties_to_remove" in value:
        import capo_sagemaker.types.list_lineage_entity_parameter_key

        out["PropertiesToRemove"] = (
            capo_sagemaker.types.list_lineage_entity_parameter_key.serialize_aws_json_1_1(
                value["properties_to_remove"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContextRequest:
    out: UpdateContextRequest = {}  # type: ignore[typeddict-item]
    if "ContextName" in data:
        out["context_name"] = data["ContextName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Properties" in data:
        import capo_sagemaker.types.lineage_entity_parameters

        out["properties"] = (
            capo_sagemaker.types.lineage_entity_parameters.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "PropertiesToRemove" in data:
        import capo_sagemaker.types.list_lineage_entity_parameter_key

        out["properties_to_remove"] = (
            capo_sagemaker.types.list_lineage_entity_parameter_key.deserialize_aws_json_1_1(
                data["PropertiesToRemove"]
            )
        )
    return out
