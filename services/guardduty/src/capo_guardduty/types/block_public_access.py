"""Generated from Smithy shape ``com.amazonaws.guardduty#BlockPublicAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean


class BlockPublicAccess(TypedDict, closed=True):
    ignore_public_acls: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates if S3 Block Public Access is set to <code>IgnorePublicAcls</code>.</p>"""
    restrict_public_buckets: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates if S3 Block Public Access is set to <code>RestrictPublicBuckets</code>.</p>"""
    block_public_acls: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates if S3 Block Public Access is set to <code>BlockPublicAcls</code>.</p>"""
    block_public_policy: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates if S3 Block Public Access is set to <code>BlockPublicPolicy</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockPublicAccess) -> dict:
    out: dict = {}
    if "ignore_public_acls" in value:
        out["ignorePublicAcls"] = value["ignore_public_acls"]
    if "restrict_public_buckets" in value:
        out["restrictPublicBuckets"] = value["restrict_public_buckets"]
    if "block_public_acls" in value:
        out["blockPublicAcls"] = value["block_public_acls"]
    if "block_public_policy" in value:
        out["blockPublicPolicy"] = value["block_public_policy"]
    return out


def deserialize_json(data: dict) -> BlockPublicAccess:
    out: BlockPublicAccess = {}  # type: ignore[typeddict-item]
    if "ignorePublicAcls" in data:
        out["ignore_public_acls"] = data["ignorePublicAcls"]
    if "restrictPublicBuckets" in data:
        out["restrict_public_buckets"] = data["restrictPublicBuckets"]
    if "blockPublicAcls" in data:
        out["block_public_acls"] = data["blockPublicAcls"]
    if "blockPublicPolicy" in data:
        out["block_public_policy"] = data["blockPublicPolicy"]
    return out
