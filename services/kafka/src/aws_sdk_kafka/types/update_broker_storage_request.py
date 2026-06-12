"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateBrokerStorageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_broker_ebs_volume_info
    import aws_sdk_kafka.types.__string


class UpdateBrokerStorageRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of cluster to update from. A successful operation will then generate a new version.</p>"""
    target_broker_ebs_volume_info: NotRequired[
        "aws_sdk_kafka.types.__list_of_broker_ebs_volume_info.__listOfBrokerEBSVolumeInfo"
    ]
    """<p>Describes the target volume size and the ID of the broker to apply the update to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrokerStorageRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "target_broker_ebs_volume_info" in value:
        import aws_sdk_kafka.types.__list_of_broker_ebs_volume_info

        out["targetBrokerEBSVolumeInfo"] = (
            aws_sdk_kafka.types.__list_of_broker_ebs_volume_info.serialize_json(
                value["target_broker_ebs_volume_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBrokerStorageRequest:
    out: UpdateBrokerStorageRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "targetBrokerEBSVolumeInfo" in data:
        import aws_sdk_kafka.types.__list_of_broker_ebs_volume_info

        out["target_broker_ebs_volume_info"] = (
            aws_sdk_kafka.types.__list_of_broker_ebs_volume_info.deserialize_json(
                data["targetBrokerEBSVolumeInfo"]
            )
        )
    return out
