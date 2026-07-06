"""Generated from Smithy shape ``com.amazonaws.macie2#S3BucketOwner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class S3BucketOwner(TypedDict, closed=True):
    display_name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The display name of the account that owns the bucket.</p>"""
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The canonical user ID for the account that owns the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketOwner) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> S3BucketOwner:
    out: S3BucketOwner = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "id" in data:
        out["id"] = data["id"]
    return out
