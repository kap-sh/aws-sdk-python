"""Generated from Smithy shape ``com.amazonaws.kafka#BrokerNodeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__double
    import capo_kafka.types.__list_of__string
    import capo_kafka.types.__string
    import capo_kafka.types.broker_software_info


class BrokerNodeInfo(TypedDict, closed=True):
    attached_eni_id: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The attached elastic network interface of the broker.</p>"""
    broker_id: NotRequired["capo_kafka.types.__double.__double"]
    """<p>The ID of the broker.</p>"""
    client_subnet: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The client subnet to which this broker node belongs.</p>"""
    client_vpc_ip_address: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The virtual private cloud (VPC) of the client.</p>"""
    current_broker_software_info: NotRequired[
        "capo_kafka.types.broker_software_info.BrokerSoftwareInfo"
    ]
    """<p>Information about the version of software currently deployed on the Apache Kafka brokers in the cluster.</p>"""
    endpoints: NotRequired["capo_kafka.types.__list_of__string.__listOf__string"]
    """<p>Endpoints for accessing the broker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerNodeInfo) -> dict:
    out: dict = {}
    if "attached_eni_id" in value:
        out["attachedENIId"] = value["attached_eni_id"]
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "client_subnet" in value:
        out["clientSubnet"] = value["client_subnet"]
    if "client_vpc_ip_address" in value:
        out["clientVpcIpAddress"] = value["client_vpc_ip_address"]
    if "current_broker_software_info" in value:
        import capo_kafka.types.broker_software_info

        out["currentBrokerSoftwareInfo"] = (
            capo_kafka.types.broker_software_info.serialize_json(
                value["current_broker_software_info"]
            )
        )
    if "endpoints" in value:
        import capo_kafka.types.__list_of__string

        out["endpoints"] = capo_kafka.types.__list_of__string.serialize_json(
            value["endpoints"]
        )
    return out


def deserialize_json(data: dict) -> BrokerNodeInfo:
    out: BrokerNodeInfo = {}  # type: ignore[typeddict-item]
    if "attachedENIId" in data:
        out["attached_eni_id"] = data["attachedENIId"]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    if "clientSubnet" in data:
        out["client_subnet"] = data["clientSubnet"]
    if "clientVpcIpAddress" in data:
        out["client_vpc_ip_address"] = data["clientVpcIpAddress"]
    if "currentBrokerSoftwareInfo" in data:
        import capo_kafka.types.broker_software_info

        out["current_broker_software_info"] = (
            capo_kafka.types.broker_software_info.deserialize_json(
                data["currentBrokerSoftwareInfo"]
            )
        )
    if "endpoints" in data:
        import capo_kafka.types.__list_of__string

        out["endpoints"] = capo_kafka.types.__list_of__string.deserialize_json(
            data["endpoints"]
        )
    return out
