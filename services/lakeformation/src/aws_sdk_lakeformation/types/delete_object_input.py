"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteObjectInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.e_tag_string
    import aws_sdk_lakeformation.types.partition_values_list
    import aws_sdk_lakeformation.types.uri


class DeleteObjectInput(TypedDict):
    uri: "aws_sdk_lakeformation.types.uri.URI"
    """<p>The Amazon S3 location of the object to delete.</p>"""
    e_tag: NotRequired["aws_sdk_lakeformation.types.e_tag_string.ETagString"]
    """<p>The Amazon S3 ETag of the object. Returned by <code>GetTableObjects</code> for validation and used to identify changes to the underlying data.</p>"""
    partition_values: NotRequired[
        "aws_sdk_lakeformation.types.partition_values_list.PartitionValuesList"
    ]
    """<p>A list of partition values for the object. A value must be specified for each partition key associated with the governed table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteObjectInput) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "partition_values" in value:
        import aws_sdk_lakeformation.types.partition_values_list

        out["PartitionValues"] = (
            aws_sdk_lakeformation.types.partition_values_list.serialize_json(
                value["partition_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteObjectInput:
    out: DeleteObjectInput = {}  # type: ignore[typeddict-item]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    else:
        raise DeserializationError("DeleteObjectInput.uri required")
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "PartitionValues" in data:
        import aws_sdk_lakeformation.types.partition_values_list

        out["partition_values"] = (
            aws_sdk_lakeformation.types.partition_values_list.deserialize_json(
                data["PartitionValues"]
            )
        )
    return out
