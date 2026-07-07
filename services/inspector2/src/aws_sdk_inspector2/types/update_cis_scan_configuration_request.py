"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCisScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_configuration_arn
    import aws_sdk_inspector2.types.cis_scan_name
    import aws_sdk_inspector2.types.cis_security_level
    import aws_sdk_inspector2.types.schedule
    import aws_sdk_inspector2.types.update_cis_targets


class UpdateCisScanConfigurationRequest(TypedDict, closed=True):
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    )
    """<p>The CIS scan configuration ARN.</p>"""
    scan_name: NotRequired["aws_sdk_inspector2.types.cis_scan_name.CisScanName"]
    """<p>The scan name for the CIS scan configuration.</p>"""
    security_level: NotRequired[
        "aws_sdk_inspector2.types.cis_security_level.CisSecurityLevel"
    ]
    """<p> The security level for the CIS scan configuration. Security level refers to the Benchmark levels that CIS assigns to a profile. </p>"""
    schedule: NotRequired["aws_sdk_inspector2.types.schedule.Schedule"]
    """<p>The schedule for the CIS scan configuration.</p>"""
    targets: NotRequired["aws_sdk_inspector2.types.update_cis_targets.UpdateCisTargets"]
    """<p>The targets for the CIS scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCisScanConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    if "scan_name" in value:
        out["scanName"] = value["scan_name"]
    if "security_level" in value:
        import aws_sdk_inspector2.types.cis_security_level

        out["securityLevel"] = (
            aws_sdk_inspector2.types.cis_security_level.serialize_json(
                value["security_level"]
            )
        )
    if "schedule" in value:
        import aws_sdk_inspector2.types.schedule

        out["schedule"] = aws_sdk_inspector2.types.schedule.serialize_json(
            value["schedule"]
        )
    if "targets" in value:
        import aws_sdk_inspector2.types.update_cis_targets

        out["targets"] = aws_sdk_inspector2.types.update_cis_targets.serialize_json(
            value["targets"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCisScanConfigurationRequest:
    out: UpdateCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateCisScanConfigurationRequest.scan_configuration_arn required"
        )
    if "scanName" in data:
        out["scan_name"] = data["scanName"]
    if "securityLevel" in data:
        import aws_sdk_inspector2.types.cis_security_level

        out["security_level"] = (
            aws_sdk_inspector2.types.cis_security_level.deserialize_json(
                data["securityLevel"]
            )
        )
    if "schedule" in data:
        import aws_sdk_inspector2.types.schedule

        out["schedule"] = aws_sdk_inspector2.types.schedule.deserialize_json(
            data["schedule"]
        )
    if "targets" in data:
        import aws_sdk_inspector2.types.update_cis_targets

        out["targets"] = aws_sdk_inspector2.types.update_cis_targets.deserialize_json(
            data["targets"]
        )
    return out
