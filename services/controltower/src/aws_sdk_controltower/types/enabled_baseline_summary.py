"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.enabled_baseline_drift_status_summary
    import aws_sdk_controltower.types.enablement_status_summary


class EnabledBaselineSummary(TypedDict, closed=True):
    arn: "aws_sdk_controltower.types.arn.Arn"
    """<p>The ARN of the <code>EnabledBaseline</code> resource</p>"""
    baseline_identifier: "str"
    """<p>The specific baseline that is enabled as part of the <code>EnabledBaseline</code> resource.</p>"""
    baseline_version: NotRequired["str"]
    """<p>The enabled version of the baseline.</p>"""
    drift_status_summary: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_drift_status_summary.EnabledBaselineDriftStatusSummary"
    ]
    """<p>The drift status of the enabled baseline.</p>"""
    target_identifier: "str"
    """<p>The target upon which the baseline is enabled.</p>"""
    parent_identifier: NotRequired["aws_sdk_controltower.types.arn.Arn"]
    """<p>An ARN that represents an object returned by <code>ListEnabledBaseline</code>, to describe an enabled baseline.</p>"""
    status_summary: (
        "aws_sdk_controltower.types.enablement_status_summary.EnablementStatusSummary"
    )


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["baselineIdentifier"] = value["baseline_identifier"]
    if "baseline_version" in value:
        out["baselineVersion"] = value["baseline_version"]
    if "drift_status_summary" in value:
        import aws_sdk_controltower.types.enabled_baseline_drift_status_summary

        out["driftStatusSummary"] = (
            aws_sdk_controltower.types.enabled_baseline_drift_status_summary.serialize_json(
                value["drift_status_summary"]
            )
        )
    out["targetIdentifier"] = value["target_identifier"]
    if "parent_identifier" in value:
        out["parentIdentifier"] = value["parent_identifier"]
    import aws_sdk_controltower.types.enablement_status_summary

    out["statusSummary"] = (
        aws_sdk_controltower.types.enablement_status_summary.serialize_json(
            value["status_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> EnabledBaselineSummary:
    out: EnabledBaselineSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EnabledBaselineSummary.arn required")
    if "baselineIdentifier" in data:
        out["baseline_identifier"] = data["baselineIdentifier"]
    else:
        raise DeserializationError(
            "EnabledBaselineSummary.baseline_identifier required"
        )
    if "baselineVersion" in data:
        out["baseline_version"] = data["baselineVersion"]
    if "driftStatusSummary" in data:
        import aws_sdk_controltower.types.enabled_baseline_drift_status_summary

        out["drift_status_summary"] = (
            aws_sdk_controltower.types.enabled_baseline_drift_status_summary.deserialize_json(
                data["driftStatusSummary"]
            )
        )
    if "targetIdentifier" in data:
        out["target_identifier"] = data["targetIdentifier"]
    else:
        raise DeserializationError("EnabledBaselineSummary.target_identifier required")
    if "parentIdentifier" in data:
        out["parent_identifier"] = data["parentIdentifier"]
    if "statusSummary" in data:
        import aws_sdk_controltower.types.enablement_status_summary

        out["status_summary"] = (
            aws_sdk_controltower.types.enablement_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    else:
        raise DeserializationError("EnabledBaselineSummary.status_summary required")
    return out
