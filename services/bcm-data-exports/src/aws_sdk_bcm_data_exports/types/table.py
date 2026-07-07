"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#Table``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.generic_string
    import aws_sdk_bcm_data_exports.types.table_name
    import aws_sdk_bcm_data_exports.types.table_property_description_list


class Table(TypedDict, closed=True):
    table_name: NotRequired["aws_sdk_bcm_data_exports.types.table_name.TableName"]
    """<p>The name of the table.</p>"""
    description: NotRequired[
        "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The description for the table.</p>"""
    table_properties: NotRequired[
        "aws_sdk_bcm_data_exports.types.table_property_description_list.TablePropertyDescriptionList"
    ]
    """<p>The properties for the table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Table) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "table_properties" in value:
        import aws_sdk_bcm_data_exports.types.table_property_description_list

        out["TableProperties"] = (
            aws_sdk_bcm_data_exports.types.table_property_description_list.serialize_aws_json_1_1(
                value["table_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Table:
    out: Table = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "TableProperties" in data:
        import aws_sdk_bcm_data_exports.types.table_property_description_list

        out["table_properties"] = (
            aws_sdk_bcm_data_exports.types.table_property_description_list.deserialize_aws_json_1_1(
                data["TableProperties"]
            )
        )
    return out
