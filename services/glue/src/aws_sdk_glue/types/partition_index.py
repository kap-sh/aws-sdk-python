"""Generated from Smithy shape ``com.amazonaws.glue#PartitionIndex``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.key_list
    import aws_sdk_glue.types.name_string


class PartitionIndex(TypedDict):
    keys: "aws_sdk_glue.types.key_list.KeyList"
    """<p>The keys for the partition index.</p>"""
    index_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the partition index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionIndex) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.key_list

    out["Keys"] = aws_sdk_glue.types.key_list.serialize_aws_json_1_1(value["keys"])
    out["IndexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionIndex:
    out: PartitionIndex = {}  # type: ignore[typeddict-item]
    if "Keys" in data:
        import aws_sdk_glue.types.key_list

        out["keys"] = aws_sdk_glue.types.key_list.deserialize_aws_json_1_1(data["Keys"])
    else:
        raise DeserializationError("PartitionIndex.keys required")
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("PartitionIndex.index_name required")
    return out
