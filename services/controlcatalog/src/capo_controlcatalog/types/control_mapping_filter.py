"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlMappingFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_arn_filter_list
    import capo_controlcatalog.types.control_arn_filter_list
    import capo_controlcatalog.types.mapping_type_filter_list


class ControlMappingFilter(TypedDict, closed=True):
    control_arns: NotRequired[
        "capo_controlcatalog.types.control_arn_filter_list.ControlArnFilterList"
    ]
    """<p>A list of control ARNs to filter the mappings. When specified, only mappings associated with these controls are returned.</p>"""
    common_control_arns: NotRequired[
        "capo_controlcatalog.types.common_control_arn_filter_list.CommonControlArnFilterList"
    ]
    """<p>A list of common control ARNs to filter the mappings. When specified, only mappings associated with these common controls are returned.</p>"""
    mapping_types: NotRequired[
        "capo_controlcatalog.types.mapping_type_filter_list.MappingTypeFilterList"
    ]
    """<p>A list of mapping types to filter the mappings. When specified, only mappings of these types are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlMappingFilter) -> dict:
    out: dict = {}
    if "control_arns" in value:
        import capo_controlcatalog.types.control_arn_filter_list

        out["ControlArns"] = (
            capo_controlcatalog.types.control_arn_filter_list.serialize_json(
                value["control_arns"]
            )
        )
    if "common_control_arns" in value:
        import capo_controlcatalog.types.common_control_arn_filter_list

        out["CommonControlArns"] = (
            capo_controlcatalog.types.common_control_arn_filter_list.serialize_json(
                value["common_control_arns"]
            )
        )
    if "mapping_types" in value:
        import capo_controlcatalog.types.mapping_type_filter_list

        out["MappingTypes"] = (
            capo_controlcatalog.types.mapping_type_filter_list.serialize_json(
                value["mapping_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlMappingFilter:
    out: ControlMappingFilter = {}  # type: ignore[typeddict-item]
    if "ControlArns" in data:
        import capo_controlcatalog.types.control_arn_filter_list

        out["control_arns"] = (
            capo_controlcatalog.types.control_arn_filter_list.deserialize_json(
                data["ControlArns"]
            )
        )
    if "CommonControlArns" in data:
        import capo_controlcatalog.types.common_control_arn_filter_list

        out["common_control_arns"] = (
            capo_controlcatalog.types.common_control_arn_filter_list.deserialize_json(
                data["CommonControlArns"]
            )
        )
    if "MappingTypes" in data:
        import capo_controlcatalog.types.mapping_type_filter_list

        out["mapping_types"] = (
            capo_controlcatalog.types.mapping_type_filter_list.deserialize_json(
                data["MappingTypes"]
            )
        )
    return out
