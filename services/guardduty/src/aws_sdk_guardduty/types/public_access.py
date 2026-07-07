"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.permission_configuration
    import aws_sdk_guardduty.types.string


class PublicAccess(TypedDict, closed=True):
    permission_configuration: NotRequired[
        "aws_sdk_guardduty.types.permission_configuration.PermissionConfiguration"
    ]
    """<p>Contains information about how permissions are configured for the S3 bucket.</p>"""
    effective_permission: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Describes the effective permission on this bucket after factoring all attached policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicAccess) -> dict:
    out: dict = {}
    if "permission_configuration" in value:
        import aws_sdk_guardduty.types.permission_configuration

        out["permissionConfiguration"] = (
            aws_sdk_guardduty.types.permission_configuration.serialize_json(
                value["permission_configuration"]
            )
        )
    if "effective_permission" in value:
        out["effectivePermission"] = value["effective_permission"]
    return out


def deserialize_json(data: dict) -> PublicAccess:
    out: PublicAccess = {}  # type: ignore[typeddict-item]
    if "permissionConfiguration" in data:
        import aws_sdk_guardduty.types.permission_configuration

        out["permission_configuration"] = (
            aws_sdk_guardduty.types.permission_configuration.deserialize_json(
                data["permissionConfiguration"]
            )
        )
    if "effectivePermission" in data:
        out["effective_permission"] = data["effectivePermission"]
    return out
