"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMinimumTimeToLive``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.storage_minimum_time_to_live_unit
    import capo_iotfleetwise.types.storage_minimum_time_to_live_value


class StorageMinimumTimeToLive(TypedDict, closed=True):
    unit: "capo_iotfleetwise.types.storage_minimum_time_to_live_unit.StorageMinimumTimeToLiveUnit"
    """<p>The time increment type.</p>"""
    value: "capo_iotfleetwise.types.storage_minimum_time_to_live_value.StorageMinimumTimeToLiveValue"
    """<p>The minimum amount of time to store the data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageMinimumTimeToLive) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.storage_minimum_time_to_live_unit

    out["unit"] = (
        capo_iotfleetwise.types.storage_minimum_time_to_live_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StorageMinimumTimeToLive:
    out: StorageMinimumTimeToLive = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import capo_iotfleetwise.types.storage_minimum_time_to_live_unit

        out["unit"] = (
            capo_iotfleetwise.types.storage_minimum_time_to_live_unit.deserialize_aws_json_1_0(
                data["unit"]
            )
        )
    else:
        raise DeserializationError("StorageMinimumTimeToLive.unit required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("StorageMinimumTimeToLive.value required")
    return out
