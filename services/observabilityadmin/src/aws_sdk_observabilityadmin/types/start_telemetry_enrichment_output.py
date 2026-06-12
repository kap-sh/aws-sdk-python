"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StartTelemetryEnrichmentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.aws_resource_explorer_managed_view_arn
    import aws_sdk_observabilityadmin.types.telemetry_enrichment_status


class StartTelemetryEnrichmentOutput(TypedDict):
    status: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_enrichment_status.TelemetryEnrichmentStatus"
    ]
    """<p> The status of the resource tags for telemetry feature after the start operation (<code>Running</code>, <code>Stopped</code>, or <code>Impaired</code>). </p>"""
    aws_resource_explorer_managed_view_arn: NotRequired[
        "aws_sdk_observabilityadmin.types.aws_resource_explorer_managed_view_arn.AwsResourceExplorerManagedViewArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the Resource Explorer managed view created for resource tags for telemetry. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTelemetryEnrichmentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_observabilityadmin.types.telemetry_enrichment_status

        out["Status"] = (
            aws_sdk_observabilityadmin.types.telemetry_enrichment_status.serialize_json(
                value["status"]
            )
        )
    if "aws_resource_explorer_managed_view_arn" in value:
        out["AwsResourceExplorerManagedViewArn"] = value[
            "aws_resource_explorer_managed_view_arn"
        ]
    return out


def deserialize_json(data: dict) -> StartTelemetryEnrichmentOutput:
    out: StartTelemetryEnrichmentOutput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_observabilityadmin.types.telemetry_enrichment_status

        out["status"] = (
            aws_sdk_observabilityadmin.types.telemetry_enrichment_status.deserialize_json(
                data["Status"]
            )
        )
    if "AwsResourceExplorerManagedViewArn" in data:
        out["aws_resource_explorer_managed_view_arn"] = data[
            "AwsResourceExplorerManagedViewArn"
        ]
    return out
