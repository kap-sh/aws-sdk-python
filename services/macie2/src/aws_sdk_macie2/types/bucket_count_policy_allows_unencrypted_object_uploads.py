"""Generated from Smithy shape ``com.amazonaws.macie2#BucketCountPolicyAllowsUnencryptedObjectUploads``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long


class BucketCountPolicyAllowsUnencryptedObjectUploads(TypedDict):
    allows_unencrypted_object_uploads: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that don't have a bucket policy or have a bucket policy that doesn't require server-side encryption of new objects. If a bucket policy exists, the policy doesn't require PutObject requests to include a valid server-side encryption header: the x-amz-server-side-encryption header with a value of AES256 or aws:kms, or the x-amz-server-side-encryption-customer-algorithm header with a value of AES256.</p>"""
    denies_unencrypted_object_uploads: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets whose bucket policies require server-side encryption of new objects. PutObject requests for these buckets must include a valid server-side encryption header: the x-amz-server-side-encryption header with a value of AES256 or aws:kms, or the x-amz-server-side-encryption-customer-algorithm header with a value of AES256.</p>"""
    unknown: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that Amazon Macie wasn't able to evaluate server-side encryption requirements for. For example, the buckets' permissions settings or a quota prevented Macie from retrieving the requisite data. Macie can't determine whether bucket policies for the buckets require server-side encryption of new objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BucketCountPolicyAllowsUnencryptedObjectUploads) -> dict:
    out: dict = {}
    if "allows_unencrypted_object_uploads" in value:
        out["allowsUnencryptedObjectUploads"] = value[
            "allows_unencrypted_object_uploads"
        ]
    if "denies_unencrypted_object_uploads" in value:
        out["deniesUnencryptedObjectUploads"] = value[
            "denies_unencrypted_object_uploads"
        ]
    if "unknown" in value:
        out["unknown"] = value["unknown"]
    return out


def deserialize_json(data: dict) -> BucketCountPolicyAllowsUnencryptedObjectUploads:
    out: BucketCountPolicyAllowsUnencryptedObjectUploads = {}  # type: ignore[typeddict-item]
    if "allowsUnencryptedObjectUploads" in data:
        out["allows_unencrypted_object_uploads"] = data[
            "allowsUnencryptedObjectUploads"
        ]
    if "deniesUnencryptedObjectUploads" in data:
        out["denies_unencrypted_object_uploads"] = data[
            "deniesUnencryptedObjectUploads"
        ]
    if "unknown" in data:
        out["unknown"] = data["unknown"]
    return out
