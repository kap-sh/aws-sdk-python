"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchDomainStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.advanced_options
    import aws_sdk_elasticsearch_service.types.advanced_security_options
    import aws_sdk_elasticsearch_service.types.arn
    import aws_sdk_elasticsearch_service.types.auto_tune_options_output
    import aws_sdk_elasticsearch_service.types.automated_snapshot_pause_options
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.change_progress_details
    import aws_sdk_elasticsearch_service.types.cognito_options
    import aws_sdk_elasticsearch_service.types.deployment_strategy_options
    import aws_sdk_elasticsearch_service.types.domain_endpoint_options
    import aws_sdk_elasticsearch_service.types.domain_id
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.domain_processing_status_type
    import aws_sdk_elasticsearch_service.types.ebs_options
    import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config
    import aws_sdk_elasticsearch_service.types.elasticsearch_version_string
    import aws_sdk_elasticsearch_service.types.encryption_at_rest_options
    import aws_sdk_elasticsearch_service.types.endpoints_map
    import aws_sdk_elasticsearch_service.types.log_publishing_options
    import aws_sdk_elasticsearch_service.types.modifying_properties_list
    import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options
    import aws_sdk_elasticsearch_service.types.policy_document
    import aws_sdk_elasticsearch_service.types.service_software_options
    import aws_sdk_elasticsearch_service.types.service_url
    import aws_sdk_elasticsearch_service.types.snapshot_options
    import aws_sdk_elasticsearch_service.types.vpc_derived_info


