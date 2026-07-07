"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCisScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_name
    import aws_sdk_inspector2.types.cis_security_level
    import aws_sdk_inspector2.types.cis_tag_map
    import aws_sdk_inspector2.types.create_cis_targets
    import aws_sdk_inspector2.types.schedule


class CreateCisScanConfigurationRequest(TypedDict, closed=True):
    scan_name: "aws_sdk_inspector2.types.cis_scan_name.CisScanName"
    """<p>The scan name for the CIS scan configuration.</p>"""
    security_level: "aws_sdk_inspector2.types.cis_security_level.CisSecurityLevel"
    """<p> The security level for the CIS scan configuration. Security level refers to the Benchmark levels that CIS assigns to a profile. </p>"""
    schedule: "aws_sdk_inspector2.types.schedule.Schedule"
    """<p>The schedule for the CIS scan configuration.</p>"""
    targets: "aws_sdk_inspector2.types.create_cis_targets.CreateCisTargets"
    """<p>The targets for the CIS scan configuration.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.cis_tag_map.CisTagMap"]
    """<p>The tags for the CIS scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCisScanConfigurationRequest) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    import aws_sdk_inspector2.types.cis_security_level

    out["securityLevel"] = aws_sdk_inspector2.types.cis_security_level.serialize_json(
        value["security_level"]
    )
    import aws_sdk_inspector2.types.schedule

    out["schedule"] = aws_sdk_inspector2.types.schedule.serialize_json(
        value["schedule"]
    )
    import aws_sdk_inspector2.types.create_cis_targets

    out["targets"] = aws_sdk_inspector2.types.create_cis_targets.serialize_json(
        value["targets"]
    )
    if "tags" in value:
        import aws_sdk_inspector2.types.cis_tag_map

        out["tags"] = aws_sdk_inspector2.types.cis_tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCisScanConfigurationRequest:
    out: CreateCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scanName" in data:
        out["scan_name"] = data["scanName"]
    else:
        raise DeserializationError(
            "CreateCisScanConfigurationRequest.scan_name required"
        )
    if "securityLevel" in data:
        import aws_sdk_inspector2.types.cis_security_level

        out["security_level"] = (
            aws_sdk_inspector2.types.cis_security_level.deserialize_json(
                data["securityLevel"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCisScanConfigurationRequest.security_level required"
        )
    if "schedule" in data:
        import aws_sdk_inspector2.types.schedule

        out["schedule"] = aws_sdk_inspector2.types.schedule.deserialize_json(
            data["schedule"]
        )
    else:
        raise DeserializationError(
            "CreateCisScanConfigurationRequest.schedule required"
        )
    if "targets" in data:
        import aws_sdk_inspector2.types.create_cis_targets

        out["targets"] = aws_sdk_inspector2.types.create_cis_targets.deserialize_json(
            data["targets"]
        )
    else:
        raise DeserializationError("CreateCisScanConfigurationRequest.targets required")
    if "tags" in data:
        import aws_sdk_inspector2.types.cis_tag_map

        out["tags"] = aws_sdk_inspector2.types.cis_tag_map.deserialize_json(
            data["tags"]
        )
    return out
