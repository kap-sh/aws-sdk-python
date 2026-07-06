"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_inspector2.types.cis_scan_arn
    import aws_sdk_inspector2.types.cis_scan_configuration_arn
    import aws_sdk_inspector2.types.cis_scan_name
    import aws_sdk_inspector2.types.cis_scan_status
    import aws_sdk_inspector2.types.cis_security_level
    import aws_sdk_inspector2.types.cis_targets


class CisScan(TypedDict, closed=True):
    scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The CIS scan's ARN.</p>"""
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    )
    """<p>The CIS scan's configuration ARN.</p>"""
    status: NotRequired["aws_sdk_inspector2.types.cis_scan_status.CisScanStatus"]
    """<p>The CIS scan's status.</p>"""
    scan_name: NotRequired["aws_sdk_inspector2.types.cis_scan_name.CisScanName"]
    """<p>The the name of the scan configuration that's associated with this scan.</p>"""
    scan_date: NotRequired["datetime.datetime"]
    """<p>The CIS scan's date.</p>"""
    failed_checks: NotRequired["int"]
    """<p>The CIS scan's failed checks.</p>"""
    total_checks: NotRequired["int"]
    """<p>The CIS scan's total checks.</p>"""
    targets: NotRequired["aws_sdk_inspector2.types.cis_targets.CisTargets"]
    """<p>The CIS scan's targets.</p>"""
    scheduled_by: NotRequired["str"]
    """<p>The account or organization that schedules the CIS scan.</p>"""
    security_level: NotRequired[
        "aws_sdk_inspector2.types.cis_security_level.CisSecurityLevel"
    ]
    """<p> The security level for the CIS scan. Security level refers to the Benchmark levels that CIS assigns to a profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisScan) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    if "status" in value:
        import aws_sdk_inspector2.types.cis_scan_status

        out["status"] = aws_sdk_inspector2.types.cis_scan_status.serialize_json(
            value["status"]
        )
    if "scan_name" in value:
        out["scanName"] = value["scan_name"]
    if "scan_date" in value:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["scanDate"] = aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
            value["scan_date"]
        )
    if "failed_checks" in value:
        out["failedChecks"] = value["failed_checks"]
    if "total_checks" in value:
        out["totalChecks"] = value["total_checks"]
    if "targets" in value:
        import aws_sdk_inspector2.types.cis_targets

        out["targets"] = aws_sdk_inspector2.types.cis_targets.serialize_json(
            value["targets"]
        )
    if "scheduled_by" in value:
        out["scheduledBy"] = value["scheduled_by"]
    if "security_level" in value:
        import aws_sdk_inspector2.types.cis_security_level

        out["securityLevel"] = (
            aws_sdk_inspector2.types.cis_security_level.serialize_json(
                value["security_level"]
            )
        )
    return out


def deserialize_json(data: dict) -> CisScan:
    out: CisScan = {}  # type: ignore[typeddict-item]
    if "scanArn" in data:
        out["scan_arn"] = data["scanArn"]
    else:
        raise DeserializationError("CisScan.scan_arn required")
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError("CisScan.scan_configuration_arn required")
    if "status" in data:
        import aws_sdk_inspector2.types.cis_scan_status

        out["status"] = aws_sdk_inspector2.types.cis_scan_status.deserialize_json(
            data["status"]
        )
    if "scanName" in data:
        out["scan_name"] = data["scanName"]
    if "scanDate" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["scan_date"] = aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
            data["scanDate"]
        )
    if "failedChecks" in data:
        out["failed_checks"] = data["failedChecks"]
    if "totalChecks" in data:
        out["total_checks"] = data["totalChecks"]
    if "targets" in data:
        import aws_sdk_inspector2.types.cis_targets

        out["targets"] = aws_sdk_inspector2.types.cis_targets.deserialize_json(
            data["targets"]
        )
    if "scheduledBy" in data:
        out["scheduled_by"] = data["scheduledBy"]
    if "securityLevel" in data:
        import aws_sdk_inspector2.types.cis_security_level

        out["security_level"] = (
            aws_sdk_inspector2.types.cis_security_level.deserialize_json(
                data["securityLevel"]
            )
        )
    return out
