"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateRebalancingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.rebalancing


class UpdateRebalancingRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The current version of the cluster.</p>"""
    rebalancing: NotRequired["aws_sdk_kafka.types.rebalancing.Rebalancing"]
    """<p>Specifies if intelligent rebalancing should be turned on for your cluster. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters that you create with Express brokers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRebalancingRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "rebalancing" in value:
        import aws_sdk_kafka.types.rebalancing

        out["rebalancing"] = aws_sdk_kafka.types.rebalancing.serialize_json(
            value["rebalancing"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRebalancingRequest:
    out: UpdateRebalancingRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "rebalancing" in data:
        import aws_sdk_kafka.types.rebalancing

        out["rebalancing"] = aws_sdk_kafka.types.rebalancing.deserialize_json(
            data["rebalancing"]
        )
    return out
