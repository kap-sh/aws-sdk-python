"""Generated from Smithy shape ``com.amazonaws.macie2#BucketPublicAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.bucket_permission_configuration
    import capo_macie2.types.effective_permission


class BucketPublicAccess(TypedDict, closed=True):
    effective_permission: NotRequired[
        "capo_macie2.types.effective_permission.EffectivePermission"
    ]
    """<p>Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket. Possible values are:</p> <ul><li><p>NOT_PUBLIC - The bucket isn't publicly accessible.</p></li> <li><p>PUBLIC - The bucket is publicly accessible.</p></li> <li><p>UNKNOWN - Amazon Macie can't determine whether the bucket is publicly accessible.</p></li></ul>"""
    permission_configuration: NotRequired[
        "capo_macie2.types.bucket_permission_configuration.BucketPermissionConfiguration"
    ]
    """<p>The account-level and bucket-level permissions settings for the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketPublicAccess) -> dict:
    out: dict = {}
    if "effective_permission" in value:
        import capo_macie2.types.effective_permission

        out["effectivePermission"] = (
            capo_macie2.types.effective_permission.serialize_json(
                value["effective_permission"]
            )
        )
    if "permission_configuration" in value:
        import capo_macie2.types.bucket_permission_configuration

        out["permissionConfiguration"] = (
            capo_macie2.types.bucket_permission_configuration.serialize_json(
                value["permission_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BucketPublicAccess:
    out: BucketPublicAccess = {}  # type: ignore[typeddict-item]
    if "effectivePermission" in data:
        import capo_macie2.types.effective_permission

        out["effective_permission"] = (
            capo_macie2.types.effective_permission.deserialize_json(
                data["effectivePermission"]
            )
        )
    if "permissionConfiguration" in data:
        import capo_macie2.types.bucket_permission_configuration

        out["permission_configuration"] = (
            capo_macie2.types.bucket_permission_configuration.deserialize_json(
                data["permissionConfiguration"]
            )
        )
    return out
