"""Generated from Smithy shape ``com.amazonaws.connect#DescribeInstanceStorageConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_storage_config


class DescribeInstanceStorageConfigResponse(TypedDict, closed=True):
    storage_config: NotRequired[
        "capo_connect.types.instance_storage_config.InstanceStorageConfig"
    ]
    """<p>A valid storage type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceStorageConfigResponse) -> dict:
    out: dict = {}
    if "storage_config" in value:
        import capo_connect.types.instance_storage_config

        out["StorageConfig"] = (
            capo_connect.types.instance_storage_config.serialize_json(
                value["storage_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeInstanceStorageConfigResponse:
    out: DescribeInstanceStorageConfigResponse = {}  # type: ignore[typeddict-item]
    if "StorageConfig" in data:
        import capo_connect.types.instance_storage_config

        out["storage_config"] = (
            capo_connect.types.instance_storage_config.deserialize_json(
                data["StorageConfig"]
            )
        )
    return out
