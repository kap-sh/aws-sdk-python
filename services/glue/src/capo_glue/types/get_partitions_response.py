"""Generated from Smithy shape ``com.amazonaws.glue#GetPartitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.partition_list
    import capo_glue.types.token


class GetPartitionsResponse(TypedDict, closed=True):
    partitions: NotRequired["capo_glue.types.partition_list.PartitionList"]
    """<p>A list of requested partitions.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if the returned list of partitions does not include the last one.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPartitionsResponse) -> dict:
    out: dict = {}
    if "partitions" in value:
        import capo_glue.types.partition_list

        out["Partitions"] = capo_glue.types.partition_list.serialize_aws_json_1_1(
            value["partitions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPartitionsResponse:
    out: GetPartitionsResponse = {}  # type: ignore[typeddict-item]
    if "Partitions" in data:
        import capo_glue.types.partition_list

        out["partitions"] = capo_glue.types.partition_list.deserialize_aws_json_1_1(
            data["Partitions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
