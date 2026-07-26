"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#UpdateIngestConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_arn
    import capo_ivs_realtime.types.ingest_configuration_stage_arn
    import capo_ivs_realtime.types.redundant_ingest


class UpdateIngestConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>ARN of the IngestConfiguration, for which the related stage ARN needs to be updated.</p>"""
    stage_arn: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_stage_arn.IngestConfigurationStageArn"
    ]
    """<p>Stage ARN that needs to be updated.</p>"""
    redundant_ingest: "capo_ivs_realtime.types.redundant_ingest.RedundantIngest"
    """<p>Indicates whether redundant ingest is enabled for the ingest configuration. Default: <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIngestConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "stage_arn" in value:
        out["stageArn"] = value["stage_arn"]
    out["redundantIngest"] = value.get("redundant_ingest", False)
    return out


def deserialize_json(data: dict) -> UpdateIngestConfigurationRequest:
    out: UpdateIngestConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateIngestConfigurationRequest.arn required")
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    if "redundantIngest" in data:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    return out
