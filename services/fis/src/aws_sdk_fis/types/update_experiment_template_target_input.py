"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateTargetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_target_filter_input_list
    import aws_sdk_fis.types.experiment_template_target_parameter_map
    import aws_sdk_fis.types.experiment_template_target_selection_mode
    import aws_sdk_fis.types.resource_arn_list
    import aws_sdk_fis.types.tag_map
    import aws_sdk_fis.types.target_resource_type_id


class UpdateExperimentTemplateTargetInput(TypedDict, closed=True):
    resource_type: "aws_sdk_fis.types.target_resource_type_id.TargetResourceTypeId"
    """<p>The resource type. The resource type must be supported for the specified action.</p>"""
    resource_arns: NotRequired["aws_sdk_fis.types.resource_arn_list.ResourceArnList"]
    """<p>The Amazon Resource Names (ARNs) of the targets.</p>"""
    resource_tags: NotRequired["aws_sdk_fis.types.tag_map.TagMap"]
    """<p>The tags for the target resources.</p>"""
    filters: NotRequired[
        "aws_sdk_fis.types.experiment_template_target_filter_input_list.ExperimentTemplateTargetFilterInputList"
    ]
    """<p>The filters to apply to identify target resources using specific attributes.</p>"""
    selection_mode: "aws_sdk_fis.types.experiment_template_target_selection_mode.ExperimentTemplateTargetSelectionMode"
    """<p>Scopes the identified resources to a specific count or percentage.</p>"""
    parameters: NotRequired[
        "aws_sdk_fis.types.experiment_template_target_parameter_map.ExperimentTemplateTargetParameterMap"
    ]
    """<p>The resource type parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateTargetInput) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    if "resource_arns" in value:
        import aws_sdk_fis.types.resource_arn_list

        out["resourceArns"] = aws_sdk_fis.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    if "resource_tags" in value:
        import aws_sdk_fis.types.tag_map

        out["resourceTags"] = aws_sdk_fis.types.tag_map.serialize_json(
            value["resource_tags"]
        )
    if "filters" in value:
        import aws_sdk_fis.types.experiment_template_target_filter_input_list

        out["filters"] = (
            aws_sdk_fis.types.experiment_template_target_filter_input_list.serialize_json(
                value["filters"]
            )
        )
    out["selectionMode"] = value["selection_mode"]
    if "parameters" in value:
        import aws_sdk_fis.types.experiment_template_target_parameter_map

        out["parameters"] = (
            aws_sdk_fis.types.experiment_template_target_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateTargetInput:
    out: UpdateExperimentTemplateTargetInput = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError(
            "UpdateExperimentTemplateTargetInput.resource_type required"
        )
    if "resourceArns" in data:
        import aws_sdk_fis.types.resource_arn_list

        out["resource_arns"] = aws_sdk_fis.types.resource_arn_list.deserialize_json(
            data["resourceArns"]
        )
    if "resourceTags" in data:
        import aws_sdk_fis.types.tag_map

        out["resource_tags"] = aws_sdk_fis.types.tag_map.deserialize_json(
            data["resourceTags"]
        )
    if "filters" in data:
        import aws_sdk_fis.types.experiment_template_target_filter_input_list

        out["filters"] = (
            aws_sdk_fis.types.experiment_template_target_filter_input_list.deserialize_json(
                data["filters"]
            )
        )
    if "selectionMode" in data:
        out["selection_mode"] = data["selectionMode"]
    else:
        raise DeserializationError(
            "UpdateExperimentTemplateTargetInput.selection_mode required"
        )
    if "parameters" in data:
        import aws_sdk_fis.types.experiment_template_target_parameter_map

        out["parameters"] = (
            aws_sdk_fis.types.experiment_template_target_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    return out
