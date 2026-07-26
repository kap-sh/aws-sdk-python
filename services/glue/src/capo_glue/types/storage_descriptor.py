"""Generated from Smithy shape ``com.amazonaws.glue#StorageDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boolean
    import capo_glue.types.column_list
    import capo_glue.types.format_string
    import capo_glue.types.integer
    import capo_glue.types.location_string
    import capo_glue.types.location_string_list
    import capo_glue.types.name_string_list
    import capo_glue.types.order_list
    import capo_glue.types.parameters_map
    import capo_glue.types.schema_reference
    import capo_glue.types.ser_de_info
    import capo_glue.types.skewed_info


class StorageDescriptor(TypedDict, closed=True):
    columns: NotRequired["capo_glue.types.column_list.ColumnList"]
    """<p>A list of the <code>Columns</code> in the table.</p>"""
    location: NotRequired["capo_glue.types.location_string.LocationString"]
    """<p>The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.</p>"""
    additional_locations: NotRequired[
        "capo_glue.types.location_string_list.LocationStringList"
    ]
    """<p>A list of locations that point to the path where a Delta table is located.</p>"""
    input_format: NotRequired["capo_glue.types.format_string.FormatString"]
    """<p>The input format: <code>SequenceFileInputFormat</code> (binary), or <code>TextInputFormat</code>, or a custom format.</p>"""
    output_format: NotRequired["capo_glue.types.format_string.FormatString"]
    """<p>The output format: <code>SequenceFileOutputFormat</code> (binary), or <code>IgnoreKeyTextOutputFormat</code>, or a custom format.</p>"""
    compressed: "capo_glue.types.boolean.Boolean"
    """<p> <code>True</code> if the data in the table is compressed, or <code>False</code> if not.</p>"""
    number_of_buckets: "capo_glue.types.integer.Integer"
    """<p>Must be specified if the table contains any dimension columns.</p>"""
    serde_info: NotRequired["capo_glue.types.ser_de_info.SerDeInfo"]
    """<p>The serialization/deserialization (SerDe) information.</p>"""
    bucket_columns: NotRequired["capo_glue.types.name_string_list.NameStringList"]
    """<p>A list of reducer grouping columns, clustering columns, and bucketing columns in the table.</p>"""
    sort_columns: NotRequired["capo_glue.types.order_list.OrderList"]
    """<p>A list specifying the sort order of each bucket in the table.</p>"""
    parameters: NotRequired["capo_glue.types.parameters_map.ParametersMap"]
    """<p>The user-supplied properties in key-value form.</p>"""
    skewed_info: NotRequired["capo_glue.types.skewed_info.SkewedInfo"]
    """<p>The information about values that appear frequently in a column (skewed values).</p>"""
    stored_as_sub_directories: "capo_glue.types.boolean.Boolean"
    """<p> <code>True</code> if the table data is stored in subdirectories, or <code>False</code> if not.</p>"""
    schema_reference: NotRequired["capo_glue.types.schema_reference.SchemaReference"]
    """<p>An object that references a schema stored in the Glue Schema Registry.</p> <p>When creating a table, you can pass an empty list of columns for the schema, and instead use a schema reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageDescriptor) -> dict:
    out: dict = {}
    if "columns" in value:
        import capo_glue.types.column_list

        out["Columns"] = capo_glue.types.column_list.serialize_aws_json_1_1(
            value["columns"]
        )
    if "location" in value:
        out["Location"] = value["location"]
    if "additional_locations" in value:
        import capo_glue.types.location_string_list

        out["AdditionalLocations"] = (
            capo_glue.types.location_string_list.serialize_aws_json_1_1(
                value["additional_locations"]
            )
        )
    if "input_format" in value:
        out["InputFormat"] = value["input_format"]
    if "output_format" in value:
        out["OutputFormat"] = value["output_format"]
    out["Compressed"] = value.get("compressed", False)
    out["NumberOfBuckets"] = value.get("number_of_buckets", 0)
    if "serde_info" in value:
        import capo_glue.types.ser_de_info

        out["SerdeInfo"] = capo_glue.types.ser_de_info.serialize_aws_json_1_1(
            value["serde_info"]
        )
    if "bucket_columns" in value:
        import capo_glue.types.name_string_list

        out["BucketColumns"] = capo_glue.types.name_string_list.serialize_aws_json_1_1(
            value["bucket_columns"]
        )
    if "sort_columns" in value:
        import capo_glue.types.order_list

        out["SortColumns"] = capo_glue.types.order_list.serialize_aws_json_1_1(
            value["sort_columns"]
        )
    if "parameters" in value:
        import capo_glue.types.parameters_map

        out["Parameters"] = capo_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "skewed_info" in value:
        import capo_glue.types.skewed_info

        out["SkewedInfo"] = capo_glue.types.skewed_info.serialize_aws_json_1_1(
            value["skewed_info"]
        )
    out["StoredAsSubDirectories"] = value.get("stored_as_sub_directories", False)
    if "schema_reference" in value:
        import capo_glue.types.schema_reference

        out["SchemaReference"] = (
            capo_glue.types.schema_reference.serialize_aws_json_1_1(
                value["schema_reference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageDescriptor:
    out: StorageDescriptor = {}  # type: ignore[typeddict-item]
    if "Columns" in data:
        import capo_glue.types.column_list

        out["columns"] = capo_glue.types.column_list.deserialize_aws_json_1_1(
            data["Columns"]
        )
    if "Location" in data:
        out["location"] = data["Location"]
    if "AdditionalLocations" in data:
        import capo_glue.types.location_string_list

        out["additional_locations"] = (
            capo_glue.types.location_string_list.deserialize_aws_json_1_1(
                data["AdditionalLocations"]
            )
        )
    if "InputFormat" in data:
        out["input_format"] = data["InputFormat"]
    if "OutputFormat" in data:
        out["output_format"] = data["OutputFormat"]
    if "Compressed" in data:
        out["compressed"] = data["Compressed"]
    else:
        out["compressed"] = False
    if "NumberOfBuckets" in data:
        out["number_of_buckets"] = data["NumberOfBuckets"]
    else:
        out["number_of_buckets"] = 0
    if "SerdeInfo" in data:
        import capo_glue.types.ser_de_info

        out["serde_info"] = capo_glue.types.ser_de_info.deserialize_aws_json_1_1(
            data["SerdeInfo"]
        )
    if "BucketColumns" in data:
        import capo_glue.types.name_string_list

        out["bucket_columns"] = (
            capo_glue.types.name_string_list.deserialize_aws_json_1_1(
                data["BucketColumns"]
            )
        )
    if "SortColumns" in data:
        import capo_glue.types.order_list

        out["sort_columns"] = capo_glue.types.order_list.deserialize_aws_json_1_1(
            data["SortColumns"]
        )
    if "Parameters" in data:
        import capo_glue.types.parameters_map

        out["parameters"] = capo_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "SkewedInfo" in data:
        import capo_glue.types.skewed_info

        out["skewed_info"] = capo_glue.types.skewed_info.deserialize_aws_json_1_1(
            data["SkewedInfo"]
        )
    if "StoredAsSubDirectories" in data:
        out["stored_as_sub_directories"] = data["StoredAsSubDirectories"]
    else:
        out["stored_as_sub_directories"] = False
    if "SchemaReference" in data:
        import capo_glue.types.schema_reference

        out["schema_reference"] = (
            capo_glue.types.schema_reference.deserialize_aws_json_1_1(
                data["SchemaReference"]
            )
        )
    return out
