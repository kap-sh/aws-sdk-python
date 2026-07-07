"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_open_search_service_domain_advanced_security_options_details
    import aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_details
    import aws_sdk_securityhub.types.aws_open_search_service_domain_domain_endpoint_options_details
    import aws_sdk_securityhub.types.aws_open_search_service_domain_encryption_at_rest_options_details
    import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_options_details
    import aws_sdk_securityhub.types.aws_open_search_service_domain_node_to_node_encryption_options_details
    import aws_sdk_securityhub.types.aws_open_search_service_domain_service_software_options_details
    import aws_sdk_securityhub.types.aws_open_search_service_domain_vpc_options_details
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string


class AwsOpenSearchServiceDomainDetails(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the OpenSearch Service domain.</p>"""
    access_policies: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>IAM policy document that specifies the access policies for the OpenSearch Service domain.</p>"""
    domain_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the endpoint.</p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the domain.</p>"""
    domain_endpoint: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The domain endpoint.</p>"""
    engine_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the domain engine.</p>"""
    encryption_at_rest_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_encryption_at_rest_options_details.AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails"
    ]
    """<p>Details about the configuration for encryption at rest.</p>"""
    node_to_node_encryption_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_node_to_node_encryption_options_details.AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails"
    ]
    """<p>Details about the configuration for node-to-node encryption.</p>"""
    service_software_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_service_software_options_details.AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails"
    ]
    """<p>Information about the status of a domain relative to the latest service software.</p>"""
    cluster_config: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_details.AwsOpenSearchServiceDomainClusterConfigDetails"
    ]
    """<p>Details about the configuration of an OpenSearch cluster.</p>"""
    domain_endpoint_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_domain_endpoint_options_details.AwsOpenSearchServiceDomainDomainEndpointOptionsDetails"
    ]
    """<p>Additional options for the domain endpoint.</p>"""
    vpc_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_vpc_options_details.AwsOpenSearchServiceDomainVpcOptionsDetails"
    ]
    """<p>Information that OpenSearch Service derives based on <code>VPCOptions</code> for the domain.</p>"""
    log_publishing_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_options_details.AwsOpenSearchServiceDomainLogPublishingOptionsDetails"
    ]
    """<p>Configures the CloudWatch Logs to publish for the OpenSearch domain.</p>"""
    domain_endpoints: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>The domain endpoints. Used if the OpenSearch domain resides in a VPC.</p> <p>This is a map of key-value pairs. The key is always <code>vpc</code>. The value is the endpoint.</p>"""
    advanced_security_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_advanced_security_options_details.AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails"
    ]
    """<p>Specifies options for fine-grained access control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsOpenSearchServiceDomainDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "domain_endpoint" in value:
        out["DomainEndpoint"] = value["domain_endpoint"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "encryption_at_rest_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_encryption_at_rest_options_details

        out["EncryptionAtRestOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_encryption_at_rest_options_details.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_node_to_node_encryption_options_details

        out["NodeToNodeEncryptionOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_node_to_node_encryption_options_details.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "service_software_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_service_software_options_details

        out["ServiceSoftwareOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_service_software_options_details.serialize_json(
                value["service_software_options"]
            )
        )
    if "cluster_config" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_details

        out["ClusterConfig"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_details.serialize_json(
                value["cluster_config"]
            )
        )
    if "domain_endpoint_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_domain_endpoint_options_details

        out["DomainEndpointOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_domain_endpoint_options_details.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "vpc_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_vpc_options_details

        out["VpcOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_vpc_options_details.serialize_json(
                value["vpc_options"]
            )
        )
    if "log_publishing_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_options_details

        out["LogPublishingOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_options_details.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "domain_endpoints" in value:
        import aws_sdk_securityhub.types.field_map

        out["DomainEndpoints"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["domain_endpoints"]
        )
    if "advanced_security_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_advanced_security_options_details

        out["AdvancedSecurityOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_advanced_security_options_details.serialize_json(
                value["advanced_security_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsOpenSearchServiceDomainDetails:
    out: AwsOpenSearchServiceDomainDetails = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AccessPolicies" in data:
        out["access_policies"] = data["AccessPolicies"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "DomainEndpoint" in data:
        out["domain_endpoint"] = data["DomainEndpoint"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "EncryptionAtRestOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_encryption_at_rest_options_details

        out["encryption_at_rest_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_encryption_at_rest_options_details.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "NodeToNodeEncryptionOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_node_to_node_encryption_options_details

        out["node_to_node_encryption_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_node_to_node_encryption_options_details.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if "ServiceSoftwareOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_service_software_options_details

        out["service_software_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_service_software_options_details.deserialize_json(
                data["ServiceSoftwareOptions"]
            )
        )
    if "ClusterConfig" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_details

        out["cluster_config"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_details.deserialize_json(
                data["ClusterConfig"]
            )
        )
    if "DomainEndpointOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_domain_endpoint_options_details

        out["domain_endpoint_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_domain_endpoint_options_details.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if "VpcOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_vpc_options_details

        out["vpc_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_vpc_options_details.deserialize_json(
                data["VpcOptions"]
            )
        )
    if "LogPublishingOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_options_details

        out["log_publishing_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_log_publishing_options_details.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "DomainEndpoints" in data:
        import aws_sdk_securityhub.types.field_map

        out["domain_endpoints"] = aws_sdk_securityhub.types.field_map.deserialize_json(
            data["DomainEndpoints"]
        )
    if "AdvancedSecurityOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_advanced_security_options_details

        out["advanced_security_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_advanced_security_options_details.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    return out
