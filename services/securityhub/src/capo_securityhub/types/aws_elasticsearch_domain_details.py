"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elasticsearch_domain_domain_endpoint_options
    import capo_securityhub.types.aws_elasticsearch_domain_elasticsearch_cluster_config_details
    import capo_securityhub.types.aws_elasticsearch_domain_encryption_at_rest_options
    import capo_securityhub.types.aws_elasticsearch_domain_log_publishing_options
    import capo_securityhub.types.aws_elasticsearch_domain_node_to_node_encryption_options
    import capo_securityhub.types.aws_elasticsearch_domain_service_software_options
    import capo_securityhub.types.aws_elasticsearch_domain_vpc_options
    import capo_securityhub.types.field_map
    import capo_securityhub.types.non_empty_string


class AwsElasticsearchDomainDetails(TypedDict, closed=True):
    access_policies: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>IAM policy document specifying the access policies for the new Elasticsearch domain.</p>"""
    domain_endpoint_options: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_domain_endpoint_options.AwsElasticsearchDomainDomainEndpointOptions"
    ]
    """<p>Additional options for the domain endpoint.</p>"""
    domain_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Unique identifier for an Elasticsearch domain.</p>"""
    domain_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Name of an Elasticsearch domain.</p> <p>Domain names are unique across all domains owned by the same account within an Amazon Web Services Region.</p> <p>Domain names must start with a lowercase letter and must be between 3 and 28 characters.</p> <p>Valid characters are a-z (lowercase only), 0-9, and – (hyphen). </p>"""
    endpoint: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Domain-specific endpoint used to submit index, search, and data upload requests to an Elasticsearch domain.</p> <p>The endpoint is a service URL. </p>"""
    endpoints: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p>The key-value pair that exists if the Elasticsearch domain uses VPC endpoints.</p>"""
    elasticsearch_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>OpenSearch version.</p>"""
    elasticsearch_cluster_config: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_elasticsearch_cluster_config_details.AwsElasticsearchDomainElasticsearchClusterConfigDetails"
    ]
    """<p>Information about an OpenSearch cluster configuration.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_encryption_at_rest_options.AwsElasticsearchDomainEncryptionAtRestOptions"
    ]
    """<p>Details about the configuration for encryption at rest.</p>"""
    log_publishing_options: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_log_publishing_options.AwsElasticsearchDomainLogPublishingOptions"
    ]
    """<p>Configures the CloudWatch Logs to publish for the Elasticsearch domain.</p>"""
    node_to_node_encryption_options: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_node_to_node_encryption_options.AwsElasticsearchDomainNodeToNodeEncryptionOptions"
    ]
    """<p>Details about the configuration for node-to-node encryption.</p>"""
    service_software_options: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_service_software_options.AwsElasticsearchDomainServiceSoftwareOptions"
    ]
    """<p>Information about the status of a domain relative to the latest service software.</p>"""
    vpc_options: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_vpc_options.AwsElasticsearchDomainVPCOptions"
    ]
    """<p>Information that OpenSearch derives based on <code>VPCOptions</code> for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticsearchDomainDetails) -> dict:
    out: dict = {}
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "domain_endpoint_options" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_domain_endpoint_options

        out["DomainEndpointOptions"] = (
            capo_securityhub.types.aws_elasticsearch_domain_domain_endpoint_options.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "endpoints" in value:
        import capo_securityhub.types.field_map

        out["Endpoints"] = capo_securityhub.types.field_map.serialize_json(
            value["endpoints"]
        )
    if "elasticsearch_version" in value:
        out["ElasticsearchVersion"] = value["elasticsearch_version"]
    if "elasticsearch_cluster_config" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_elasticsearch_cluster_config_details

        out["ElasticsearchClusterConfig"] = (
            capo_securityhub.types.aws_elasticsearch_domain_elasticsearch_cluster_config_details.serialize_json(
                value["elasticsearch_cluster_config"]
            )
        )
    if "encryption_at_rest_options" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            capo_securityhub.types.aws_elasticsearch_domain_encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "log_publishing_options" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_log_publishing_options

        out["LogPublishingOptions"] = (
            capo_securityhub.types.aws_elasticsearch_domain_log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_node_to_node_encryption_options

        out["NodeToNodeEncryptionOptions"] = (
            capo_securityhub.types.aws_elasticsearch_domain_node_to_node_encryption_options.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "service_software_options" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_service_software_options

        out["ServiceSoftwareOptions"] = (
            capo_securityhub.types.aws_elasticsearch_domain_service_software_options.serialize_json(
                value["service_software_options"]
            )
        )
    if "vpc_options" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_vpc_options

        out["VPCOptions"] = (
            capo_securityhub.types.aws_elasticsearch_domain_vpc_options.serialize_json(
                value["vpc_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsElasticsearchDomainDetails:
    out: AwsElasticsearchDomainDetails = {}  # type: ignore[typeddict-item]
    if "AccessPolicies" in data:
        out["access_policies"] = data["AccessPolicies"]
    if "DomainEndpointOptions" in data:
        import capo_securityhub.types.aws_elasticsearch_domain_domain_endpoint_options

        out["domain_endpoint_options"] = (
            capo_securityhub.types.aws_elasticsearch_domain_domain_endpoint_options.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "Endpoints" in data:
        import capo_securityhub.types.field_map

        out["endpoints"] = capo_securityhub.types.field_map.deserialize_json(
            data["Endpoints"]
        )
    if "ElasticsearchVersion" in data:
        out["elasticsearch_version"] = data["ElasticsearchVersion"]
    if "ElasticsearchClusterConfig" in data:
        import capo_securityhub.types.aws_elasticsearch_domain_elasticsearch_cluster_config_details

        out["elasticsearch_cluster_config"] = (
            capo_securityhub.types.aws_elasticsearch_domain_elasticsearch_cluster_config_details.deserialize_json(
                data["ElasticsearchClusterConfig"]
            )
        )
    if "EncryptionAtRestOptions" in data:
        import capo_securityhub.types.aws_elasticsearch_domain_encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            capo_securityhub.types.aws_elasticsearch_domain_encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "LogPublishingOptions" in data:
        import capo_securityhub.types.aws_elasticsearch_domain_log_publishing_options

        out["log_publishing_options"] = (
            capo_securityhub.types.aws_elasticsearch_domain_log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "NodeToNodeEncryptionOptions" in data:
        import capo_securityhub.types.aws_elasticsearch_domain_node_to_node_encryption_options

        out["node_to_node_encryption_options"] = (
            capo_securityhub.types.aws_elasticsearch_domain_node_to_node_encryption_options.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if "ServiceSoftwareOptions" in data:
        import capo_securityhub.types.aws_elasticsearch_domain_service_software_options

        out["service_software_options"] = (
            capo_securityhub.types.aws_elasticsearch_domain_service_software_options.deserialize_json(
                data["ServiceSoftwareOptions"]
            )
        )
    if "VPCOptions" in data:
        import capo_securityhub.types.aws_elasticsearch_domain_vpc_options

        out["vpc_options"] = (
            capo_securityhub.types.aws_elasticsearch_domain_vpc_options.deserialize_json(
                data["VPCOptions"]
            )
        )
    return out
