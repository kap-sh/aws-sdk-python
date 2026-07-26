"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.capacity_description


class WorkerSetting(TypedDict, closed=True):
    capacity: NotRequired[
        "capo_kafkaconnect.types.capacity_description.CapacityDescription"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSetting) -> dict:
    out: dict = {}
    if "capacity" in value:
        import capo_kafkaconnect.types.capacity_description

        out["capacity"] = capo_kafkaconnect.types.capacity_description.serialize_json(
            value["capacity"]
        )
    return out


def deserialize_json(data: dict) -> WorkerSetting:
    out: WorkerSetting = {}  # type: ignore[typeddict-item]
    if "capacity" in data:
        import capo_kafkaconnect.types.capacity_description

        out["capacity"] = capo_kafkaconnect.types.capacity_description.deserialize_json(
            data["capacity"]
        )
    return out
