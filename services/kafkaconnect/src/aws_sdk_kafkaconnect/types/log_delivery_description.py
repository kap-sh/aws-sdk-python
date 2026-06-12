"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#LogDeliveryDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.worker_log_delivery_description


class LogDeliveryDescription(TypedDict):
    worker_log_delivery: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_log_delivery_description.WorkerLogDeliveryDescription"
    ]
    """<p>The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogDeliveryDescription) -> dict:
    out: dict = {}
    if "worker_log_delivery" in value:
        import aws_sdk_kafkaconnect.types.worker_log_delivery_description

        out["workerLogDelivery"] = (
            aws_sdk_kafkaconnect.types.worker_log_delivery_description.serialize_json(
                value["worker_log_delivery"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogDeliveryDescription:
    out: LogDeliveryDescription = {}  # type: ignore[typeddict-item]
    if "workerLogDelivery" in data:
        import aws_sdk_kafkaconnect.types.worker_log_delivery_description

        out["worker_log_delivery"] = (
            aws_sdk_kafkaconnect.types.worker_log_delivery_description.deserialize_json(
                data["workerLogDelivery"]
            )
        )
    return out
