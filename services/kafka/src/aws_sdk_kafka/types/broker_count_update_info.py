"""Generated from Smithy shape ``com.amazonaws.kafka#BrokerCountUpdateInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__double


class BrokerCountUpdateInfo(TypedDict, closed=True):
    created_broker_ids: NotRequired[
        "aws_sdk_kafka.types.__list_of__double.__listOf__double"
    ]
    """<p>Kafka Broker IDs of brokers being created.</p>"""
    deleted_broker_ids: NotRequired[
        "aws_sdk_kafka.types.__list_of__double.__listOf__double"
    ]
    """<p>Kafka Broker IDs of brokers being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerCountUpdateInfo) -> dict:
    out: dict = {}
    if "created_broker_ids" in value:
        import aws_sdk_kafka.types.__list_of__double

        out["createdBrokerIds"] = aws_sdk_kafka.types.__list_of__double.serialize_json(
            value["created_broker_ids"]
        )
    if "deleted_broker_ids" in value:
        import aws_sdk_kafka.types.__list_of__double

        out["deletedBrokerIds"] = aws_sdk_kafka.types.__list_of__double.serialize_json(
            value["deleted_broker_ids"]
        )
    return out


def deserialize_json(data: dict) -> BrokerCountUpdateInfo:
    out: BrokerCountUpdateInfo = {}  # type: ignore[typeddict-item]
    if "createdBrokerIds" in data:
        import aws_sdk_kafka.types.__list_of__double

        out["created_broker_ids"] = (
            aws_sdk_kafka.types.__list_of__double.deserialize_json(
                data["createdBrokerIds"]
            )
        )
    if "deletedBrokerIds" in data:
        import aws_sdk_kafka.types.__list_of__double

        out["deleted_broker_ids"] = (
            aws_sdk_kafka.types.__list_of__double.deserialize_json(
                data["deletedBrokerIds"]
            )
        )
    return out
