"""Generated from Smithy shape ``com.amazonaws.rtbfabric#EksEndpointsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.base64_encoded_certificate_chain
    import aws_sdk_rtbfabric.types.kubernetes_cluster_name
    import aws_sdk_rtbfabric.types.kubernetes_endpoints_resource_name
    import aws_sdk_rtbfabric.types.kubernetes_namespace
    import aws_sdk_rtbfabric.types.uri


class EksEndpointsConfiguration(TypedDict):
    endpoints_resource_name: "aws_sdk_rtbfabric.types.kubernetes_endpoints_resource_name.KubernetesEndpointsResourceName"
    """<p>The name of the endpoint resource.</p>"""
    endpoints_resource_namespace: (
        "aws_sdk_rtbfabric.types.kubernetes_namespace.KubernetesNamespace"
    )
    """<p>The namespace of the endpoint resource.</p>"""
    cluster_api_server_endpoint_uri: "aws_sdk_rtbfabric.types.uri.URI"
    """<p>The URI of the cluster API server endpoint.</p>"""
    cluster_api_server_ca_certificate_chain: "aws_sdk_rtbfabric.types.base64_encoded_certificate_chain.Base64EncodedCertificateChain"
    """<p>The CA certificate chain of the cluster API server.</p>"""
    cluster_name: (
        "aws_sdk_rtbfabric.types.kubernetes_cluster_name.KubernetesClusterName"
    )
    """<p>The name of the cluster.</p>"""
    role_arn: "str"
    """<p>The role ARN for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksEndpointsConfiguration) -> dict:
    out: dict = {}
    out["endpointsResourceName"] = value["endpoints_resource_name"]
    out["endpointsResourceNamespace"] = value["endpoints_resource_namespace"]
    out["clusterApiServerEndpointUri"] = value["cluster_api_server_endpoint_uri"]
    out["clusterApiServerCaCertificateChain"] = value[
        "cluster_api_server_ca_certificate_chain"
    ]
    out["clusterName"] = value["cluster_name"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> EksEndpointsConfiguration:
    out: EksEndpointsConfiguration = {}  # type: ignore[typeddict-item]
    if "endpointsResourceName" in data:
        out["endpoints_resource_name"] = data["endpointsResourceName"]
    else:
        raise DeserializationError(
            "EksEndpointsConfiguration.endpoints_resource_name required"
        )
    if "endpointsResourceNamespace" in data:
        out["endpoints_resource_namespace"] = data["endpointsResourceNamespace"]
    else:
        raise DeserializationError(
            "EksEndpointsConfiguration.endpoints_resource_namespace required"
        )
    if "clusterApiServerEndpointUri" in data:
        out["cluster_api_server_endpoint_uri"] = data["clusterApiServerEndpointUri"]
    else:
        raise DeserializationError(
            "EksEndpointsConfiguration.cluster_api_server_endpoint_uri required"
        )
    if "clusterApiServerCaCertificateChain" in data:
        out["cluster_api_server_ca_certificate_chain"] = data[
            "clusterApiServerCaCertificateChain"
        ]
    else:
        raise DeserializationError(
            "EksEndpointsConfiguration.cluster_api_server_ca_certificate_chain required"
        )
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("EksEndpointsConfiguration.cluster_name required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("EksEndpointsConfiguration.role_arn required")
    return out
