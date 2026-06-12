"""Generated from Smithy shape ``com.amazonaws.macie2#BucketCountByEffectivePermission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long


class BucketCountByEffectivePermission(TypedDict):
    publicly_accessible: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that allow the general public to have read or write access to the bucket.</p>"""
    publicly_readable: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that allow the general public to have read access to the bucket.</p>"""
    publicly_writable: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that allow the general public to have write access to the bucket.</p>"""
    unknown: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that Amazon Macie wasn't able to evaluate permissions settings for. For example, the buckets' policies or a quota prevented Macie from retrieving the requisite data. Macie can't determine whether the buckets are publicly accessible.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketCountByEffectivePermission) -> dict:
    out: dict = {}
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "publicly_readable" in value:
        out["publiclyReadable"] = value["publicly_readable"]
    if "publicly_writable" in value:
        out["publiclyWritable"] = value["publicly_writable"]
    if "unknown" in value:
        out["unknown"] = value["unknown"]
    return out


def deserialize_json(data: dict) -> BucketCountByEffectivePermission:
    out: BucketCountByEffectivePermission = {}  # type: ignore[typeddict-item]
    if "publiclyAccessible" in data:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if "publiclyReadable" in data:
        out["publicly_readable"] = data["publiclyReadable"]
    if "publiclyWritable" in data:
        out["publicly_writable"] = data["publiclyWritable"]
    if "unknown" in data:
        out["unknown"] = data["unknown"]
    return out
