"""Generated from Smithy shape ``com.amazonaws.lakeformation#AddObjectInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.e_tag_string
    import aws_sdk_lakeformation.types.object_size
    import aws_sdk_lakeformation.types.partition_values_list
    import aws_sdk_lakeformation.types.uri


class AddObjectInput(TypedDict):
    uri: "aws_sdk_lakeformation.types.uri.URI"
    """<p>The Amazon S3 location of the object.</p>"""
    e_tag: "aws_sdk_lakeformation.types.e_tag_string.ETagString"
    """<p>The Amazon S3 ETag of the object. Returned by <code>GetTableObjects</code> for validation and used to identify changes to the underlying data.</p>"""
    size: "aws_sdk_lakeformation.types.object_size.ObjectSize"
    """<p>The size of the Amazon S3 object in bytes.</p>"""
    partition_values: NotRequired[
        "aws_sdk_lakeformation.types.partition_values_list.PartitionValuesList"
    ]
    """<p>A list of partition values for the object. A value must be specified for each partition key associated with the table.</p> <p>The supported data types are integer, long, date(yyyy-MM-dd), timestamp(yyyy-MM-dd HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss\"), string and decimal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddObjectInput) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    out["ETag"] = value["e_tag"]
    out["Size"] = value.get("size", 0)
    if "partition_values" in value:
        import aws_sdk_lakeformation.types.partition_values_list

        out["PartitionValues"] = (
            aws_sdk_lakeformation.types.partition_values_list.serialize_json(
                value["partition_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddObjectInput:
    out: AddObjectInput = {}  # type: ignore[typeddict-item]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    else:
        raise DeserializationError("AddObjectInput.uri required")
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    else:
        raise DeserializationError("AddObjectInput.e_tag required")
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if "PartitionValues" in data:
        import aws_sdk_lakeformation.types.partition_values_list

        out["partition_values"] = (
            aws_sdk_lakeformation.types.partition_values_list.deserialize_json(
                data["PartitionValues"]
            )
        )
    return out
