"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#LogDeliveryDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.worker_log_delivery_description


class LogDeliveryDescription(TypedDict, closed=True):
    worker_log_delivery: NotRequired[
        "capo_kafkaconnect.types.worker_log_delivery_description.WorkerLogDeliveryDescription"
    ]
    """<p>The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogDeliveryDescription) -> dict:
    out: dict = {}
    if "worker_log_delivery" in value:
        import capo_kafkaconnect.types.worker_log_delivery_description

        out["workerLogDelivery"] = (
            capo_kafkaconnect.types.worker_log_delivery_description.serialize_json(
                value["worker_log_delivery"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogDeliveryDescription:
    out: LogDeliveryDescription = {}  # type: ignore[typeddict-item]
    if "workerLogDelivery" in data:
        import capo_kafkaconnect.types.worker_log_delivery_description

        out["worker_log_delivery"] = (
            capo_kafkaconnect.types.worker_log_delivery_description.deserialize_json(
                data["workerLogDelivery"]
            )
        )
    return out
