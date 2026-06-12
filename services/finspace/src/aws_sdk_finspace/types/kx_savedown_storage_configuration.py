"""Generated from Smithy shape ``com.amazonaws.finspace#KxSavedownStorageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_savedown_storage_size
    import aws_sdk_finspace.types.kx_savedown_storage_type
    import aws_sdk_finspace.types.kx_volume_name


class KxSavedownStorageConfiguration(TypedDict):
    type: NotRequired[
        "aws_sdk_finspace.types.kx_savedown_storage_type.KxSavedownStorageType"
    ]
    """<p>The type of writeable storage space for temporarily storing your savedown data. The valid values are:</p> <ul> <li> <p>SDS01 – This type represents 3000 IOPS and io2 ebs volume type.</p> </li> </ul>"""
    size: NotRequired[
        "aws_sdk_finspace.types.kx_savedown_storage_size.KxSavedownStorageSize"
    ]
    """<p>The size of temporary storage in gibibytes.</p>"""
    volume_name: NotRequired["aws_sdk_finspace.types.kx_volume_name.KxVolumeName"]
    """<p> The name of the kdb volume that you want to use as writeable save-down storage for clusters. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxSavedownStorageConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_finspace.types.kx_savedown_storage_type

        out["type"] = aws_sdk_finspace.types.kx_savedown_storage_type.serialize_json(
            value["type"]
        )
    if "size" in value:
        out["size"] = value["size"]
    if "volume_name" in value:
        out["volumeName"] = value["volume_name"]
    return out


def deserialize_json(data: dict) -> KxSavedownStorageConfiguration:
    out: KxSavedownStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_finspace.types.kx_savedown_storage_type

        out["type"] = aws_sdk_finspace.types.kx_savedown_storage_type.deserialize_json(
            data["type"]
        )
    if "size" in data:
        out["size"] = data["size"]
    if "volumeName" in data:
        out["volume_name"] = data["volumeName"]
    return out
