"""Generated from Smithy shape ``com.amazonaws.glue#GetPartitionIndexesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition_index_descriptor_list
    import aws_sdk_glue.types.token


class GetPartitionIndexesResponse(TypedDict, closed=True):
    partition_index_descriptor_list: NotRequired[
        "aws_sdk_glue.types.partition_index_descriptor_list.PartitionIndexDescriptorList"
    ]
    """<p>A list of index descriptors.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, present if the current list segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPartitionIndexesResponse) -> dict:
    out: dict = {}
    if "partition_index_descriptor_list" in value:
        import aws_sdk_glue.types.partition_index_descriptor_list

        out["PartitionIndexDescriptorList"] = (
            aws_sdk_glue.types.partition_index_descriptor_list.serialize_aws_json_1_1(
                value["partition_index_descriptor_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPartitionIndexesResponse:
    out: GetPartitionIndexesResponse = {}  # type: ignore[typeddict-item]
    if "PartitionIndexDescriptorList" in data:
        import aws_sdk_glue.types.partition_index_descriptor_list

        out["partition_index_descriptor_list"] = (
            aws_sdk_glue.types.partition_index_descriptor_list.deserialize_aws_json_1_1(
                data["PartitionIndexDescriptorList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
