"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.endpoint_id
    import aws_sdk_iot_managed_integrations.types.matter_clusters


class MatterEndpoint(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iot_managed_integrations.types.endpoint_id.EndpointId"]
    """<p>The Matter endpoint id.</p>"""
    clusters: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_clusters.MatterClusters"
    ]
    """<p>A list of Matter clusters for a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "clusters" in value:
        import aws_sdk_iot_managed_integrations.types.matter_clusters

        out["clusters"] = (
            aws_sdk_iot_managed_integrations.types.matter_clusters.serialize_json(
                value["clusters"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatterEndpoint:
    out: MatterEndpoint = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "clusters" in data:
        import aws_sdk_iot_managed_integrations.types.matter_clusters

        out["clusters"] = (
            aws_sdk_iot_managed_integrations.types.matter_clusters.deserialize_json(
                data["clusters"]
            )
        )
    return out
