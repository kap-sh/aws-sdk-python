"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#StartTelemetryEvaluationForOrganizationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.all_regions
    import aws_sdk_observabilityadmin.types.regions


class StartTelemetryEvaluationForOrganizationInput(TypedDict):
    regions: NotRequired["aws_sdk_observabilityadmin.types.regions.Regions"]
    """<p> An optional list of Amazon Web Services Regions to include in multi-region telemetry evaluation for the organization. The current region is always implicitly included and must not be specified in this list. When provided, telemetry evaluation starts in the current region and propagates to all specified regions for the organization. Mutually exclusive with <code>AllRegions</code>. If neither <code>Regions</code> nor <code>AllRegions</code> is provided, the operation applies only to the current region. </p>"""
    all_regions: NotRequired["aws_sdk_observabilityadmin.types.all_regions.AllRegions"]
    """<p> If set to <code>true</code>, telemetry evaluation for the organization starts in all Amazon Web Services Regions where Amazon CloudWatch Observability Admin is available in the current partition. The current region becomes the home region for managing multi-region evaluation for the organization. When new regions become available, evaluation automatically expands to include them. Mutually exclusive with <code>Regions</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTelemetryEvaluationForOrganizationInput) -> dict:
    out: dict = {}
    if "regions" in value:
        import aws_sdk_observabilityadmin.types.regions

        out["Regions"] = aws_sdk_observabilityadmin.types.regions.serialize_json(
            value["regions"]
        )
    if "all_regions" in value:
        out["AllRegions"] = value["all_regions"]
    return out


def deserialize_json(data: dict) -> StartTelemetryEvaluationForOrganizationInput:
    out: StartTelemetryEvaluationForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "Regions" in data:
        import aws_sdk_observabilityadmin.types.regions

        out["regions"] = aws_sdk_observabilityadmin.types.regions.deserialize_json(
            data["Regions"]
        )
    if "AllRegions" in data:
        out["all_regions"] = data["AllRegions"]
    return out
