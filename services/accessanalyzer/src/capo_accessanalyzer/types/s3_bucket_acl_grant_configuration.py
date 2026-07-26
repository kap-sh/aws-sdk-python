"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3BucketAclGrantConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.acl_grantee
    import capo_accessanalyzer.types.acl_permission


class S3BucketAclGrantConfiguration(TypedDict, closed=True):
    permission: "capo_accessanalyzer.types.acl_permission.AclPermission"
    """<p>The permissions being granted.</p>"""
    grantee: "capo_accessanalyzer.types.acl_grantee.AclGrantee"
    """<p>The grantee to whom you’re assigning access rights.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketAclGrantConfiguration) -> dict:
    out: dict = {}
    out["permission"] = value["permission"]
    import capo_accessanalyzer.types.acl_grantee

    out["grantee"] = capo_accessanalyzer.types.acl_grantee.serialize_json(
        value["grantee"]
    )
    return out


def deserialize_json(data: dict) -> S3BucketAclGrantConfiguration:
    out: S3BucketAclGrantConfiguration = {}  # type: ignore[typeddict-item]
    if "permission" in data:
        out["permission"] = data["permission"]
    else:
        raise DeserializationError("S3BucketAclGrantConfiguration.permission required")
    if "grantee" in data:
        import capo_accessanalyzer.types.acl_grantee

        out["grantee"] = capo_accessanalyzer.types.acl_grantee.deserialize_json(
            data["grantee"]
        )
    else:
        raise DeserializationError("S3BucketAclGrantConfiguration.grantee required")
    return out
