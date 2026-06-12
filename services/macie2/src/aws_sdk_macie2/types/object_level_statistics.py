"""Generated from Smithy shape ``com.amazonaws.macie2#ObjectLevelStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long


class ObjectLevelStatistics(TypedDict):
    file_type: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects don't have a file name extension for a supported file or storage format.</p>"""
    storage_class: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class.</p>"""
    total: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class or don't have a file name extension for a supported file or storage format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectLevelStatistics) -> dict:
    out: dict = {}
    if "file_type" in value:
        out["fileType"] = value["file_type"]
    if "storage_class" in value:
        out["storageClass"] = value["storage_class"]
    if "total" in value:
        out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> ObjectLevelStatistics:
    out: ObjectLevelStatistics = {}  # type: ignore[typeddict-item]
    if "fileType" in data:
        out["file_type"] = data["fileType"]
    if "storageClass" in data:
        out["storage_class"] = data["storageClass"]
    if "total" in data:
        out["total"] = data["total"]
    return out
