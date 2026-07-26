"""Generated from Smithy shape ``com.amazonaws.macie2#BucketCountBySharedAccessType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long


class BucketCountBySharedAccessType(TypedDict, closed=True):
    external: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of buckets that are shared with one or more of the following or any combination of the following: an Amazon CloudFront OAI, a CloudFront OAC, or an Amazon Web Services account that isn't in the same Amazon Macie organization.</p>"""
    internal: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of buckets that are shared with one or more Amazon Web Services accounts in the same Amazon Macie organization. These buckets aren't shared with Amazon CloudFront OAIs or OACs.</p>"""
    not_shared: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of buckets that aren't shared with other Amazon Web Services accounts, Amazon CloudFront OAIs, or CloudFront OACs.</p>"""
    unknown: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of buckets that Amazon Macie wasn't able to evaluate shared access settings for. For example, the buckets' permissions settings or a quota prevented Macie from retrieving the requisite data. Macie can't determine whether the buckets are shared with other Amazon Web Services accounts, Amazon CloudFront OAIs, or CloudFront OACs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketCountBySharedAccessType) -> dict:
    out: dict = {}
    if "external" in value:
        out["external"] = value["external"]
    if "internal" in value:
        out["internal"] = value["internal"]
    if "not_shared" in value:
        out["notShared"] = value["not_shared"]
    if "unknown" in value:
        out["unknown"] = value["unknown"]
    return out


def deserialize_json(data: dict) -> BucketCountBySharedAccessType:
    out: BucketCountBySharedAccessType = {}  # type: ignore[typeddict-item]
    if "external" in data:
        out["external"] = data["external"]
    if "internal" in data:
        out["internal"] = data["internal"]
    if "notShared" in data:
        out["not_shared"] = data["notShared"]
    if "unknown" in data:
        out["unknown"] = data["unknown"]
    return out
