"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateBrokerCountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer_min1_max15
    import aws_sdk_kafka.types.__string


class UpdateBrokerCountRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of cluster to update from. A successful operation will then generate a new version.</p>"""
    target_number_of_broker_nodes: NotRequired[
        "aws_sdk_kafka.types.__integer_min1_max15.__integerMin1Max15"
    ]
    """<p>The number of broker nodes that you want the cluster to have after this operation completes successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrokerCountRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "target_number_of_broker_nodes" in value:
        out["targetNumberOfBrokerNodes"] = value["target_number_of_broker_nodes"]
    return out


def deserialize_json(data: dict) -> UpdateBrokerCountRequest:
    out: UpdateBrokerCountRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "targetNumberOfBrokerNodes" in data:
        out["target_number_of_broker_nodes"] = data["targetNumberOfBrokerNodes"]
    return out
