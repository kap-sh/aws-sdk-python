"""Generated from Smithy shape ``com.amazonaws.glue#GetUnfilteredPartitionsMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.token
    import aws_sdk_glue.types.unfiltered_partition_list


class GetUnfilteredPartitionsMetadataResponse(TypedDict, closed=True):
    unfiltered_partitions: NotRequired[
        "aws_sdk_glue.types.unfiltered_partition_list.UnfilteredPartitionList"
    ]
    """<p>A list of requested partitions.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if the returned list of partitions does not include the last one.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUnfilteredPartitionsMetadataResponse) -> dict:
    out: dict = {}
    if "unfiltered_partitions" in value:
        import aws_sdk_glue.types.unfiltered_partition_list

        out["UnfilteredPartitions"] = (
            aws_sdk_glue.types.unfiltered_partition_list.serialize_aws_json_1_1(
                value["unfiltered_partitions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUnfilteredPartitionsMetadataResponse:
    out: GetUnfilteredPartitionsMetadataResponse = {}  # type: ignore[typeddict-item]
    if "UnfilteredPartitions" in data:
        import aws_sdk_glue.types.unfiltered_partition_list

        out["unfiltered_partitions"] = (
            aws_sdk_glue.types.unfiltered_partition_list.deserialize_aws_json_1_1(
                data["UnfilteredPartitions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
