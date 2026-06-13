"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetTableResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.column_list
    import aws_sdk_bcm_data_exports.types.generic_string
    import aws_sdk_bcm_data_exports.types.table_name
    import aws_sdk_bcm_data_exports.types.table_properties


class GetTableResponse(TypedDict):
    table_name: NotRequired["aws_sdk_bcm_data_exports.types.table_name.TableName"]
    """<p>The name of the table.</p>"""
    description: NotRequired[
        "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The table description.</p>"""
    table_properties: NotRequired[
        "aws_sdk_bcm_data_exports.types.table_properties.TableProperties"
    ]
    """<p>TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. Tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified.</p>"""
    schema: NotRequired["aws_sdk_bcm_data_exports.types.column_list.ColumnList"]
    """<p>The schema of the table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableResponse) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "table_properties" in value:
        import aws_sdk_bcm_data_exports.types.table_properties

        out["TableProperties"] = (
            aws_sdk_bcm_data_exports.types.table_properties.serialize_aws_json_1_1(
                value["table_properties"]
            )
        )
    if "schema" in value:
        import aws_sdk_bcm_data_exports.types.column_list

        out["Schema"] = (
            aws_sdk_bcm_data_exports.types.column_list.serialize_aws_json_1_1(
                value["schema"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableResponse:
    out: GetTableResponse = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "TableProperties" in data:
        import aws_sdk_bcm_data_exports.types.table_properties

        out["table_properties"] = (
            aws_sdk_bcm_data_exports.types.table_properties.deserialize_aws_json_1_1(
                data["TableProperties"]
            )
        )
    if "Schema" in data:
        import aws_sdk_bcm_data_exports.types.column_list

        out["schema"] = (
            aws_sdk_bcm_data_exports.types.column_list.deserialize_aws_json_1_1(
                data["Schema"]
            )
        )
    return out
