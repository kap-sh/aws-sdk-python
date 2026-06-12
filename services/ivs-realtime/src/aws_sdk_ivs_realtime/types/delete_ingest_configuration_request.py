"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DeleteIngestConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.boolean
    import aws_sdk_ivs_realtime.types.ingest_configuration_arn


class DeleteIngestConfigurationRequest(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>ARN of the IngestConfiguration.</p>"""
    force: "aws_sdk_ivs_realtime.types.boolean.Boolean"
    """<p>Optional field to force deletion of the IngestConfiguration. If this is set to <code>true</code> when a participant is actively publishing, the participant is disconnected from the stage, followed by deletion of the IngestConfiguration. Default: <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIngestConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["force"] = value.get("force", False)
    return out


def deserialize_json(data: dict) -> DeleteIngestConfigurationRequest:
    out: DeleteIngestConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteIngestConfigurationRequest.arn required")
    if "force" in data:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
