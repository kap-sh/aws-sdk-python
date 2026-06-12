"""Generated from Smithy shape ``com.amazonaws.snowball#DataTransfer``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.long


class DataTransfer(TypedDict):
    bytes_transferred: "aws_sdk_snowball.types.long.Long"
    """<p>The number of bytes transferred between a Snow device and Amazon S3.</p>"""
    objects_transferred: "aws_sdk_snowball.types.long.Long"
    """<p>The number of objects transferred between a Snow device and Amazon S3.</p>"""
    total_bytes: "aws_sdk_snowball.types.long.Long"
    """<p>The total bytes of data for a transfer between a Snow device and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.</p>"""
    total_objects: "aws_sdk_snowball.types.long.Long"
    """<p>The total number of objects for a transfer between a Snow device and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataTransfer) -> dict:
    out: dict = {}
    out["BytesTransferred"] = value.get("bytes_transferred", 0)
    out["ObjectsTransferred"] = value.get("objects_transferred", 0)
    out["TotalBytes"] = value.get("total_bytes", 0)
    out["TotalObjects"] = value.get("total_objects", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DataTransfer:
    out: DataTransfer = {}  # type: ignore[typeddict-item]
    if "BytesTransferred" in data:
        out["bytes_transferred"] = data["BytesTransferred"]
    else:
        out["bytes_transferred"] = 0
    if "ObjectsTransferred" in data:
        out["objects_transferred"] = data["ObjectsTransferred"]
    else:
        out["objects_transferred"] = 0
    if "TotalBytes" in data:
        out["total_bytes"] = data["TotalBytes"]
    else:
        out["total_bytes"] = 0
    if "TotalObjects" in data:
        out["total_objects"] = data["TotalObjects"]
    else:
        out["total_objects"] = 0
    return out
