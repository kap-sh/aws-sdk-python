"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.landing_zone_drift_status_summary
    import aws_sdk_controltower.types.landing_zone_status
    import aws_sdk_controltower.types.landing_zone_version
    import aws_sdk_controltower.types.manifest
    import aws_sdk_controltower.types.remediation_types


class LandingZoneDetail(TypedDict, closed=True):
    version: "aws_sdk_controltower.types.landing_zone_version.LandingZoneVersion"
    """<p>The landing zone's current deployed version.</p>"""
    remediation_types: NotRequired[
        "aws_sdk_controltower.types.remediation_types.RemediationTypes"
    ]
    """<p>The types of remediation actions configured for the landing zone, such as automatic drift correction or compliance enforcement.</p>"""
    arn: NotRequired["aws_sdk_controltower.types.arn.Arn"]
    """<p>The ARN of the landing zone.</p>"""
    status: NotRequired[
        "aws_sdk_controltower.types.landing_zone_status.LandingZoneStatus"
    ]
    """<p>The landing zone deployment status. One of <code>ACTIVE</code>, <code>PROCESSING</code>, <code>FAILED</code>.</p>"""
    latest_available_version: NotRequired[
        "aws_sdk_controltower.types.landing_zone_version.LandingZoneVersion"
    ]
    """<p>The latest available version of the landing zone.</p>"""
    drift_status: NotRequired[
        "aws_sdk_controltower.types.landing_zone_drift_status_summary.LandingZoneDriftStatusSummary"
    ]
    """<p>The drift status of the landing zone.</p>"""
    manifest: "aws_sdk_controltower.types.manifest.Manifest"
    """<p>The landing zone manifest JSON text file that specifies the landing zone configurations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneDetail) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "remediation_types" in value:
        import aws_sdk_controltower.types.remediation_types

        out["remediationTypes"] = (
            aws_sdk_controltower.types.remediation_types.serialize_json(
                value["remediation_types"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_controltower.types.landing_zone_status

        out["status"] = aws_sdk_controltower.types.landing_zone_status.serialize_json(
            value["status"]
        )
    if "latest_available_version" in value:
        out["latestAvailableVersion"] = value["latest_available_version"]
    if "drift_status" in value:
        import aws_sdk_controltower.types.landing_zone_drift_status_summary

        out["driftStatus"] = (
            aws_sdk_controltower.types.landing_zone_drift_status_summary.serialize_json(
                value["drift_status"]
            )
        )
    out["manifest"] = value["manifest"]
    return out


def deserialize_json(data: dict) -> LandingZoneDetail:
    out: LandingZoneDetail = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("LandingZoneDetail.version required")
    if "remediationTypes" in data:
        import aws_sdk_controltower.types.remediation_types

        out["remediation_types"] = (
            aws_sdk_controltower.types.remediation_types.deserialize_json(
                data["remediationTypes"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import aws_sdk_controltower.types.landing_zone_status

        out["status"] = aws_sdk_controltower.types.landing_zone_status.deserialize_json(
            data["status"]
        )
    if "latestAvailableVersion" in data:
        out["latest_available_version"] = data["latestAvailableVersion"]
    if "driftStatus" in data:
        import aws_sdk_controltower.types.landing_zone_drift_status_summary

        out["drift_status"] = (
            aws_sdk_controltower.types.landing_zone_drift_status_summary.deserialize_json(
                data["driftStatus"]
            )
        )
    if "manifest" in data:
        out["manifest"] = data["manifest"]
    else:
        raise DeserializationError("LandingZoneDetail.manifest required")
    return out
