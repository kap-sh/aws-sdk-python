"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_target_filter_list
    import capo_fis.types.experiment_target_parameter_map
    import capo_fis.types.experiment_target_selection_mode
    import capo_fis.types.resource_arn_list
    import capo_fis.types.tag_map
    import capo_fis.types.target_resource_type_id


class ExperimentTarget(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_fis.types.target_resource_type_id.TargetResourceTypeId"
    ]
    """<p>The resource type.</p>"""
    resource_arns: NotRequired["capo_fis.types.resource_arn_list.ResourceArnList"]
    """<p>The Amazon Resource Names (ARNs) of the resources.</p>"""
    resource_tags: NotRequired["capo_fis.types.tag_map.TagMap"]
    """<p>The tags for the target resources.</p>"""
    filters: NotRequired[
        "capo_fis.types.experiment_target_filter_list.ExperimentTargetFilterList"
    ]
    """<p>The filters to apply to identify target resources using specific attributes.</p>"""
    selection_mode: NotRequired[
        "capo_fis.types.experiment_target_selection_mode.ExperimentTargetSelectionMode"
    ]
    """<p>Scopes the identified resources to a specific count or percentage.</p>"""
    parameters: NotRequired[
        "capo_fis.types.experiment_target_parameter_map.ExperimentTargetParameterMap"
    ]
    """<p>The resource type parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTarget) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "resource_arns" in value:
        import capo_fis.types.resource_arn_list

        out["resourceArns"] = capo_fis.types.resource_arn_list.serialize_json(
            value["resource_arns"]
        )
    if "resource_tags" in value:
        import capo_fis.types.tag_map

        out["resourceTags"] = capo_fis.types.tag_map.serialize_json(
            value["resource_tags"]
        )
    if "filters" in value:
        import capo_fis.types.experiment_target_filter_list

        out["filters"] = capo_fis.types.experiment_target_filter_list.serialize_json(
            value["filters"]
        )
    if "selection_mode" in value:
        out["selectionMode"] = value["selection_mode"]
    if "parameters" in value:
        import capo_fis.types.experiment_target_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_target_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentTarget:
    out: ExperimentTarget = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "resourceArns" in data:
        import capo_fis.types.resource_arn_list

        out["resource_arns"] = capo_fis.types.resource_arn_list.deserialize_json(
            data["resourceArns"]
        )
    if "resourceTags" in data:
        import capo_fis.types.tag_map

        out["resource_tags"] = capo_fis.types.tag_map.deserialize_json(
            data["resourceTags"]
        )
    if "filters" in data:
        import capo_fis.types.experiment_target_filter_list

        out["filters"] = capo_fis.types.experiment_target_filter_list.deserialize_json(
            data["filters"]
        )
    if "selectionMode" in data:
        out["selection_mode"] = data["selectionMode"]
    if "parameters" in data:
        import capo_fis.types.experiment_target_parameter_map

        out["parameters"] = (
            capo_fis.types.experiment_target_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    return out
