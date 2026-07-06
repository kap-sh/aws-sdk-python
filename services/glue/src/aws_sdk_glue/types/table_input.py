"""Generated from Smithy shape ``com.amazonaws.glue#TableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_list
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.non_negative_integer
    import aws_sdk_glue.types.parameters_map
    import aws_sdk_glue.types.storage_descriptor
    import aws_sdk_glue.types.table_identifier
    import aws_sdk_glue.types.table_type_string
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.view_definition_input
    import aws_sdk_glue.types.view_text_string


class TableInput(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The table name. For Hive compatibility, this is folded to lowercase when it is stored.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the table.</p>"""
    owner: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The table owner. Included for Apache Hive compatibility. Not used in the normal course of Glue operations.</p>"""
    last_access_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The last time that the table was accessed.</p>"""
    last_analyzed_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The last time that column statistics were computed for this table.</p>"""
    retention: "aws_sdk_glue.types.non_negative_integer.NonNegativeInteger"
    """<p>The retention time for this table.</p>"""
    storage_descriptor: NotRequired[
        "aws_sdk_glue.types.storage_descriptor.StorageDescriptor"
    ]
    """<p>A storage descriptor containing information about the physical storage of this table.</p>"""
    partition_keys: NotRequired["aws_sdk_glue.types.column_list.ColumnList"]
    r"""<p>A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.</p> <p>When you create a table used by Amazon Athena, and you do not specify any <code>partitionKeys</code>, you must at least set the value of <code>partitionKeys</code> to an empty list. For example:</p> <p> <code>\"PartitionKeys\": []</code> </p>"""
    view_original_text: NotRequired[
        "aws_sdk_glue.types.view_text_string.ViewTextString"
    ]
    """<p>Included for Apache Hive compatibility. Not used in the normal course of Glue operations. If the table is a <code>VIRTUAL_VIEW</code>, certain Athena configuration encoded in base64.</p>"""
    view_expanded_text: NotRequired[
        "aws_sdk_glue.types.view_text_string.ViewTextString"
    ]
    """<p>Included for Apache Hive compatibility. Not used in the normal course of Glue operations.</p>"""
    table_type: NotRequired["aws_sdk_glue.types.table_type_string.TableTypeString"]
    """<p>The type of this table. Glue will create tables with the <code>EXTERNAL_TABLE</code> type. Other services, such as Athena, may create tables with additional table types. </p> <p>Glue related table types:</p> <dl> <dt>EXTERNAL_TABLE</dt> <dd> <p>Hive compatible attribute - indicates a non-Hive managed table.</p> </dd> <dt>GOVERNED</dt> <dd> <p>Used by Lake Formation. The Glue Data Catalog understands <code>GOVERNED</code>.</p> </dd> </dl>"""
    parameters: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define properties associated with the table.</p>"""
    target_table: NotRequired["aws_sdk_glue.types.table_identifier.TableIdentifier"]
    """<p>A <code>TableIdentifier</code> structure that describes a target table for resource linking.</p>"""
    view_definition: NotRequired[
        "aws_sdk_glue.types.view_definition_input.ViewDefinitionInput"
    ]
    """<p>A structure that contains all the information that defines the view, including the dialect or dialects for the view, and the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "last_access_time" in value:
        import aws_sdk_glue.types.timestamp

        out["LastAccessTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_access_time"]
        )
    if "last_analyzed_time" in value:
        import aws_sdk_glue.types.timestamp

        out["LastAnalyzedTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_analyzed_time"]
        )
    out["Retention"] = value.get("retention", 0)
    if "storage_descriptor" in value:
        import aws_sdk_glue.types.storage_descriptor

        out["StorageDescriptor"] = (
            aws_sdk_glue.types.storage_descriptor.serialize_aws_json_1_1(
                value["storage_descriptor"]
            )
        )
    if "partition_keys" in value:
        import aws_sdk_glue.types.column_list

        out["PartitionKeys"] = aws_sdk_glue.types.column_list.serialize_aws_json_1_1(
            value["partition_keys"]
        )
    if "view_original_text" in value:
        out["ViewOriginalText"] = value["view_original_text"]
    if "view_expanded_text" in value:
        out["ViewExpandedText"] = value["view_expanded_text"]
    if "table_type" in value:
        out["TableType"] = value["table_type"]
    if "parameters" in value:
        import aws_sdk_glue.types.parameters_map

        out["Parameters"] = aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "target_table" in value:
        import aws_sdk_glue.types.table_identifier

        out["TargetTable"] = aws_sdk_glue.types.table_identifier.serialize_aws_json_1_1(
            value["target_table"]
        )
    if "view_definition" in value:
        import aws_sdk_glue.types.view_definition_input

        out["ViewDefinition"] = (
            aws_sdk_glue.types.view_definition_input.serialize_aws_json_1_1(
                value["view_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableInput:
    out: TableInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TableInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "LastAccessTime" in data:
        import aws_sdk_glue.types.timestamp

        out["last_access_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastAccessTime"]
        )
    if "LastAnalyzedTime" in data:
        import aws_sdk_glue.types.timestamp

        out["last_analyzed_time"] = (
            aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
                data["LastAnalyzedTime"]
            )
        )
    if "Retention" in data:
        out["retention"] = data["Retention"]
    else:
        out["retention"] = 0
    if "StorageDescriptor" in data:
        import aws_sdk_glue.types.storage_descriptor

        out["storage_descriptor"] = (
            aws_sdk_glue.types.storage_descriptor.deserialize_aws_json_1_1(
                data["StorageDescriptor"]
            )
        )
    if "PartitionKeys" in data:
        import aws_sdk_glue.types.column_list

        out["partition_keys"] = aws_sdk_glue.types.column_list.deserialize_aws_json_1_1(
            data["PartitionKeys"]
        )
    if "ViewOriginalText" in data:
        out["view_original_text"] = data["ViewOriginalText"]
    if "ViewExpandedText" in data:
        out["view_expanded_text"] = data["ViewExpandedText"]
    if "TableType" in data:
        out["table_type"] = data["TableType"]
    if "Parameters" in data:
        import aws_sdk_glue.types.parameters_map

        out["parameters"] = aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "TargetTable" in data:
        import aws_sdk_glue.types.table_identifier

        out["target_table"] = (
            aws_sdk_glue.types.table_identifier.deserialize_aws_json_1_1(
                data["TargetTable"]
            )
        )
    if "ViewDefinition" in data:
        import aws_sdk_glue.types.view_definition_input

        out["view_definition"] = (
            aws_sdk_glue.types.view_definition_input.deserialize_aws_json_1_1(
                data["ViewDefinition"]
            )
        )
    return out
