"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetResourceAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.cis_scan_arn
    import aws_sdk_inspector2.types.cis_target_status
    import aws_sdk_inspector2.types.cis_target_status_reason
    import aws_sdk_inspector2.types.resource_id
    import aws_sdk_inspector2.types.status_counts
    import aws_sdk_inspector2.types.target_resource_tags


class CisTargetResourceAggregation(TypedDict):
    scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN for the CIS target resource.</p>"""
    target_resource_id: NotRequired["aws_sdk_inspector2.types.resource_id.ResourceId"]
    """<p>The ID of the target resource.</p>"""
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The account ID for the CIS target resource.</p>"""
    target_resource_tags: NotRequired[
        "aws_sdk_inspector2.types.target_resource_tags.TargetResourceTags"
    ]
    """<p>The tag for the target resource.</p>"""
    status_counts: NotRequired["aws_sdk_inspector2.types.status_counts.StatusCounts"]
    """<p>The target resource status counts.</p>"""
    platform: NotRequired["str"]
    """<p>The platform for the CIS target resource.</p>"""
    target_status: NotRequired[
        "aws_sdk_inspector2.types.cis_target_status.CisTargetStatus"
    ]
    """<p>The status of the target resource.</p>"""
    target_status_reason: NotRequired[
        "aws_sdk_inspector2.types.cis_target_status_reason.CisTargetStatusReason"
    ]
    """<p>The reason for the target resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetResourceAggregation) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "target_resource_id" in value:
        out["targetResourceId"] = value["target_resource_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "target_resource_tags" in value:
        import aws_sdk_inspector2.types.target_resource_tags

        out["targetResourceTags"] = (
            aws_sdk_inspector2.types.target_resource_tags.serialize_json(
                value["target_resource_tags"]
            )
        )
    if "status_counts" in value:
        import aws_sdk_inspector2.types.status_counts

        out["statusCounts"] = aws_sdk_inspector2.types.status_counts.serialize_json(
            value["status_counts"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "target_status" in value:
        import aws_sdk_inspector2.types.cis_target_status

        out["targetStatus"] = aws_sdk_inspector2.types.cis_target_status.serialize_json(
            value["target_status"]
        )
    if "target_status_reason" in value:
        import aws_sdk_inspector2.types.cis_target_status_reason

        out["targetStatusReason"] = (
            aws_sdk_inspector2.types.cis_target_status_reason.serialize_json(
                value["target_status_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisTargetResourceAggregation:
    out: CisTargetResourceAggregation = {}  # type: ignore[typeddict-item]
    if "scanArn" in data:
        out["scan_arn"] = data["scanArn"]
    else:
        raise DeserializationError("CisTargetResourceAggregation.scan_arn required")
    if "targetResourceId" in data:
        out["target_resource_id"] = data["targetResourceId"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "targetResourceTags" in data:
        import aws_sdk_inspector2.types.target_resource_tags

        out["target_resource_tags"] = (
            aws_sdk_inspector2.types.target_resource_tags.deserialize_json(
                data["targetResourceTags"]
            )
        )
    if "statusCounts" in data:
        import aws_sdk_inspector2.types.status_counts

        out["status_counts"] = aws_sdk_inspector2.types.status_counts.deserialize_json(
            data["statusCounts"]
        )
    if "platform" in data:
        out["platform"] = data["platform"]
    if "targetStatus" in data:
        import aws_sdk_inspector2.types.cis_target_status

        out["target_status"] = (
            aws_sdk_inspector2.types.cis_target_status.deserialize_json(
                data["targetStatus"]
            )
        )
    if "targetStatusReason" in data:
        import aws_sdk_inspector2.types.cis_target_status_reason

        out["target_status_reason"] = (
            aws_sdk_inspector2.types.cis_target_status_reason.deserialize_json(
                data["targetStatusReason"]
            )
        )
    return out
