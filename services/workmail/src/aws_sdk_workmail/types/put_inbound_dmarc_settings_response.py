"""Generated from Smithy shape ``com.amazonaws.workmail#PutInboundDmarcSettingsResponse``."""

from typing_extensions import TypedDict


class PutInboundDmarcSettingsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInboundDmarcSettingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInboundDmarcSettingsResponse:
    out: PutInboundDmarcSettingsResponse = {}  # type: ignore[typeddict-item]
    return out
