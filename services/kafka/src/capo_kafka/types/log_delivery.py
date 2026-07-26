"""Generated from Smithy shape ``com.amazonaws.kafka#LogDelivery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.replicator_log_delivery


class LogDelivery(TypedDict, closed=True):
    replicator_log_delivery: NotRequired[
        "capo_kafka.types.replicator_log_delivery.ReplicatorLogDelivery"
    ]
    """<p>Configuration for replicator log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogDelivery) -> dict:
    out: dict = {}
    if "replicator_log_delivery" in value:
        import capo_kafka.types.replicator_log_delivery

        out["replicatorLogDelivery"] = (
            capo_kafka.types.replicator_log_delivery.serialize_json(
                value["replicator_log_delivery"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogDelivery:
    out: LogDelivery = {}  # type: ignore[typeddict-item]
    if "replicatorLogDelivery" in data:
        import capo_kafka.types.replicator_log_delivery

        out["replicator_log_delivery"] = (
            capo_kafka.types.replicator_log_delivery.deserialize_json(
                data["replicatorLogDelivery"]
            )
        )
    return out
