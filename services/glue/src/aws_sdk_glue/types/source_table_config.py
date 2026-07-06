"""Generated from Smithy shape ``com.amazonaws.glue#SourceTableConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.primary_key_list
    import aws_sdk_glue.types.source_table_fields_list
    import aws_sdk_glue.types.string128


class SourceTableConfig(TypedDict, closed=True):
    fields: NotRequired[
        "aws_sdk_glue.types.source_table_fields_list.SourceTableFieldsList"
    ]
    """<p>A list of fields used for column-level filtering. Currently unsupported.</p>"""
    filter_predicate: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>A condition clause used for row-level filtering. Currently unsupported.</p>"""
    primary_key: NotRequired["aws_sdk_glue.types.primary_key_list.PrimaryKeyList"]
    """<p>Provide the primary key set for this table. Currently supported specifically for SAP <code>EntityOf</code> entities upon request. Contact Amazon Web Services Support to make this feature available.</p>"""
    record_update_field: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>Incremental pull timestamp-based field. Currently unsupported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceTableConfig) -> dict:
    out: dict = {}
    if "fields" in value:
        import aws_sdk_glue.types.source_table_fields_list

        out["Fields"] = (
            aws_sdk_glue.types.source_table_fields_list.serialize_aws_json_1_1(
                value["fields"]
            )
        )
    if "filter_predicate" in value:
        out["FilterPredicate"] = value["filter_predicate"]
    if "primary_key" in value:
        import aws_sdk_glue.types.primary_key_list

        out["PrimaryKey"] = aws_sdk_glue.types.primary_key_list.serialize_aws_json_1_1(
            value["primary_key"]
        )
    if "record_update_field" in value:
        out["RecordUpdateField"] = value["record_update_field"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceTableConfig:
    out: SourceTableConfig = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_glue.types.source_table_fields_list

        out["fields"] = (
            aws_sdk_glue.types.source_table_fields_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    if "FilterPredicate" in data:
        out["filter_predicate"] = data["FilterPredicate"]
    if "PrimaryKey" in data:
        import aws_sdk_glue.types.primary_key_list

        out["primary_key"] = (
            aws_sdk_glue.types.primary_key_list.deserialize_aws_json_1_1(
                data["PrimaryKey"]
            )
        )
    if "RecordUpdateField" in data:
        out["record_update_field"] = data["RecordUpdateField"]
    return out
