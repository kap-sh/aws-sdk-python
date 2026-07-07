"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StopEventDataStoreIngestionResponse``."""

from typing_extensions import TypedDict


class StopEventDataStoreIngestionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEventDataStoreIngestionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEventDataStoreIngestionResponse:
    out: StopEventDataStoreIngestionResponse = {}  # type: ignore[typeddict-item]
    return out
