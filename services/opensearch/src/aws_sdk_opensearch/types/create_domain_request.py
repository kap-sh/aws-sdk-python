"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.advanced_options
    import aws_sdk_opensearch.types.advanced_security_options_input
    import aws_sdk_opensearch.types.aiml_options_input
    import aws_sdk_opensearch.types.auto_tune_options_input
    import aws_sdk_opensearch.types.automated_snapshot_pause_request_options
    import aws_sdk_opensearch.types.cluster_config
    import aws_sdk_opensearch.types.cognito_options
    import aws_sdk_opensearch.types.deployment_strategy_options
    import aws_sdk_opensearch.types.domain_endpoint_options
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.ebs_options
    import aws_sdk_opensearch.types.encryption_at_rest_options
    import aws_sdk_opensearch.types.identity_center_options_input
    import aws_sdk_opensearch.types.ip_address_type
    import aws_sdk_opensearch.types.log_publishing_options
    import aws_sdk_opensearch.types.node_to_node_encryption_options
    import aws_sdk_opensearch.types.off_peak_window_options
    import aws_sdk_opensearch.types.policy_document
    import aws_sdk_opensearch.types.snapshot_options
    import aws_sdk_opensearch.types.software_update_options
    import aws_sdk_opensearch.types.tag_list
    import aws_sdk_opensearch.types.version_string
    import aws_sdk_opensearch.types.vpc_options


class CreateDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>Name of the OpenSearch Service domain to create. Domain names are unique across the domains owned by an account within an Amazon Web Services Region.</p>"""
    engine_version: NotRequired["aws_sdk_opensearch.types.version_string.VersionString"]
    r"""<p>String of format Elasticsearch_X.Y or OpenSearch_X.Y to specify the engine version for the OpenSearch Service domain. For example, <code>OpenSearch_1.0</code> or <code>Elasticsearch_7.9</code>. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains\">Creating and managing Amazon OpenSearch Service domains</a>.</p>"""
    cluster_config: NotRequired["aws_sdk_opensearch.types.cluster_config.ClusterConfig"]
    """<p>Container for the cluster configuration of a domain.</p>"""
    ebs_options: NotRequired["aws_sdk_opensearch.types.ebs_options.EBSOptions"]
    """<p>Container for the parameters required to enable EBS-based storage for an OpenSearch Service domain.</p>"""
    access_policies: NotRequired[
        "aws_sdk_opensearch.types.policy_document.PolicyDocument"
    ]
    """<p>Identity and Access Management (IAM) policy document specifying the access policies for the new domain.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_opensearch.types.ip_address_type.IPAddressType"
    ]
    """<p>Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.</p>"""
    snapshot_options: NotRequired[
        "aws_sdk_opensearch.types.snapshot_options.SnapshotOptions"
    ]
    """<p>DEPRECATED. Container for the parameters required to configure automated snapshots of domain indexes.</p>"""
    vpc_options: NotRequired["aws_sdk_opensearch.types.vpc_options.VPCOptions"]
    r"""<p>Container for the values required to configure VPC access domains. If you don't specify these values, OpenSearch Service creates the domain with a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html\">Launching your Amazon OpenSearch Service domains using a VPC</a>.</p>"""
    cognito_options: NotRequired[
        "aws_sdk_opensearch.types.cognito_options.CognitoOptions"
    ]
    r"""<p>Key-value pairs to configure Amazon Cognito authentication. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html\">Configuring Amazon Cognito authentication for OpenSearch Dashboards</a>.</p>"""
    encryption_at_rest_options: NotRequired[
        "aws_sdk_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Key-value pairs to enable encryption at rest.</p>"""
    node_to_node_encryption_options: NotRequired[
        "aws_sdk_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    ]
    """<p>Enables node-to-node encryption.</p>"""
    advanced_options: NotRequired[
        "aws_sdk_opensearch.types.advanced_options.AdvancedOptions"
    ]
    r"""<p>Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:</p> <ul> <li> <p> <code>\"rest.action.multi.allow_explicit_index\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>\"indices.fielddata.cache.size\": \"80\" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>\"indices.query.bool.max_clause_count\": \"1024\"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> <li> <p> <code>\"override_main_response_version\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether the domain reports its version as 7.10 to allow Elasticsearch OSS clients and plugins to continue working with it. Default is false when creating a domain and true when upgrading a domain.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\">Advanced cluster parameters</a>.</p>"""
    log_publishing_options: NotRequired[
        "aws_sdk_opensearch.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Key-value pairs to configure log publishing.</p>"""
    domain_endpoint_options: NotRequired[
        "aws_sdk_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
    ]
    """<p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>"""
    advanced_security_options: NotRequired[
        "aws_sdk_opensearch.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
    ]
    """<p>Options for fine-grained access control.</p>"""
    identity_center_options: NotRequired[
        "aws_sdk_opensearch.types.identity_center_options_input.IdentityCenterOptionsInput"
    ]
    """<p>Configuration options for enabling and managing IAM Identity Center integration within a domain.</p>"""
    tag_list: NotRequired["aws_sdk_opensearch.types.tag_list.TagList"]
    """<p>List of tags to add to the domain upon creation.</p>"""
    auto_tune_options: NotRequired[
        "aws_sdk_opensearch.types.auto_tune_options_input.AutoTuneOptionsInput"
    ]
    """<p>Options for Auto-Tune.</p>"""
    off_peak_window_options: NotRequired[
        "aws_sdk_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
    ]
    """<p>Specifies a daily 10-hour time block during which OpenSearch Service can perform configuration changes on the domain, including service software updates and Auto-Tune enhancements that require a blue/green deployment. If no options are specified, the default start time of 10:00 P.M. local time (for the Region that the domain is created in) is used.</p>"""
    software_update_options: NotRequired[
        "aws_sdk_opensearch.types.software_update_options.SoftwareUpdateOptions"
    ]
    """<p>Software update options for the domain.</p>"""
    aiml_options: NotRequired[
        "aws_sdk_opensearch.types.aiml_options_input.AIMLOptionsInput"
    ]
    """<p>Options for all machine learning features for the specified domain.</p>"""
    deployment_strategy_options: NotRequired[
        "aws_sdk_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
    ]
    """<p>Specifies the deployment strategy options for the domain.</p>"""
    automated_snapshot_pause_options: NotRequired[
        "aws_sdk_opensearch.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
    ]
    """<p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "cluster_config" in value:
        import aws_sdk_opensearch.types.cluster_config

        out["ClusterConfig"] = aws_sdk_opensearch.types.cluster_config.serialize_json(
            value["cluster_config"]
        )
    if "ebs_options" in value:
        import aws_sdk_opensearch.types.ebs_options

        out["EBSOptions"] = aws_sdk_opensearch.types.ebs_options.serialize_json(
            value["ebs_options"]
        )
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "ip_address_type" in value:
        import aws_sdk_opensearch.types.ip_address_type

        out["IPAddressType"] = aws_sdk_opensearch.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "snapshot_options" in value:
        import aws_sdk_opensearch.types.snapshot_options

        out["SnapshotOptions"] = (
            aws_sdk_opensearch.types.snapshot_options.serialize_json(
                value["snapshot_options"]
            )
        )
    if "vpc_options" in value:
        import aws_sdk_opensearch.types.vpc_options

        out["VPCOptions"] = aws_sdk_opensearch.types.vpc_options.serialize_json(
            value["vpc_options"]
        )
    if "cognito_options" in value:
        import aws_sdk_opensearch.types.cognito_options

        out["CognitoOptions"] = aws_sdk_opensearch.types.cognito_options.serialize_json(
            value["cognito_options"]
        )
    if "encryption_at_rest_options" in value:
        import aws_sdk_opensearch.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            aws_sdk_opensearch.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import aws_sdk_opensearch.types.node_to_node_encryption_options

        out["NodeToNodeEncryptionOptions"] = (
            aws_sdk_opensearch.types.node_to_node_encryption_options.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "advanced_options" in value:
        import aws_sdk_opensearch.types.advanced_options

        out["AdvancedOptions"] = (
            aws_sdk_opensearch.types.advanced_options.serialize_json(
                value["advanced_options"]
            )
        )
    if "log_publishing_options" in value:
        import aws_sdk_opensearch.types.log_publishing_options

        out["LogPublishingOptions"] = (
            aws_sdk_opensearch.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "domain_endpoint_options" in value:
        import aws_sdk_opensearch.types.domain_endpoint_options

        out["DomainEndpointOptions"] = (
            aws_sdk_opensearch.types.domain_endpoint_options.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "advanced_security_options" in value:
        import aws_sdk_opensearch.types.advanced_security_options_input

        out["AdvancedSecurityOptions"] = (
            aws_sdk_opensearch.types.advanced_security_options_input.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "identity_center_options" in value:
        import aws_sdk_opensearch.types.identity_center_options_input

        out["IdentityCenterOptions"] = (
            aws_sdk_opensearch.types.identity_center_options_input.serialize_json(
                value["identity_center_options"]
            )
        )
    if "tag_list" in value:
        import aws_sdk_opensearch.types.tag_list

        out["TagList"] = aws_sdk_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    if "auto_tune_options" in value:
        import aws_sdk_opensearch.types.auto_tune_options_input

        out["AutoTuneOptions"] = (
            aws_sdk_opensearch.types.auto_tune_options_input.serialize_json(
                value["auto_tune_options"]
            )
        )
    if "off_peak_window_options" in value:
        import aws_sdk_opensearch.types.off_peak_window_options

        out["OffPeakWindowOptions"] = (
            aws_sdk_opensearch.types.off_peak_window_options.serialize_json(
                value["off_peak_window_options"]
            )
        )
    if "software_update_options" in value:
        import aws_sdk_opensearch.types.software_update_options

        out["SoftwareUpdateOptions"] = (
            aws_sdk_opensearch.types.software_update_options.serialize_json(
                value["software_update_options"]
            )
        )
    if "aiml_options" in value:
        import aws_sdk_opensearch.types.aiml_options_input

        out["AIMLOptions"] = aws_sdk_opensearch.types.aiml_options_input.serialize_json(
            value["aiml_options"]
        )
    if "deployment_strategy_options" in value:
        import aws_sdk_opensearch.types.deployment_strategy_options

        out["DeploymentStrategyOptions"] = (
            aws_sdk_opensearch.types.deployment_strategy_options.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "automated_snapshot_pause_options" in value:
        import aws_sdk_opensearch.types.automated_snapshot_pause_request_options

        out["AutomatedSnapshotPauseOptions"] = (
            aws_sdk_opensearch.types.automated_snapshot_pause_request_options.serialize_json(
                value["automated_snapshot_pause_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDomainRequest:
    out: CreateDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("CreateDomainRequest.domain_name required")
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "ClusterConfig" in data:
        import aws_sdk_opensearch.types.cluster_config

        out["cluster_config"] = (
            aws_sdk_opensearch.types.cluster_config.deserialize_json(
                data["ClusterConfig"]
            )
        )
    if "EBSOptions" in data:
        import aws_sdk_opensearch.types.ebs_options

        out["ebs_options"] = aws_sdk_opensearch.types.ebs_options.deserialize_json(
            data["EBSOptions"]
        )
    if "AccessPolicies" in data:
        out["access_policies"] = data["AccessPolicies"]
    if "IPAddressType" in data:
        import aws_sdk_opensearch.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_opensearch.types.ip_address_type.deserialize_json(
                data["IPAddressType"]
            )
        )
    if "SnapshotOptions" in data:
        import aws_sdk_opensearch.types.snapshot_options

        out["snapshot_options"] = (
            aws_sdk_opensearch.types.snapshot_options.deserialize_json(
                data["SnapshotOptions"]
            )
        )
    if "VPCOptions" in data:
        import aws_sdk_opensearch.types.vpc_options

        out["vpc_options"] = aws_sdk_opensearch.types.vpc_options.deserialize_json(
            data["VPCOptions"]
        )
    if "CognitoOptions" in data:
        import aws_sdk_opensearch.types.cognito_options

        out["cognito_options"] = (
            aws_sdk_opensearch.types.cognito_options.deserialize_json(
                data["CognitoOptions"]
            )
        )
    if "EncryptionAtRestOptions" in data:
        import aws_sdk_opensearch.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            aws_sdk_opensearch.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "NodeToNodeEncryptionOptions" in data:
        import aws_sdk_opensearch.types.node_to_node_encryption_options

        out["node_to_node_encryption_options"] = (
            aws_sdk_opensearch.types.node_to_node_encryption_options.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if "AdvancedOptions" in data:
        import aws_sdk_opensearch.types.advanced_options

        out["advanced_options"] = (
            aws_sdk_opensearch.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if "LogPublishingOptions" in data:
        import aws_sdk_opensearch.types.log_publishing_options

        out["log_publishing_options"] = (
            aws_sdk_opensearch.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "DomainEndpointOptions" in data:
        import aws_sdk_opensearch.types.domain_endpoint_options

        out["domain_endpoint_options"] = (
            aws_sdk_opensearch.types.domain_endpoint_options.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if "AdvancedSecurityOptions" in data:
        import aws_sdk_opensearch.types.advanced_security_options_input

        out["advanced_security_options"] = (
            aws_sdk_opensearch.types.advanced_security_options_input.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if "IdentityCenterOptions" in data:
        import aws_sdk_opensearch.types.identity_center_options_input

        out["identity_center_options"] = (
            aws_sdk_opensearch.types.identity_center_options_input.deserialize_json(
                data["IdentityCenterOptions"]
            )
        )
    if "TagList" in data:
        import aws_sdk_opensearch.types.tag_list

        out["tag_list"] = aws_sdk_opensearch.types.tag_list.deserialize_json(
            data["TagList"]
        )
    if "AutoTuneOptions" in data:
        import aws_sdk_opensearch.types.auto_tune_options_input

        out["auto_tune_options"] = (
            aws_sdk_opensearch.types.auto_tune_options_input.deserialize_json(
                data["AutoTuneOptions"]
            )
        )
    if "OffPeakWindowOptions" in data:
        import aws_sdk_opensearch.types.off_peak_window_options

        out["off_peak_window_options"] = (
            aws_sdk_opensearch.types.off_peak_window_options.deserialize_json(
                data["OffPeakWindowOptions"]
            )
        )
    if "SoftwareUpdateOptions" in data:
        import aws_sdk_opensearch.types.software_update_options

        out["software_update_options"] = (
            aws_sdk_opensearch.types.software_update_options.deserialize_json(
                data["SoftwareUpdateOptions"]
            )
        )
    if "AIMLOptions" in data:
        import aws_sdk_opensearch.types.aiml_options_input

        out["aiml_options"] = (
            aws_sdk_opensearch.types.aiml_options_input.deserialize_json(
                data["AIMLOptions"]
            )
        )
    if "DeploymentStrategyOptions" in data:
        import aws_sdk_opensearch.types.deployment_strategy_options

        out["deployment_strategy_options"] = (
            aws_sdk_opensearch.types.deployment_strategy_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if "AutomatedSnapshotPauseOptions" in data:
        import aws_sdk_opensearch.types.automated_snapshot_pause_request_options

        out["automated_snapshot_pause_options"] = (
            aws_sdk_opensearch.types.automated_snapshot_pause_request_options.deserialize_json(
                data["AutomatedSnapshotPauseOptions"]
            )
        )
    return out
