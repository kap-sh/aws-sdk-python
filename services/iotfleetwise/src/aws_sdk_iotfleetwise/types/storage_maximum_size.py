"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMaximumSize``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.storage_maximum_size_unit
    import aws_sdk_iotfleetwise.types.storage_maximum_size_value


class StorageMaximumSize(TypedDict):
    unit: "aws_sdk_iotfleetwise.types.storage_maximum_size_unit.StorageMaximumSizeUnit"
    """<p>The data type of the data to store.</p>"""
    value: (
        "aws_sdk_iotfleetwise.types.storage_maximum_size_value.StorageMaximumSizeValue"
    )
    """<p>The maximum amount of time to store data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageMaximumSize) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.storage_maximum_size_unit

    out["unit"] = (
        aws_sdk_iotfleetwise.types.storage_maximum_size_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StorageMaximumSize:
    out: StorageMaximumSize = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import aws_sdk_iotfleetwise.types.storage_maximum_size_unit

        out["unit"] = (
            aws_sdk_iotfleetwise.types.storage_maximum_size_unit.deserialize_aws_json_1_0(
                data["unit"]
            )
        )
    else:
        raise DeserializationError("StorageMaximumSize.unit required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("StorageMaximumSize.value required")
    return out
