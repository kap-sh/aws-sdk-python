"""Generated from Smithy shape ``com.amazonaws.iot#SecurityProfileTargetMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_profile_identifier
    import aws_sdk_iot.types.security_profile_target


class SecurityProfileTargetMapping(TypedDict, closed=True):
    security_profile_identifier: NotRequired[
        "aws_sdk_iot.types.security_profile_identifier.SecurityProfileIdentifier"
    ]
    """<p>Information that identifies the security profile.</p>"""
    target: NotRequired[
        "aws_sdk_iot.types.security_profile_target.SecurityProfileTarget"
    ]
    """<p>Information about the target (thing group) associated with the security profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileTargetMapping) -> dict:
    out: dict = {}
    if "security_profile_identifier" in value:
        import aws_sdk_iot.types.security_profile_identifier

        out["securityProfileIdentifier"] = (
            aws_sdk_iot.types.security_profile_identifier.serialize_json(
                value["security_profile_identifier"]
            )
        )
    if "target" in value:
        import aws_sdk_iot.types.security_profile_target

        out["target"] = aws_sdk_iot.types.security_profile_target.serialize_json(
            value["target"]
        )
    return out


def deserialize_json(data: dict) -> SecurityProfileTargetMapping:
    out: SecurityProfileTargetMapping = {}  # type: ignore[typeddict-item]
    if "securityProfileIdentifier" in data:
        import aws_sdk_iot.types.security_profile_identifier

        out["security_profile_identifier"] = (
            aws_sdk_iot.types.security_profile_identifier.deserialize_json(
                data["securityProfileIdentifier"]
            )
        )
    if "target" in data:
        import aws_sdk_iot.types.security_profile_target

        out["target"] = aws_sdk_iot.types.security_profile_target.deserialize_json(
            data["target"]
        )
    return out
