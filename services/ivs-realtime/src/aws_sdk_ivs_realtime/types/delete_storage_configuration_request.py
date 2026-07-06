"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DeleteStorageConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.storage_configuration_arn


class DeleteStorageConfigurationRequest(TypedDict, closed=True):
    arn: "aws_sdk_ivs_realtime.types.storage_configuration_arn.StorageConfigurationArn"
    """<p>ARN of the storage configuration to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStorageConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteStorageConfigurationRequest:
    out: DeleteStorageConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteStorageConfigurationRequest.arn required")
    return out
