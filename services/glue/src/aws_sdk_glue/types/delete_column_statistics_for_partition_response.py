"""Generated from Smithy shape ``com.amazonaws.glue#DeleteColumnStatisticsForPartitionResponse``."""

from typing_extensions import TypedDict


class DeleteColumnStatisticsForPartitionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteColumnStatisticsForPartitionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteColumnStatisticsForPartitionResponse:
    out: DeleteColumnStatisticsForPartitionResponse = {}  # type: ignore[typeddict-item]
    return out
