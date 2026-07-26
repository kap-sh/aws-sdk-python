"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#LogDelivery``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.worker_log_delivery


class LogDelivery(TypedDict, closed=True):
    worker_log_delivery: "capo_kafkaconnect.types.worker_log_delivery.WorkerLogDelivery"
    """<p>The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogDelivery) -> dict:
    out: dict = {}
    import capo_kafkaconnect.types.worker_log_delivery

    out["workerLogDelivery"] = (
        capo_kafkaconnect.types.worker_log_delivery.serialize_json(
            value["worker_log_delivery"]
        )
    )
    return out


def deserialize_json(data: dict) -> LogDelivery:
    out: LogDelivery = {}  # type: ignore[typeddict-item]
    if "workerLogDelivery" in data:
        import capo_kafkaconnect.types.worker_log_delivery

        out["worker_log_delivery"] = (
            capo_kafkaconnect.types.worker_log_delivery.deserialize_json(
                data["workerLogDelivery"]
            )
        )
    else:
        raise DeserializationError("LogDelivery.worker_log_delivery required")
    return out
