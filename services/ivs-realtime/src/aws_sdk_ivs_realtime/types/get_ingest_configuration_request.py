"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetIngestConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.ingest_configuration_arn


class GetIngestConfigurationRequest(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>ARN of the ingest for which the information is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIngestConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetIngestConfigurationRequest:
    out: GetIngestConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetIngestConfigurationRequest.arn required")
    return out
