"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetTelemetryEvaluationStatusForOrganizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.failure_reason
    import aws_sdk_observabilityadmin.types.region
    import aws_sdk_observabilityadmin.types.region_statuses
    import aws_sdk_observabilityadmin.types.status


class GetTelemetryEvaluationStatusForOrganizationOutput(TypedDict, closed=True):
    status: NotRequired["aws_sdk_observabilityadmin.types.status.Status"]
    """<p> The onboarding status of the telemetry config feature for the organization. </p>"""
    failure_reason: NotRequired[
        "aws_sdk_observabilityadmin.types.failure_reason.FailureReason"
    ]
    """<p> This field describes the reason for the failure status. The field will only be populated if <code>Status</code> is <code>FAILED_START</code> or <code>FAILED_STOP</code>. </p>"""
    home_region: NotRequired["aws_sdk_observabilityadmin.types.region.Region"]
    """<p> The Amazon Web Services Region that is designated as the home region for multi-region telemetry evaluation for the organization. The home region is the single management point for all multi-region operations on this organization. This field is only present when multi-region telemetry evaluation is active. </p>"""
    region_statuses: NotRequired[
        "aws_sdk_observabilityadmin.types.region_statuses.RegionStatuses"
    ]
    """<p> A list of per-region telemetry evaluation statuses for the organization. Each entry indicates the evaluation status for a specific spoke region included in the multi-region configuration. This field is only present when multi-region telemetry evaluation is active. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTelemetryEvaluationStatusForOrganizationOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_observabilityadmin.types.status

        out["Status"] = aws_sdk_observabilityadmin.types.status.serialize_json(
            value["status"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "region_statuses" in value:
        import aws_sdk_observabilityadmin.types.region_statuses

        out["RegionStatuses"] = (
            aws_sdk_observabilityadmin.types.region_statuses.serialize_json(
                value["region_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTelemetryEvaluationStatusForOrganizationOutput:
    out: GetTelemetryEvaluationStatusForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_observabilityadmin.types.status

        out["status"] = aws_sdk_observabilityadmin.types.status.deserialize_json(
            data["Status"]
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    if "RegionStatuses" in data:
        import aws_sdk_observabilityadmin.types.region_statuses

        out["region_statuses"] = (
            aws_sdk_observabilityadmin.types.region_statuses.deserialize_json(
                data["RegionStatuses"]
            )
        )
    return out
