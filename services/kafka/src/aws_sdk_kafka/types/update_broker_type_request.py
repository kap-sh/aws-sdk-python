"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateBrokerTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class UpdateBrokerTypeRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The cluster version that you want to change. After this operation completes successfully, the cluster will have a new version.</p>"""
    target_instance_type: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon MSK broker type that you want all of the brokers in this cluster to be.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrokerTypeRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "target_instance_type" in value:
        out["targetInstanceType"] = value["target_instance_type"]
    return out


def deserialize_json(data: dict) -> UpdateBrokerTypeRequest:
    out: UpdateBrokerTypeRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "targetInstanceType" in data:
        out["target_instance_type"] = data["targetInstanceType"]
    return out
