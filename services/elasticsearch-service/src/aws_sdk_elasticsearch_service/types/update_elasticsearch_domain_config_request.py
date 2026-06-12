"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdateElasticsearchDomainConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.advanced_options
    import aws_sdk_elasticsearch_service.types.advanced_security_options_input
    import aws_sdk_elasticsearch_service.types.auto_tune_options
    import aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options
    import aws_sdk_elasticsearch_service.types.cognito_options
    import aws_sdk_elasticsearch_service.types.deployment_strategy_options
    import aws_sdk_elasticsearch_service.types.domain_endpoint_options
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.dry_run
    import aws_sdk_elasticsearch_service.types.ebs_options
    import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config
    import aws_sdk_elasticsearch_service.types.encryption_at_rest_options
    import aws_sdk_elasticsearch_service.types.log_publishing_options
    import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options
    import aws_sdk_elasticsearch_service.types.policy_document
    import aws_sdk_elasticsearch_service.types.snapshot_options
    import aws_sdk_elasticsearch_service.types.vpc_options


class UpdateElasticsearchDomainConfigRequest(TypedDict):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the Elasticsearch domain that you are updating. </p>"""
    elasticsearch_cluster_config: NotRequired[
        "aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
    ]
    """<p>The type and number of instances to instantiate for the domain cluster.</p>"""
    ebs_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.ebs_options.EBSOptions"
    ]
    """<p>Specify the type and size of the EBS volume that you want to use. </p>"""
    snapshot_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.snapshot_options.SnapshotOptions"
    ]
    """<p>Option to set the time, in UTC format, for the daily automated snapshot. Default value is <code>0</code> hours. </p>"""
    vpc_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.vpc_options.VPCOptions"
    ]
    """<p>Options to specify the subnets and security groups for VPC endpoint. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc\" target=\"_blank\">Creating a VPC</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i></p>"""
    cognito_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.cognito_options.CognitoOptions"
    ]
    """<p>Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html\" target=\"_blank\">Amazon Cognito Authentication for Kibana</a>.</p>"""
    advanced_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.advanced_options.AdvancedOptions"
    ]
    """<p>Modifies the advanced option to allow references to indices in an HTTP request body. Must be <code>false</code> when configuring access to individual sub-resources. By default, the value is <code>true</code>. See <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options\" target=\"_blank\">Configuration Advanced Options</a> for more information.</p>"""
    access_policies: NotRequired[
        "aws_sdk_elasticsearch_service.types.policy_document.PolicyDocument"
    ]
    """<p>IAM access policy as a JSON-formatted string.</p>"""
    log_publishing_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Map of <code>LogType</code> and <code>LogPublishingOption</code>, each containing options to publish a given type of Elasticsearch log.</p>"""
    domain_endpoint_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_endpoint_options.DomainEndpointOptions"
    ]
    """<p>Options to specify configuration that will be applied to the domain endpoint.</p>"""
    advanced_security_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
    ]
    """<p>Specifies advanced security options.</p>"""
    node_to_node_encryption_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    ]
    """<p>Specifies the NodeToNodeEncryptionOptions.</p>"""
    encryption_at_rest_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Specifies the Encryption At Rest Options.</p>"""
    auto_tune_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.auto_tune_options.AutoTuneOptions"
    ]
    """<p>Specifies Auto-Tune options.</p>"""
    dry_run: NotRequired["aws_sdk_elasticsearch_service.types.dry_run.DryRun"]
    """<p> This flag, when set to True, specifies whether the <code>UpdateElasticsearchDomain</code> request should return the results of validation checks without actually applying the change. This flag, when set to True, specifies the deployment mechanism through which the update shall be applied on the domain. This will not actually perform the Update. </p>"""
    deployment_strategy_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
    ]
    """<p>Specifies the deployment strategy options.</p>"""
    automated_snapshot_pause_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
    ]
    """<p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateElasticsearchDomainConfigRequest) -> dict:
    out: dict = {}
    if "elasticsearch_cluster_config" in value:
        import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config

        out["ElasticsearchClusterConfig"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.serialize_json(
                value["elasticsearch_cluster_config"]
            )
        )
    if "ebs_options" in value:
        import aws_sdk_elasticsearch_service.types.ebs_options

        out["EBSOptions"] = (
            aws_sdk_elasticsearch_service.types.ebs_options.serialize_json(
                value["ebs_options"]
            )
        )
    if "snapshot_options" in value:
        import aws_sdk_elasticsearch_service.types.snapshot_options

        out["SnapshotOptions"] = (
            aws_sdk_elasticsearch_service.types.snapshot_options.serialize_json(
                value["snapshot_options"]
            )
        )
    if "vpc_options" in value:
        import aws_sdk_elasticsearch_service.types.vpc_options

        out["VPCOptions"] = (
            aws_sdk_elasticsearch_service.types.vpc_options.serialize_json(
                value["vpc_options"]
            )
        )
    if "cognito_options" in value:
        import aws_sdk_elasticsearch_service.types.cognito_options

        out["CognitoOptions"] = (
            aws_sdk_elasticsearch_service.types.cognito_options.serialize_json(
                value["cognito_options"]
            )
        )
    if "advanced_options" in value:
        import aws_sdk_elasticsearch_service.types.advanced_options

        out["AdvancedOptions"] = (
            aws_sdk_elasticsearch_service.types.advanced_options.serialize_json(
                value["advanced_options"]
            )
        )
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "log_publishing_options" in value:
        import aws_sdk_elasticsearch_service.types.log_publishing_options

        out["LogPublishingOptions"] = (
            aws_sdk_elasticsearch_service.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "domain_endpoint_options" in value:
        import aws_sdk_elasticsearch_service.types.domain_endpoint_options

        out["DomainEndpointOptions"] = (
            aws_sdk_elasticsearch_service.types.domain_endpoint_options.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "advanced_security_options" in value:
        import aws_sdk_elasticsearch_service.types.advanced_security_options_input

        out["AdvancedSecurityOptions"] = (
            aws_sdk_elasticsearch_service.types.advanced_security_options_input.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options

        out["NodeToNodeEncryptionOptions"] = (
            aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "encryption_at_rest_options" in value:
        import aws_sdk_elasticsearch_service.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            aws_sdk_elasticsearch_service.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "auto_tune_options" in value:
        import aws_sdk_elasticsearch_service.types.auto_tune_options

        out["AutoTuneOptions"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_options.serialize_json(
                value["auto_tune_options"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "deployment_strategy_options" in value:
        import aws_sdk_elasticsearch_service.types.deployment_strategy_options

        out["DeploymentStrategyOptions"] = (
            aws_sdk_elasticsearch_service.types.deployment_strategy_options.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "automated_snapshot_pause_options" in value:
        import aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options

        out["AutomatedSnapshotPauseOptions"] = (
            aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options.serialize_json(
                value["automated_snapshot_pause_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateElasticsearchDomainConfigRequest:
    out: UpdateElasticsearchDomainConfigRequest = {}  # type: ignore[typeddict-item]
    if "ElasticsearchClusterConfig" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config

        out["elasticsearch_cluster_config"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.deserialize_json(
                data["ElasticsearchClusterConfig"]
            )
        )
    if "EBSOptions" in data:
        import aws_sdk_elasticsearch_service.types.ebs_options

        out["ebs_options"] = (
            aws_sdk_elasticsearch_service.types.ebs_options.deserialize_json(
                data["EBSOptions"]
            )
        )
    if "SnapshotOptions" in data:
        import aws_sdk_elasticsearch_service.types.snapshot_options

        out["snapshot_options"] = (
            aws_sdk_elasticsearch_service.types.snapshot_options.deserialize_json(
                data["SnapshotOptions"]
            )
        )
    if "VPCOptions" in data:
        import aws_sdk_elasticsearch_service.types.vpc_options

        out["vpc_options"] = (
            aws_sdk_elasticsearch_service.types.vpc_options.deserialize_json(
                data["VPCOptions"]
            )
        )
    if "CognitoOptions" in data:
        import aws_sdk_elasticsearch_service.types.cognito_options

        out["cognito_options"] = (
            aws_sdk_elasticsearch_service.types.cognito_options.deserialize_json(
                data["CognitoOptions"]
            )
        )
    if "AdvancedOptions" in data:
        import aws_sdk_elasticsearch_service.types.advanced_options

        out["advanced_options"] = (
            aws_sdk_elasticsearch_service.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if "AccessPolicies" in data:
        out["access_policies"] = data["AccessPolicies"]
    if "LogPublishingOptions" in data:
        import aws_sdk_elasticsearch_service.types.log_publishing_options

        out["log_publishing_options"] = (
            aws_sdk_elasticsearch_service.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "DomainEndpointOptions" in data:
        import aws_sdk_elasticsearch_service.types.domain_endpoint_options

        out["domain_endpoint_options"] = (
            aws_sdk_elasticsearch_service.types.domain_endpoint_options.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if "AdvancedSecurityOptions" in data:
        import aws_sdk_elasticsearch_service.types.advanced_security_options_input

        out["advanced_security_options"] = (
            aws_sdk_elasticsearch_service.types.advanced_security_options_input.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if "NodeToNodeEncryptionOptions" in data:
        import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options

        out["node_to_node_encryption_options"] = (
            aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if "EncryptionAtRestOptions" in data:
        import aws_sdk_elasticsearch_service.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            aws_sdk_elasticsearch_service.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "AutoTuneOptions" in data:
        import aws_sdk_elasticsearch_service.types.auto_tune_options

        out["auto_tune_options"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_options.deserialize_json(
                data["AutoTuneOptions"]
            )
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    if "DeploymentStrategyOptions" in data:
        import aws_sdk_elasticsearch_service.types.deployment_strategy_options

        out["deployment_strategy_options"] = (
            aws_sdk_elasticsearch_service.types.deployment_strategy_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if "AutomatedSnapshotPauseOptions" in data:
        import aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options

        out["automated_snapshot_pause_options"] = (
            aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options.deserialize_json(
                data["AutomatedSnapshotPauseOptions"]
            )
        )
    return out
