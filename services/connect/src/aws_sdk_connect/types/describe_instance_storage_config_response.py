"""Generated from Smithy shape ``com.amazonaws.connect#DescribeInstanceStorageConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_storage_config


class DescribeInstanceStorageConfigResponse(TypedDict, closed=True):
    storage_config: NotRequired[
        "aws_sdk_connect.types.instance_storage_config.InstanceStorageConfig"
    ]
    """<p>A valid storage type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceStorageConfigResponse) -> dict:
    out: dict = {}
    if "storage_config" in value:
        import aws_sdk_connect.types.instance_storage_config

        out["StorageConfig"] = (
            aws_sdk_connect.types.instance_storage_config.serialize_json(
                value["storage_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeInstanceStorageConfigResponse:
    out: DescribeInstanceStorageConfigResponse = {}  # type: ignore[typeddict-item]
    if "StorageConfig" in data:
        import aws_sdk_connect.types.instance_storage_config

        out["storage_config"] = (
            aws_sdk_connect.types.instance_storage_config.deserialize_json(
                data["StorageConfig"]
            )
        )
    return out
