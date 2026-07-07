"""Generated from Smithy shape ``com.amazonaws.kafka#LoggingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.broker_logs


class LoggingInfo(TypedDict, closed=True):
    broker_logs: NotRequired["aws_sdk_kafka.types.broker_logs.BrokerLogs"]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingInfo) -> dict:
    out: dict = {}
    if "broker_logs" in value:
        import aws_sdk_kafka.types.broker_logs

        out["brokerLogs"] = aws_sdk_kafka.types.broker_logs.serialize_json(
            value["broker_logs"]
        )
    return out


def deserialize_json(data: dict) -> LoggingInfo:
    out: LoggingInfo = {}  # type: ignore[typeddict-item]
    if "brokerLogs" in data:
        import aws_sdk_kafka.types.broker_logs

        out["broker_logs"] = aws_sdk_kafka.types.broker_logs.deserialize_json(
            data["brokerLogs"]
        )
    return out
