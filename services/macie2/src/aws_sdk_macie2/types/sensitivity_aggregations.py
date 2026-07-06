"""Generated from Smithy shape ``com.amazonaws.macie2#SensitivityAggregations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long


class SensitivityAggregations(TypedDict, closed=True):
    classifiable_size_in_bytes: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.</p> <p>If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesn't reflect the storage size of all versions of all applicable objects in the buckets.</p>"""
    publicly_accessible_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket.</p>"""
    total_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets.</p>"""
    total_size_in_bytes: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of the buckets.</p> <p>If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesn't reflect the storage size of all versions of the objects in the buckets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitivityAggregations) -> dict:
    out: dict = {}
    if "classifiable_size_in_bytes" in value:
        out["classifiableSizeInBytes"] = value["classifiable_size_in_bytes"]
    if "publicly_accessible_count" in value:
        out["publiclyAccessibleCount"] = value["publicly_accessible_count"]
    if "total_count" in value:
        out["totalCount"] = value["total_count"]
    if "total_size_in_bytes" in value:
        out["totalSizeInBytes"] = value["total_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> SensitivityAggregations:
    out: SensitivityAggregations = {}  # type: ignore[typeddict-item]
    if "classifiableSizeInBytes" in data:
        out["classifiable_size_in_bytes"] = data["classifiableSizeInBytes"]
    if "publiclyAccessibleCount" in data:
        out["publicly_accessible_count"] = data["publiclyAccessibleCount"]
    if "totalCount" in data:
        out["total_count"] = data["totalCount"]
    if "totalSizeInBytes" in data:
        out["total_size_in_bytes"] = data["totalSizeInBytes"]
    return out
