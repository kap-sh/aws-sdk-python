"""Generated from Smithy shape ``com.amazonaws.kafka#StorageInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.ebs_storage_info


class StorageInfo(TypedDict):
    ebs_storage_info: NotRequired["aws_sdk_kafka.types.ebs_storage_info.EBSStorageInfo"]
    """<p>EBS volume information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageInfo) -> dict:
    out: dict = {}
    if "ebs_storage_info" in value:
        import aws_sdk_kafka.types.ebs_storage_info

        out["ebsStorageInfo"] = aws_sdk_kafka.types.ebs_storage_info.serialize_json(
            value["ebs_storage_info"]
        )
    return out


def deserialize_json(data: dict) -> StorageInfo:
    out: StorageInfo = {}  # type: ignore[typeddict-item]
    if "ebsStorageInfo" in data:
        import aws_sdk_kafka.types.ebs_storage_info

        out["ebs_storage_info"] = aws_sdk_kafka.types.ebs_storage_info.deserialize_json(
            data["ebsStorageInfo"]
        )
    return out
