"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.enabled_baseline_drift_status_summary
    import aws_sdk_controltower.types.enabled_baseline_parameter_summaries
    import aws_sdk_controltower.types.enablement_status_summary


class EnabledBaselineDetails(TypedDict):
    arn: "aws_sdk_controltower.types.arn.Arn"
    """<p>The ARN of the <code>EnabledBaseline</code> resource.</p>"""
    baseline_identifier: "str"
    """<p>The specific <code>Baseline</code> enabled as part of the <code>EnabledBaseline</code> resource.</p>"""
    baseline_version: NotRequired["str"]
    """<p>The enabled version of the <code>Baseline</code>.</p>"""
    drift_status_summary: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_drift_status_summary.EnabledBaselineDriftStatusSummary"
    ]
    """<p>The drift status of the enabled baseline.</p>"""
    target_identifier: "str"
    """<p>The target on which to enable the <code>Baseline</code>.</p>"""
    parent_identifier: NotRequired["aws_sdk_controltower.types.arn.Arn"]
    """<p>An ARN that represents the parent <code>EnabledBaseline</code> at the Organizational Unit (OU) level, from which the child <code>EnabledBaseline</code> inherits its configuration. The value is returned by <code>GetEnabledBaseline</code>.</p>"""
    status_summary: (
        "aws_sdk_controltower.types.enablement_status_summary.EnablementStatusSummary"
    )
    parameters: NotRequired[
        "aws_sdk_controltower.types.enabled_baseline_parameter_summaries.EnabledBaselineParameterSummaries"
    ]
    """<p>Shows the parameters that are applied when enabling this <code>Baseline</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDetails) -> dict:
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
    if "parameters" in value:
        import aws_sdk_controltower.types.enabled_baseline_parameter_summaries

        out["parameters"] = (
            aws_sdk_controltower.types.enabled_baseline_parameter_summaries.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineDetails:
    out: EnabledBaselineDetails = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EnabledBaselineDetails.arn required")
    if "baselineIdentifier" in data:
        out["baseline_identifier"] = data["baselineIdentifier"]
    else:
        raise DeserializationError(
            "EnabledBaselineDetails.baseline_identifier required"
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
        raise DeserializationError("EnabledBaselineDetails.target_identifier required")
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
        raise DeserializationError("EnabledBaselineDetails.status_summary required")
    if "parameters" in data:
        import aws_sdk_controltower.types.enabled_baseline_parameter_summaries

        out["parameters"] = (
            aws_sdk_controltower.types.enabled_baseline_parameter_summaries.deserialize_json(
                data["parameters"]
            )
        )
    return out
