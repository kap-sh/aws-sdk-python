"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldOptionsCaseRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id
    import aws_sdk_connectcases.types.parent_child_field_options_mapping_list


class FieldOptionsCaseRule(TypedDict):
    parent_field_id: NotRequired["aws_sdk_connectcases.types.field_id.FieldId"]
    """<p>The identifier of the parent field that controls options.</p>"""
    child_field_id: NotRequired["aws_sdk_connectcases.types.field_id.FieldId"]
    """<p>The identifier of the child field whose options are controlled.</p>"""
    parent_child_field_options_mappings: "aws_sdk_connectcases.types.parent_child_field_options_mapping_list.ParentChildFieldOptionsMappingList"
    """<p>A mapping between a parent field option value and child field option values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldOptionsCaseRule) -> dict:
    out: dict = {}
    if "parent_field_id" in value:
        out["parentFieldId"] = value["parent_field_id"]
    if "child_field_id" in value:
        out["childFieldId"] = value["child_field_id"]
    import aws_sdk_connectcases.types.parent_child_field_options_mapping_list

    out["parentChildFieldOptionsMappings"] = (
        aws_sdk_connectcases.types.parent_child_field_options_mapping_list.serialize_json(
            value["parent_child_field_options_mappings"]
        )
    )
    return out


def deserialize_json(data: dict) -> FieldOptionsCaseRule:
    out: FieldOptionsCaseRule = {}  # type: ignore[typeddict-item]
    if "parentFieldId" in data:
        out["parent_field_id"] = data["parentFieldId"]
    if "childFieldId" in data:
        out["child_field_id"] = data["childFieldId"]
    if "parentChildFieldOptionsMappings" in data:
        import aws_sdk_connectcases.types.parent_child_field_options_mapping_list

        out["parent_child_field_options_mappings"] = (
            aws_sdk_connectcases.types.parent_child_field_options_mapping_list.deserialize_json(
                data["parentChildFieldOptionsMappings"]
            )
        )
    else:
        raise DeserializationError(
            "FieldOptionsCaseRule.parent_child_field_options_mappings required"
        )
    return out
