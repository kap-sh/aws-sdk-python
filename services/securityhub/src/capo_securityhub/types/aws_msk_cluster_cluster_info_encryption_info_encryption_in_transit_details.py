"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails(
    TypedDict, closed=True
):
    in_cluster: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> When set to <code>true</code>, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to <code>false</code>, the communication happens in plain text. The default value is <code>true</code>.</p>"""
    client_broker: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Indicates the encryption setting for data in transit between clients and brokers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails,
) -> dict:
    out: dict = {}
    if "in_cluster" in value:
        out["InCluster"] = value["in_cluster"]
    if "client_broker" in value:
        out["ClientBroker"] = value["client_broker"]
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails:
    out: AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails = {}  # type: ignore[typeddict-item]
    if "InCluster" in data:
        out["in_cluster"] = data["InCluster"]
    if "ClientBroker" in data:
        out["client_broker"] = data["ClientBroker"]
    return out
