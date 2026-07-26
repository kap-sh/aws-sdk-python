"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfBrokerEBSVolumeInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.broker_ebs_volume_info

__listOfBrokerEBSVolumeInfo: TypeAlias = list[
    "capo_kafka.types.broker_ebs_volume_info.BrokerEBSVolumeInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBrokerEBSVolumeInfo) -> list:
    import capo_kafka.types.broker_ebs_volume_info

    out: list = []
    for item in value:
        out.append(capo_kafka.types.broker_ebs_volume_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBrokerEBSVolumeInfo:
    import capo_kafka.types.broker_ebs_volume_info

    out: __listOfBrokerEBSVolumeInfo = []
    for item in data:
        out.append(capo_kafka.types.broker_ebs_volume_info.deserialize_json(item))
    return out
