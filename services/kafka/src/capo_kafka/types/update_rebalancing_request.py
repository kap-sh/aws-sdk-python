"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateRebalancingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.rebalancing


class UpdateRebalancingRequest(TypedDict, closed=True):
    cluster_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The current version of the cluster.</p>"""
    rebalancing: NotRequired["capo_kafka.types.rebalancing.Rebalancing"]
    """<p>Specifies if intelligent rebalancing should be turned on for your cluster. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters that you create with Express brokers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRebalancingRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "rebalancing" in value:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.serialize_json(
            value["rebalancing"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRebalancingRequest:
    out: UpdateRebalancingRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "rebalancing" in data:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.deserialize_json(
            data["rebalancing"]
        )
    return out
