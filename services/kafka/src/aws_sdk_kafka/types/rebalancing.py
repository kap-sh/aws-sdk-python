"""Generated from Smithy shape ``com.amazonaws.kafka#Rebalancing``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.rebalancing_status


class Rebalancing(TypedDict):
    status: NotRequired["aws_sdk_kafka.types.rebalancing_status.RebalancingStatus"]
    """<p>Intelligent rebalancing status. The default intelligent rebalancing status is ACTIVE for all new Express-based clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rebalancing) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_kafka.types.rebalancing_status

        out["status"] = aws_sdk_kafka.types.rebalancing_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> Rebalancing:
    out: Rebalancing = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_kafka.types.rebalancing_status

        out["status"] = aws_sdk_kafka.types.rebalancing_status.deserialize_json(
            data["status"]
        )
    return out
