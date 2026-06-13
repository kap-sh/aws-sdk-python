"""Generated from Smithy shape ``com.amazonaws.inspector2#CisCheckAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.cis_scan_arn
    import aws_sdk_inspector2.types.cis_security_level
    import aws_sdk_inspector2.types.status_counts


class CisCheckAggregation(TypedDict):
    scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN for the CIS check scan ARN.</p>"""
    check_id: NotRequired["str"]
    """<p>The check ID for the CIS check.</p>"""
    title: NotRequired["str"]
    """<p>The CIS check title.</p>"""
    check_description: NotRequired["str"]
    """<p>The description for the CIS check.</p>"""
    level: NotRequired["aws_sdk_inspector2.types.cis_security_level.CisSecurityLevel"]
    """<p>The CIS check level.</p>"""
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The account ID for the CIS check.</p>"""
    status_counts: NotRequired["aws_sdk_inspector2.types.status_counts.StatusCounts"]
    """<p>The CIS check status counts.</p>"""
    platform: NotRequired["str"]
    """<p>The CIS check platform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisCheckAggregation) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "check_id" in value:
        out["checkId"] = value["check_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "check_description" in value:
        out["checkDescription"] = value["check_description"]
    if "level" in value:
        import aws_sdk_inspector2.types.cis_security_level

        out["level"] = aws_sdk_inspector2.types.cis_security_level.serialize_json(
            value["level"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status_counts" in value:
        import aws_sdk_inspector2.types.status_counts

        out["statusCounts"] = aws_sdk_inspector2.types.status_counts.serialize_json(
            value["status_counts"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> CisCheckAggregation:
    out: CisCheckAggregation = {}  # type: ignore[typeddict-item]
    if "scanArn" in data:
        out["scan_arn"] = data["scanArn"]
    else:
        raise DeserializationError("CisCheckAggregation.scan_arn required")
    if "checkId" in data:
        out["check_id"] = data["checkId"]
    if "title" in data:
        out["title"] = data["title"]
    if "checkDescription" in data:
        out["check_description"] = data["checkDescription"]
    if "level" in data:
        import aws_sdk_inspector2.types.cis_security_level

        out["level"] = aws_sdk_inspector2.types.cis_security_level.deserialize_json(
            data["level"]
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "statusCounts" in data:
        import aws_sdk_inspector2.types.status_counts

        out["status_counts"] = aws_sdk_inspector2.types.status_counts.deserialize_json(
            data["statusCounts"]
        )
    if "platform" in data:
        out["platform"] = data["platform"]
    return out
