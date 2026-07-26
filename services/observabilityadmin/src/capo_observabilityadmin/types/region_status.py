"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#RegionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.region
    import capo_observabilityadmin.types.resource_arn


class RegionStatus(TypedDict, closed=True):
    region: NotRequired["capo_observabilityadmin.types.region.Region"]
    """<p> The Amazon Web Services Region code (for example, <code>eu-west-1</code> or <code>us-west-2</code>) that this status applies to. </p>"""
    status: NotRequired["str"]
    """<p> The status of the operation in this region. For telemetry evaluation, valid values include <code>STARTING</code>, <code>RUNNING</code>, and <code>FAILED_START</code>. For telemetry rules, valid values include <code>PENDING</code>, <code>ACTIVE</code>, and <code>FAILED</code>. </p>"""
    failure_reason: NotRequired["str"]
    """<p> The reason for a failure status in this region. This field is only populated when <code>Status</code> indicates a failure. </p>"""
    rule_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the telemetry rule in this spoke region. This field is only present for telemetry rule region statuses and is populated when the rule has been successfully created in the spoke region (status is <code>ACTIVE</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionStatus) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "status" in value:
        out["Status"] = value["status"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> RegionStatus:
    out: RegionStatus = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
