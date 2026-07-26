"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#TablePropertyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.generic_string
    import capo_bcm_data_exports.types.generic_string_list


class TablePropertyDescription(TypedDict, closed=True):
    name: NotRequired["capo_bcm_data_exports.types.generic_string.GenericString"]
    """<p>The name of the table.</p>"""
    valid_values: NotRequired[
        "capo_bcm_data_exports.types.generic_string_list.GenericStringList"
    ]
    """<p>The valid values for the table.</p>"""
    default_value: NotRequired[
        "capo_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The default value for the table.</p>"""
    description: NotRequired["capo_bcm_data_exports.types.generic_string.GenericString"]
    """<p>The description for the table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TablePropertyDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "valid_values" in value:
        import capo_bcm_data_exports.types.generic_string_list

        out["ValidValues"] = (
            capo_bcm_data_exports.types.generic_string_list.serialize_aws_json_1_1(
                value["valid_values"]
            )
        )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TablePropertyDescription:
    out: TablePropertyDescription = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ValidValues" in data:
        import capo_bcm_data_exports.types.generic_string_list

        out["valid_values"] = (
            capo_bcm_data_exports.types.generic_string_list.deserialize_aws_json_1_1(
                data["ValidValues"]
            )
        )
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
