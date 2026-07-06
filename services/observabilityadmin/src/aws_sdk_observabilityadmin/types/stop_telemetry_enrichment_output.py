"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StopTelemetryEnrichmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_enrichment_status


class StopTelemetryEnrichmentOutput(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_enrichment_status.TelemetryEnrichmentStatus"
    ]
    """<p> The status of the resource tags for telemetry feature after the stop operation (<code>Running</code>, <code>Stopped</code>, or <code>Impaired</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopTelemetryEnrichmentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_observabilityadmin.types.telemetry_enrichment_status

        out["Status"] = (
            aws_sdk_observabilityadmin.types.telemetry_enrichment_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> StopTelemetryEnrichmentOutput:
    out: StopTelemetryEnrichmentOutput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_observabilityadmin.types.telemetry_enrichment_status

        out["status"] = (
            aws_sdk_observabilityadmin.types.telemetry_enrichment_status.deserialize_json(
                data["Status"]
            )
        )
    return out
