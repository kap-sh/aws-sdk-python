"""Generated from Smithy shape ``com.amazonaws.glue#GetPartitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition


class GetPartitionResponse(TypedDict, closed=True):
    partition: NotRequired["aws_sdk_glue.types.partition.Partition"]
    """<p>The requested information, in the form of a <code>Partition</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPartitionResponse) -> dict:
    out: dict = {}
    if "partition" in value:
        import aws_sdk_glue.types.partition

        out["Partition"] = aws_sdk_glue.types.partition.serialize_aws_json_1_1(
            value["partition"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPartitionResponse:
    out: GetPartitionResponse = {}  # type: ignore[typeddict-item]
    if "Partition" in data:
        import aws_sdk_glue.types.partition

        out["partition"] = aws_sdk_glue.types.partition.deserialize_aws_json_1_1(
            data["Partition"]
        )
    return out
