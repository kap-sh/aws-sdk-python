"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FindingSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.entity_description
    import aws_sdk_resiliencehubv2.types.failure_category
    import aws_sdk_resiliencehubv2.types.finding_severity
    import aws_sdk_resiliencehubv2.types.finding_status
    import aws_sdk_resiliencehubv2.types.policy_component
    import aws_sdk_resiliencehubv2.types.uuid


class FindingSummary(TypedDict):
    service_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    finding_id: NotRequired["aws_sdk_resiliencehubv2.types.uuid.Uuid"]
    """<p>The unique identifier of the finding.</p>"""
    name: NotRequired["str"]
    """<p>The name of the finding.</p>"""
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    failure_category: NotRequired[
        "aws_sdk_resiliencehubv2.types.failure_category.FailureCategory"
    ]
    """<p>The failure category of the finding.</p>"""
    severity: NotRequired[
        "aws_sdk_resiliencehubv2.types.finding_severity.FindingSeverity"
    ]
    """<p>The severity of the finding.</p>"""
    status: NotRequired["aws_sdk_resiliencehubv2.types.finding_status.FindingStatus"]
    """<p>The current status of the finding.</p>"""
    policy_component: NotRequired[
        "aws_sdk_resiliencehubv2.types.policy_component.PolicyComponent"
    ]
    """<p>The policy component associated with the finding.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the finding was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummary) -> dict:
    out: dict = {}
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "failure_category" in value:
        import aws_sdk_resiliencehubv2.types.failure_category

        out["failureCategory"] = (
            aws_sdk_resiliencehubv2.types.failure_category.serialize_json(
                value["failure_category"]
            )
        )
    if "severity" in value:
        import aws_sdk_resiliencehubv2.types.finding_severity

        out["severity"] = aws_sdk_resiliencehubv2.types.finding_severity.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import aws_sdk_resiliencehubv2.types.finding_status

        out["status"] = aws_sdk_resiliencehubv2.types.finding_status.serialize_json(
            value["status"]
        )
    if "policy_component" in value:
        import aws_sdk_resiliencehubv2.types.policy_component

        out["policyComponent"] = (
            aws_sdk_resiliencehubv2.types.policy_component.serialize_json(
                value["policy_component"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingSummary:
    out: FindingSummary = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "failureCategory" in data:
        import aws_sdk_resiliencehubv2.types.failure_category

        out["failure_category"] = (
            aws_sdk_resiliencehubv2.types.failure_category.deserialize_json(
                data["failureCategory"]
            )
        )
    if "severity" in data:
        import aws_sdk_resiliencehubv2.types.finding_severity

        out["severity"] = (
            aws_sdk_resiliencehubv2.types.finding_severity.deserialize_json(
                data["severity"]
            )
        )
    if "status" in data:
        import aws_sdk_resiliencehubv2.types.finding_status

        out["status"] = aws_sdk_resiliencehubv2.types.finding_status.deserialize_json(
            data["status"]
        )
    if "policyComponent" in data:
        import aws_sdk_resiliencehubv2.types.policy_component

        out["policy_component"] = (
            aws_sdk_resiliencehubv2.types.policy_component.deserialize_json(
                data["policyComponent"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