class ElasticsearchDomainStatus(TypedDict):
    domain_id: "aws_sdk_elasticsearch_service.types.domain_id.DomainId"
    """<p>The unique identifier for the specified Elasticsearch domain.</p>"""
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).</p>"""
    arn: "aws_sdk_elasticsearch_service.types.arn.ARN"
    r"""<p>The Amazon resource name (ARN) of an Elasticsearch domain. See <a href=\"http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html\" target=\"_blank\">Identifiers for IAM Entities</a> in <i>Using AWS Identity and Access Management</i> for more information.</p>"""
    created: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>The domain creation status. <code>True</code> if the creation of an Elasticsearch domain is complete. <code>False</code> if domain creation is still in progress.</p>"""
    deleted: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>The domain deletion status. <code>True</code> if a delete request has been received for the domain but resource cleanup is still in progress. <code>False</code> if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.</p>"""
    endpoint: NotRequired["aws_sdk_elasticsearch_service.types.service_url.ServiceUrl"]
    """<p>The Elasticsearch domain endpoint that you use to submit index and search requests.</p>"""
    endpoints: NotRequired[
        "aws_sdk_elasticsearch_service.types.endpoints_map.EndpointsMap"
    ]
    """<p>Map containing the Elasticsearch domain endpoints used to submit index and search requests. Example <code>key, value</code>: <code>'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'</code>.</p>"""
    processing: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>The status of the Elasticsearch domain configuration. <code>True</code> if Amazon Elasticsearch Service is processing configuration changes. <code>False</code> if the configuration is active.</p>"""
    upgrade_processing: NotRequired[
        "aws_sdk_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>The status of an Elasticsearch domain version upgrade. <code>True</code> if Amazon Elasticsearch Service is undergoing a version upgrade. <code>False</code> if the configuration is active.</p>"""
    elasticsearch_version: NotRequired[
        "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    ]
    elasticsearch_cluster_config: "aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
    """<p>The type and number of instances in the domain cluster.</p>"""
    ebs_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.ebs_options.EBSOptions"
    ]
    r"""<p>The <code>EBSOptions</code> for the specified domain. See <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs\" target=\"_blank\">Configuring EBS-based Storage</a> for more information.</p>"""
    access_policies: NotRequired[
        "aws_sdk_elasticsearch_service.types.policy_document.PolicyDocument"
    ]
    """<p> IAM access policy as a JSON-formatted string.</p>"""
    snapshot_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.snapshot_options.SnapshotOptions"
    ]
    """<p>Specifies the status of the <code>SnapshotOptions</code></p>"""
    vpc_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.vpc_derived_info.VPCDerivedInfo"
    ]
    r"""<p>The <code>VPCOptions</code> for the specified domain. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html\" target=\"_blank\">VPC Endpoints for Amazon Elasticsearch Service Domains</a>.</p>"""
    cognito_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.cognito_options.CognitoOptions"
    ]
    r"""<p>The <code>CognitoOptions</code> for the specified domain. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html\" target=\"_blank\">Amazon Cognito Authentication for Kibana</a>.</p>"""
    encryption_at_rest_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p> Specifies the status of the <code>EncryptionAtRestOptions</code>.</p>"""
    node_to_node_encryption_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    ]
    """<p>Specifies the status of the <code>NodeToNodeEncryptionOptions</code>.</p>"""
    advanced_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.advanced_options.AdvancedOptions"
    ]
    """<p>Specifies the status of the <code>AdvancedOptions</code></p>"""
    log_publishing_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Log publishing options for the given domain.</p>"""
    service_software_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.service_software_options.ServiceSoftwareOptions"
    ]
    """<p>The current status of the Elasticsearch domain's service software.</p>"""
    domain_endpoint_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_endpoint_options.DomainEndpointOptions"
    ]
    """<p>The current status of the Elasticsearch domain's endpoint options.</p>"""
    advanced_security_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.advanced_security_options.AdvancedSecurityOptions"
    ]
    """<p>The current status of the Elasticsearch domain's advanced security options.</p>"""
    auto_tune_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.auto_tune_options_output.AutoTuneOptionsOutput"
    ]
    """<p>The current status of the Elasticsearch domain's Auto-Tune options.</p>"""
    change_progress_details: NotRequired[
        "aws_sdk_elasticsearch_service.types.change_progress_details.ChangeProgressDetails"
    ]
    """<p>Specifies change details of the domain configuration change.</p>"""
    domain_processing_status: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_processing_status_type.DomainProcessingStatusType"
    ]
    """<p>The status of any changes that are currently in progress for the domain.</p>"""
    modifying_properties: NotRequired[
        "aws_sdk_elasticsearch_service.types.modifying_properties_list.ModifyingPropertiesList"
    ]
    """<p>Information about the domain properties that are currently being modified.</p>"""
    deployment_strategy_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
    ]
    """<p>The current status of the Elasticsearch domain's deployment strategy options.</p>"""
    automated_snapshot_pause_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.automated_snapshot_pause_options.AutomatedSnapshotPauseOptions"
    ]
    """<p>The current status of the Elasticsearch domain's automated snapshot pause options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchDomainStatus) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["DomainName"] = value["domain_name"]
    out["ARN"] = value["arn"]
    if "created" in value:
        out["Created"] = value["created"]
    if "deleted" in value:
        out["Deleted"] = value["deleted"]
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "endpoints" in value:
        import aws_sdk_elasticsearch_service.types.endpoints_map

        out["Endpoints"] = (
            aws_sdk_elasticsearch_service.types.endpoints_map.serialize_json(
                value["endpoints"]
            )
        )
    if "processing" in value:
        out["Processing"] = value["processing"]
    if "upgrade_processing" in value:
        out["UpgradeProcessing"] = value["upgrade_processing"]
    if "elasticsearch_version" in value:
        out["ElasticsearchVersion"] = value["elasticsearch_version"]
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
    if "access_policies" in value:
        out["AccessPolicies"] = value["access_policies"]
    if "snapshot_options" in value:
        import aws_sdk_elasticsearch_service.types.snapshot_options

        out["SnapshotOptions"] = (
            aws_sdk_elasticsearch_service.types.snapshot_options.serialize_json(
                value["snapshot_options"]
            )
        )
    if "vpc_options" in value:
        import aws_sdk_elasticsearch_service.types.vpc_derived_info

        out["VPCOptions"] = (
            aws_sdk_elasticsearch_service.types.vpc_derived_info.serialize_json(
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
    if "encryption_at_rest_options" in value:
        import aws_sdk_elasticsearch_service.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            aws_sdk_elasticsearch_service.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "node_to_node_encryption_options" in value:
        import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options

        out["NodeToNodeEncryptionOptions"] = (
            aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.serialize_json(
                value["node_to_node_encryption_options"]
            )
        )
    if "advanced_options" in value:
        import aws_sdk_elasticsearch_service.types.advanced_options

        out["AdvancedOptions"] = (
            aws_sdk_elasticsearch_service.types.advanced_options.serialize_json(
                value["advanced_options"]
            )
        )
    if "log_publishing_options" in value:
        import aws_sdk_elasticsearch_service.types.log_publishing_options

        out["LogPublishingOptions"] = (
            aws_sdk_elasticsearch_service.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "service_software_options" in value:
        import aws_sdk_elasticsearch_service.types.service_software_options

        out["ServiceSoftwareOptions"] = (
            aws_sdk_elasticsearch_service.types.service_software_options.serialize_json(
                value["service_software_options"]
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
        import aws_sdk_elasticsearch_service.types.advanced_security_options

        out["AdvancedSecurityOptions"] = (
            aws_sdk_elasticsearch_service.types.advanced_security_options.serialize_json(
                value["advanced_security_options"]
            )
        )
    if "auto_tune_options" in value:
        import aws_sdk_elasticsearch_service.types.auto_tune_options_output

        out["AutoTuneOptions"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_options_output.serialize_json(
                value["auto_tune_options"]
            )
        )
    if "change_progress_details" in value:
        import aws_sdk_elasticsearch_service.types.change_progress_details

        out["ChangeProgressDetails"] = (
            aws_sdk_elasticsearch_service.types.change_progress_details.serialize_json(
                value["change_progress_details"]
            )
        )
    if "domain_processing_status" in value:
        import aws_sdk_elasticsearch_service.types.domain_processing_status_type

        out["DomainProcessingStatus"] = (
            aws_sdk_elasticsearch_service.types.domain_processing_status_type.serialize_json(
                value["domain_processing_status"]
            )
        )
    if "modifying_properties" in value:
        import aws_sdk_elasticsearch_service.types.modifying_properties_list

        out["ModifyingProperties"] = (
            aws_sdk_elasticsearch_service.types.modifying_properties_list.serialize_json(
                value["modifying_properties"]
            )
        )
    if "deployment_strategy_options" in value:
        import aws_sdk_elasticsearch_service.types.deployment_strategy_options

        out["DeploymentStrategyOptions"] = (
            aws_sdk_elasticsearch_service.types.deployment_strategy_options.serialize_json(
                value["deployment_strategy_options"]
            )
        )
    if "automated_snapshot_pause_options" in value:
        import aws_sdk_elasticsearch_service.types.automated_snapshot_pause_options

        out["AutomatedSnapshotPauseOptions"] = (
            aws_sdk_elasticsearch_service.types.automated_snapshot_pause_options.serialize_json(
                value["automated_snapshot_pause_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElasticsearchDomainStatus:
    out: ElasticsearchDomainStatus = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("ElasticsearchDomainStatus.domain_id required")
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("ElasticsearchDomainStatus.domain_name required")
    if "ARN" in data:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("ElasticsearchDomainStatus.arn required")
    if "Created" in data:
        out["created"] = data["Created"]
    if "Deleted" in data:
        out["deleted"] = data["Deleted"]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "Endpoints" in data:
        import aws_sdk_elasticsearch_service.types.endpoints_map

        out["endpoints"] = (
            aws_sdk_elasticsearch_service.types.endpoints_map.deserialize_json(
                data["Endpoints"]
            )
        )
    if "Processing" in data:
        out["processing"] = data["Processing"]
    if "UpgradeProcessing" in data:
        out["upgrade_processing"] = data["UpgradeProcessing"]
    if "ElasticsearchVersion" in data:
        out["elasticsearch_version"] = data["ElasticsearchVersion"]
    if "ElasticsearchClusterConfig" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config

        out["elasticsearch_cluster_config"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.deserialize_json(
                data["ElasticsearchClusterConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ElasticsearchDomainStatus.elasticsearch_cluster_config required"
        )
    if "EBSOptions" in data:
        import aws_sdk_elasticsearch_service.types.ebs_options

        out["ebs_options"] = (
            aws_sdk_elasticsearch_service.types.ebs_options.deserialize_json(
                data["EBSOptions"]
            )
        )
    if "AccessPolicies" in data:
        out["access_policies"] = data["AccessPolicies"]
    if "SnapshotOptions" in data:
        import aws_sdk_elasticsearch_service.types.snapshot_options

        out["snapshot_options"] = (
            aws_sdk_elasticsearch_service.types.snapshot_options.deserialize_json(
                data["SnapshotOptions"]
            )
        )
    if "VPCOptions" in data:
        import aws_sdk_elasticsearch_service.types.vpc_derived_info

        out["vpc_options"] = (
            aws_sdk_elasticsearch_service.types.vpc_derived_info.deserialize_json(
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
    if "EncryptionAtRestOptions" in data:
        import aws_sdk_elasticsearch_service.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            aws_sdk_elasticsearch_service.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "NodeToNodeEncryptionOptions" in data:
        import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options

        out["node_to_node_encryption_options"] = (
            aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.deserialize_json(
                data["NodeToNodeEncryptionOptions"]
            )
        )
    if "AdvancedOptions" in data:
        import aws_sdk_elasticsearch_service.types.advanced_options

        out["advanced_options"] = (
            aws_sdk_elasticsearch_service.types.advanced_options.deserialize_json(
                data["AdvancedOptions"]
            )
        )
    if "LogPublishingOptions" in data:
        import aws_sdk_elasticsearch_service.types.log_publishing_options

        out["log_publishing_options"] = (
            aws_sdk_elasticsearch_service.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "ServiceSoftwareOptions" in data:
        import aws_sdk_elasticsearch_service.types.service_software_options

        out["service_software_options"] = (
            aws_sdk_elasticsearch_service.types.service_software_options.deserialize_json(
                data["ServiceSoftwareOptions"]
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
        import aws_sdk_elasticsearch_service.types.advanced_security_options

        out["advanced_security_options"] = (
            aws_sdk_elasticsearch_service.types.advanced_security_options.deserialize_json(
                data["AdvancedSecurityOptions"]
            )
        )
    if "AutoTuneOptions" in data:
        import aws_sdk_elasticsearch_service.types.auto_tune_options_output

        out["auto_tune_options"] = (
            aws_sdk_elasticsearch_service.types.auto_tune_options_output.deserialize_json(
                data["AutoTuneOptions"]
            )
        )
    if "ChangeProgressDetails" in data:
        import aws_sdk_elasticsearch_service.types.change_progress_details

        out["change_progress_details"] = (
            aws_sdk_elasticsearch_service.types.change_progress_details.deserialize_json(
                data["ChangeProgressDetails"]
            )
        )
    if "DomainProcessingStatus" in data:
        import aws_sdk_elasticsearch_service.types.domain_processing_status_type

        out["domain_processing_status"] = (
            aws_sdk_elasticsearch_service.types.domain_processing_status_type.deserialize_json(
                data["DomainProcessingStatus"]
            )
        )
    if "ModifyingProperties" in data:
        import aws_sdk_elasticsearch_service.types.modifying_properties_list

        out["modifying_properties"] = (
            aws_sdk_elasticsearch_service.types.modifying_properties_list.deserialize_json(
                data["ModifyingProperties"]
            )
        )
    if "DeploymentStrategyOptions" in data:
        import aws_sdk_elasticsearch_service.types.deployment_strategy_options

        out["deployment_strategy_options"] = (
            aws_sdk_elasticsearch_service.types.deployment_strategy_options.deserialize_json(
                data["DeploymentStrategyOptions"]
            )
        )
    if "AutomatedSnapshotPauseOptions" in data:
        import aws_sdk_elasticsearch_service.types.automated_snapshot_pause_options

        out["automated_snapshot_pause_options"] = (
            aws_sdk_elasticsearch_service.types.automated_snapshot_pause_options.deserialize_json(
                data["AutomatedSnapshotPauseOptions"]
            )
        )
    return out
