"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateDomainConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.advanced_options
    import aws_sdk_opensearch.types.advanced_security_options_input
    import aws_sdk_opensearch.types.aiml_options_input
    import aws_sdk_opensearch.types.auto_tune_options
    import aws_sdk_opensearch.types.automated_snapshot_pause_request_options
    import aws_sdk_opensearch.types.cluster_config
    import aws_sdk_opensearch.types.cognito_options
    import aws_sdk_opensearch.types.deployment_strategy_options
    import aws_sdk_opensearch.types.domain_endpoint_options
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.dry_run
    import aws_sdk_opensearch.types.dry_run_mode
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
    import aws_sdk_opensearch.types.vpc_options


class UpdateDomainConfigRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain that you're updating.</p>"""
    cluster_config: NotRequired["aws_sdk_opensearch.types.cluster_config.ClusterConfig"]
    """<p>Changes that you want to make to the cluster configuration, such as the instance type and number of EC2 instances.</p>"""
    ebs_options: NotRequired["aws_sdk_opensearch.types.ebs_options.EBSOptions"]
    """<p>The type and size of the EBS volume to attach to instances in the domain.</p>"""
    snapshot_options: NotRequired[
        "aws_sdk_opensearch.types.snapshot_options.SnapshotOptions"
    ]
    """<p>Option to set the time, in UTC format, for the daily automated snapshot. Default value is <code>0</code> hours. </p>"""
    vpc_options: NotRequired["aws_sdk_opensearch.types.vpc_options.VPCOptions"]
    """<p>Options to specify the subnets and security groups for a VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html\">Launching your Amazon OpenSearch Service domains using a VPC</a>.</p>"""
    cognito_options: NotRequired[
        "aws_sdk_opensearch.types.cognito_options.CognitoOptions"
    ]
    """<p>Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.</p>"""
    advanced_options: NotRequired[
        "aws_sdk_opensearch.types.advanced_options.AdvancedOptions"
    ]
    """<p>Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:</p> <ul> <li> <p> <code>\"rest.action.multi.allow_explicit_index\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>\"indices.fielddata.cache.size\": \"80\" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>\"indices.query.bool.max_clause_count\": \"1024\"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\">Advanced cluster parameters</a>.</p>"""
    access_policies: NotRequired[
        "aws_sdk_opensearch.types.policy_document.PolicyDocument"
    ]
    """<p>Identity and Access Management (IAM) access policy as a JSON-formatted string.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_opensearch.types.ip_address_type.IPAddressType"
    ]
    """<p>Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If your IP address type is currently set to dual stack, you can't change it. </p>"""
    log_publishing_options: NotRequired[
        "aws_sdk_opensearch.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Options to publish OpenSearch logs to Amazon CloudWatch Logs.</p>"""
    encryption_at_rest_options: NotRequired[
        "aws_sdk_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Encryption at rest options for the domain.</p>"""
    domain_endpoint_options: NotRequired[
        "aws_sdk_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
    ]
    """<p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>"""
    node_to_node_encryption_options: NotRequired[
        "aws_sdk_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    ]
    """<p>Node-to-node encryption options for the domain.</p>"""
    advanced_security_options: NotRequired[
        "aws_sdk_opensearch.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
    ]
    """<p>Options for fine-grained access control.</p>"""
    identity_center_options: NotRequired[
        "aws_sdk_opensearch.types.identity_center_options_input.IdentityCenterOptionsInput"
    ]
    auto_tune_options: NotRequired[
        "aws_sdk_opensearch.types.auto_tune_options.AutoTuneOptions"
    ]
    """<p>Options for Auto-Tune.</p>"""
    dry_run: NotRequired["aws_sdk_opensearch.types.dry_run.DryRun"]
    """<p>This flag, when set to True, specifies whether the <code>UpdateDomain</code> request should return the results of a dry run analysis without actually applying the change. A dry run determines what type of deployment the update will cause.</p>"""
    dry_run_mode: NotRequired["aws_sdk_opensearch.types.dry_run_mode.DryRunMode"]
    """<p>The type of dry run to perform.</p> <ul> <li> <p> <code>Basic</code> only returns the type of deployment (blue/green or dynamic) that the update will cause.</p> </li> <li> <p> <code>Verbose</code> runs an additional check to validate the changes you're making. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#validation-check\">Validating a domain update</a>.</p> </li> </ul>"""
    off_peak_window_options: NotRequired[
        "aws_sdk_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
    ]
    """<p>Off-peak window options for the domain.</p>"""
    software_update_options: NotRequired[
        "aws_sdk_opensearch.types.software_update_options.SoftwareUpdateOptions"
    ]
    """<p>Service software update options for the domain.</p>"""
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
def serialize_json(value: UpdateDomainConfigRequest) -> dict:
    out: dict = {}
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
    if "advanced_options" in value:
        import aws_sdk_opensearch.types.advanced_options

        out["AdvancedOptions"] = (
            aws_sdk_opensearch.types.advanced_options.serialize_json(
                value["advanced_options"]
            )
        )
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "ip_address_type" in value:
        import aws_sdk_opensearch.types.ip_address_type

        out["IPAddressType"] = aws_sdk_opensearch.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "log_publishing_options" in value:
        import aws_sdk_opensearch.types.log_publishing_options

        out["LogPublishingOptions"] = (
            aws_sdk_opensearch.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "encryption_at_rest_options" in value:
        import aws_sdk_opensearch.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            aws_sdk_opensearch.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "domain_endpoint_options" in value:
        import aws_sdk_opensearch.types.domain_endpoint_options

        out["DomainEndpointOptions"] = (
            aws_sdk_opensearch.types.domain_endpoint_options.serialize_json(
                value["domain_endpoint_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import aws_sdk_opensearch.types.node_to_node_encryption_options

        out["NodeToNodeEncryptionOptions"] = (
            aws_sdk_opensearch.types.node_to_node_encryption_options.serialize_json(
                value["node_to_node_encryption_options"]
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
    if "auto_tune_options" in value:
        import aws_sdk_opensearch.types.auto_tune_options

        out["AutoTuneOptions"] = (
            aws_sdk_opensearch.types.auto_tune_options.serialize_json(
                value["auto_tune_options"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "dry_run_mode" in value:
        import aws_sdk_opensearch.types.dry_run_mode

        out["DryRunMode"] = aws_sdk_opensearch.types.dry_run_mode.serialize_json(
            value["dry_run_mode"]
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


def deserialize_json(data: dict) -> UpdateDomainConfigRequest:
    out: UpdateDomainConfigRequest = {}  # type: ignore[typeddict-item]
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
    if "AdvancedOptions" in data:
        import aws_sdk_opensearch.types.advanced_options

        out["advanced_options"] = (
            aws_sdk_opensearch.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
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
    if "LogPublishingOptions" in data:
        import aws_sdk_opensearch.types.log_publishing_options

        out["log_publishing_options"] = (
            aws_sdk_opensearch.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "EncryptionAtRestOptions" in data:
        import aws_sdk_opensearch.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            aws_sdk_opensearch.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "DomainEndpointOptions" in data:
        import aws_sdk_opensearch.types.domain_endpoint_options

        out["domain_endpoint_options"] = (
            aws_sdk_opensearch.types.domain_endpoint_options.deserialize_json(
                data["DomainEndpointOptions"]
            )
        )
    if "NodeToNodeEncryptionOptions" in data:
        import aws_sdk_opensearch.types.node_to_node_encryption_options

        out["node_to_node_encryption_options"] = (
            aws_sdk_opensearch.types.node_to_node_encryption_options.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
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
    if "AutoTuneOptions" in data:
        import aws_sdk_opensearch.types.auto_tune_options

        out["auto_tune_options"] = (
            aws_sdk_opensearch.types.auto_tune_options.deserialize_json(
                data["AutoTuneOptions"]
            )
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    if "DryRunMode" in data:
        import aws_sdk_opensearch.types.dry_run_mode

        out["dry_run_mode"] = aws_sdk_opensearch.types.dry_run_mode.deserialize_json(
            data["DryRunMode"]
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
