"""Generated from Smithy shape ``com.amazonaws.macie2#ResourceStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long


class ResourceStatistics(TypedDict):
    total_bytes_classified: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total amount of data, in bytes, that Amazon Macie has analyzed in the bucket.</p>"""
    total_detections: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of occurrences of sensitive data that Amazon Macie has found in the bucket's objects. This includes occurrences that are currently suppressed by the sensitivity scoring settings for the bucket (totalDetectionsSuppressed).</p>"""
    total_detections_suppressed: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of occurrences of sensitive data that are currently suppressed by the sensitivity scoring settings for the bucket. These represent occurrences of sensitive data that Amazon Macie found in the bucket's objects, but the occurrences were manually suppressed. By default, suppressed occurrences are excluded from the bucket's sensitivity score.</p>"""
    total_items_classified: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of objects that Amazon Macie has analyzed in the bucket.</p>"""
    total_items_sensitive: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of the bucket's objects that Amazon Macie has found sensitive data in.</p>"""
    total_items_skipped: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of objects that Amazon Macie wasn't able to analyze in the bucket due to an object-level issue or error. For example, an object is a malformed file. This value includes objects that Macie wasn't able to analyze for reasons reported by other statistics in the ResourceStatistics object.</p>"""
    total_items_skipped_invalid_encryption: NotRequired[
        "aws_sdk_macie2.types.__long.__long"
    ]
    """<p>The total number of objects that Amazon Macie wasn't able to analyze in the bucket because the objects are encrypted with a key that Macie can't access. The objects use server-side encryption with customer-provided keys (SSE-C).</p>"""
    total_items_skipped_invalid_kms: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of objects that Amazon Macie wasn't able to analyze in the bucket because the objects are encrypted with KMS keys that were disabled, are scheduled for deletion, or were deleted.</p>"""
    total_items_skipped_permission_denied: NotRequired[
        "aws_sdk_macie2.types.__long.__long"
    ]
    """<p>The total number of objects that Amazon Macie wasn't able to analyze in the bucket due to the permissions settings for the objects or the permissions settings for the keys that were used to encrypt the objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatistics) -> dict:
    out: dict = {}
    if "total_bytes_classified" in value:
        out["totalBytesClassified"] = value["total_bytes_classified"]
    if "total_detections" in value:
        out["totalDetections"] = value["total_detections"]
    if "total_detections_suppressed" in value:
        out["totalDetectionsSuppressed"] = value["total_detections_suppressed"]
    if "total_items_classified" in value:
        out["totalItemsClassified"] = value["total_items_classified"]
    if "total_items_sensitive" in value:
        out["totalItemsSensitive"] = value["total_items_sensitive"]
    if "total_items_skipped" in value:
        out["totalItemsSkipped"] = value["total_items_skipped"]
    if "total_items_skipped_invalid_encryption" in value:
        out["totalItemsSkippedInvalidEncryption"] = value[
            "total_items_skipped_invalid_encryption"
        ]
    if "total_items_skipped_invalid_kms" in value:
        out["totalItemsSkippedInvalidKms"] = value["total_items_skipped_invalid_kms"]
    if "total_items_skipped_permission_denied" in value:
        out["totalItemsSkippedPermissionDenied"] = value[
            "total_items_skipped_permission_denied"
        ]
    return out


def deserialize_json(data: dict) -> ResourceStatistics:
    out: ResourceStatistics = {}  # type: ignore[typeddict-item]
    if "totalBytesClassified" in data:
        out["total_bytes_classified"] = data["totalBytesClassified"]
    if "totalDetections" in data:
        out["total_detections"] = data["totalDetections"]
    if "totalDetectionsSuppressed" in data:
        out["total_detections_suppressed"] = data["totalDetectionsSuppressed"]
    if "totalItemsClassified" in data:
        out["total_items_classified"] = data["totalItemsClassified"]
    if "totalItemsSensitive" in data:
        out["total_items_sensitive"] = data["totalItemsSensitive"]
    if "totalItemsSkipped" in data:
        out["total_items_skipped"] = data["totalItemsSkipped"]
    if "totalItemsSkippedInvalidEncryption" in data:
        out["total_items_skipped_invalid_encryption"] = data[
            "totalItemsSkippedInvalidEncryption"
        ]
    if "totalItemsSkippedInvalidKms" in data:
        out["total_items_skipped_invalid_kms"] = data["totalItemsSkippedInvalidKms"]
    if "totalItemsSkippedPermissionDenied" in data:
        out["total_items_skipped_permission_denied"] = data[
            "totalItemsSkippedPermissionDenied"
        ]
    return out
