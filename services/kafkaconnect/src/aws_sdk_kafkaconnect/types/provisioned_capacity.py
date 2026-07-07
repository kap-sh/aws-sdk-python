"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ProvisionedCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__integer
    import aws_sdk_kafkaconnect.types.__integer_min1_max8


class ProvisionedCapacity(TypedDict, closed=True):
    mcu_count: "aws_sdk_kafkaconnect.types.__integer_min1_max8.__integerMin1Max8"
    """<p>The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.</p>"""
    worker_count: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The number of workers that are allocated to the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedCapacity) -> dict:
    out: dict = {}
    out["mcuCount"] = value.get("mcu_count", 0)
    out["workerCount"] = value.get("worker_count", 0)
    return out


def deserialize_json(data: dict) -> ProvisionedCapacity:
    out: ProvisionedCapacity = {}  # type: ignore[typeddict-item]
    if "mcuCount" in data:
        out["mcu_count"] = data["mcuCount"]
    else:
        out["mcu_count"] = 0
    if "workerCount" in data:
        out["worker_count"] = data["workerCount"]
    else:
        out["worker_count"] = 0
    return out
