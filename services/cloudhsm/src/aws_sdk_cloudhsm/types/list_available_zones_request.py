"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ListAvailableZonesRequest``."""

from typing_extensions import TypedDict


class ListAvailableZonesRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableZonesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableZonesRequest:
    out: ListAvailableZonesRequest = {}  # type: ignore[typeddict-item]
    return out
