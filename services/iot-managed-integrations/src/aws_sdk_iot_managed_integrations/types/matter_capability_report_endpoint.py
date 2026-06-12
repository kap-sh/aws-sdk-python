"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.device_types
    import aws_sdk_iot_managed_integrations.types.endpoint_id
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_clusters
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_parts
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags


class MatterCapabilityReportEndpoint(TypedDict):
    id: "aws_sdk_iot_managed_integrations.types.endpoint_id.EndpointId"
    """<p>The id of the Amazon Web Services Matter capability report endpoint.</p>"""
    device_types: "aws_sdk_iot_managed_integrations.types.device_types.DeviceTypes"
    """<p>The type of device.</p>"""
    clusters: "aws_sdk_iot_managed_integrations.types.matter_capability_report_clusters.MatterCapabilityReportClusters"
    """<p>Matter clusters used in capability report.</p>"""
    parts: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_parts.MatterCapabilityReportEndpointParts"
    ]
    """<p>Heirachy of child endpoints contained in the given endpoint.</p>"""
    semantic_tags: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags.MatterCapabilityReportEndpointSemanticTags"
    ]
    """<p>Semantic information related to endpoint.</p>"""
    client_clusters: NotRequired[
        "aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters.MatterCapabilityReportEndpointClientClusters"
    ]
    """<p>Semantic information related to endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportEndpoint) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_iot_managed_integrations.types.device_types

    out["deviceTypes"] = (
        aws_sdk_iot_managed_integrations.types.device_types.serialize_json(
            value["device_types"]
        )
    )
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_clusters

    out["clusters"] = (
        aws_sdk_iot_managed_integrations.types.matter_capability_report_clusters.serialize_json(
            value["clusters"]
        )
    )
    if "parts" in value:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_parts

        out["parts"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_parts.serialize_json(
                value["parts"]
            )
        )
    if "semantic_tags" in value:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags

        out["semanticTags"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags.serialize_json(
                value["semantic_tags"]
            )
        )
    if "client_clusters" in value:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters

        out["clientClusters"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters.serialize_json(
                value["client_clusters"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatterCapabilityReportEndpoint:
    out: MatterCapabilityReportEndpoint = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("MatterCapabilityReportEndpoint.id required")
    if "deviceTypes" in data:
        import aws_sdk_iot_managed_integrations.types.device_types

        out["device_types"] = (
            aws_sdk_iot_managed_integrations.types.device_types.deserialize_json(
                data["deviceTypes"]
            )
        )
    else:
        raise DeserializationError(
            "MatterCapabilityReportEndpoint.device_types required"
        )
    if "clusters" in data:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_clusters

        out["clusters"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_clusters.deserialize_json(
                data["clusters"]
            )
        )
    else:
        raise DeserializationError("MatterCapabilityReportEndpoint.clusters required")
    if "parts" in data:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_parts

        out["parts"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_parts.deserialize_json(
                data["parts"]
            )
        )
    if "semanticTags" in data:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags

        out["semantic_tags"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags.deserialize_json(
                data["semanticTags"]
            )
        )
    if "clientClusters" in data:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters

        out["client_clusters"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters.deserialize_json(
                data["clientClusters"]
            )
        )
    return out
