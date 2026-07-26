"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3PublicAccessBlockConfiguration``."""

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError


class S3PublicAccessBlockConfiguration(TypedDict, closed=True):
    ignore_public_acls: "bool"
    """<p> Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. </p>"""
    restrict_public_buckets: "bool"
    """<p> Specifies whether Amazon S3 should restrict public bucket policies for this bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3PublicAccessBlockConfiguration) -> dict:
    out: dict = {}
    out["ignorePublicAcls"] = value["ignore_public_acls"]
    out["restrictPublicBuckets"] = value["restrict_public_buckets"]
    return out


def deserialize_json(data: dict) -> S3PublicAccessBlockConfiguration:
    out: S3PublicAccessBlockConfiguration = {}  # type: ignore[typeddict-item]
    if "ignorePublicAcls" in data:
        out["ignore_public_acls"] = data["ignorePublicAcls"]
    else:
        raise DeserializationError(
            "S3PublicAccessBlockConfiguration.ignore_public_acls required"
        )
    if "restrictPublicBuckets" in data:
        out["restrict_public_buckets"] = data["restrictPublicBuckets"]
    else:
        raise DeserializationError(
            "S3PublicAccessBlockConfiguration.restrict_public_buckets required"
        )
    return out
