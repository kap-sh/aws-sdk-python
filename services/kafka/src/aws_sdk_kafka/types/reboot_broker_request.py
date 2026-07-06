"""Generated from Smithy shape ``com.amazonaws.kafka#RebootBrokerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__string


class RebootBrokerRequest(TypedDict, closed=True):
    broker_ids: NotRequired["aws_sdk_kafka.types.__list_of__string.__listOf__string"]
    """<p>The list of broker IDs to be rebooted. The reboot-broker operation supports rebooting one broker at a time.</p>"""
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RebootBrokerRequest) -> dict:
    out: dict = {}
    if "broker_ids" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["brokerIds"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["broker_ids"]
        )
    return out


def deserialize_json(data: dict) -> RebootBrokerRequest:
    out: RebootBrokerRequest = {}  # type: ignore[typeddict-item]
    if "brokerIds" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["broker_ids"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["brokerIds"]
        )
    return out
