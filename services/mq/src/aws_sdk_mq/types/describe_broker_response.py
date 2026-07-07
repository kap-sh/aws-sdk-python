"""Generated from Smithy shape ``com.amazonaws.mq#DescribeBrokerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.__list_of_action_required
    import aws_sdk_mq.types.__list_of_broker_instance
    import aws_sdk_mq.types.__list_of_user_summary
    import aws_sdk_mq.types.__map_of__string
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.__timestamp_iso8601
    import aws_sdk_mq.types.authentication_strategy
    import aws_sdk_mq.types.broker_state
    import aws_sdk_mq.types.broker_storage_type
    import aws_sdk_mq.types.configurations
    import aws_sdk_mq.types.data_replication_metadata_output
    import aws_sdk_mq.types.data_replication_mode
    import aws_sdk_mq.types.deployment_mode
    import aws_sdk_mq.types.encryption_options
    import aws_sdk_mq.types.engine_type
    import aws_sdk_mq.types.ldap_server_metadata_output
    import aws_sdk_mq.types.logs_summary
    import aws_sdk_mq.types.weekly_start_time


class DescribeBrokerResponse(TypedDict, closed=True):
    actions_required: NotRequired[
        "aws_sdk_mq.types.__list_of_action_required.__listOfActionRequired"
    ]
    """<p>Actions required for a broker.</p>"""
    authentication_strategy: NotRequired[
        "aws_sdk_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
    auto_minor_version_upgrade: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.</p>"""
    broker_arn: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker's Amazon Resource Name (ARN).</p>"""
    broker_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    broker_instances: NotRequired[
        "aws_sdk_mq.types.__list_of_broker_instance.__listOfBrokerInstance"
    ]
    """<p>A list of information about allocated brokers.</p>"""
    broker_name: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker's name. This value must be unique in your Amazon Web Services account account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.</p>"""
    broker_state: NotRequired["aws_sdk_mq.types.broker_state.BrokerState"]
    """<p>The broker's status.</p>"""
    configurations: NotRequired["aws_sdk_mq.types.configurations.Configurations"]
    """<p>The list of all revisions for the specified configuration.</p>"""
    created: NotRequired["aws_sdk_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The time when the broker was created.</p>"""
    deployment_mode: NotRequired["aws_sdk_mq.types.deployment_mode.DeploymentMode"]
    """<p>The broker's deployment mode.</p>"""
    encryption_options: NotRequired[
        "aws_sdk_mq.types.encryption_options.EncryptionOptions"
    ]
    """<p>Encryption options for the broker.</p>"""
    engine_type: NotRequired["aws_sdk_mq.types.engine_type.EngineType"]
    """<p>The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>"""
    engine_version: NotRequired["aws_sdk_mq.types.__string.__string"]
    r"""<p>The broker engine version. For more information, see the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html\">ActiveMQ version management</a> and the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html\">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    host_instance_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker's instance type.</p>"""
    ldap_server_metadata: NotRequired[
        "aws_sdk_mq.types.ldap_server_metadata_output.LdapServerMetadataOutput"
    ]
    """<p>The metadata of the LDAP server used to authenticate and authorize connections to the broker.</p>"""
    logs: NotRequired["aws_sdk_mq.types.logs_summary.LogsSummary"]
    """<p>The list of information about logs currently enabled and pending to be deployed for the specified broker.</p>"""
    maintenance_window_start_time: NotRequired[
        "aws_sdk_mq.types.weekly_start_time.WeeklyStartTime"
    ]
    """<p>The parameters that determine the WeeklyStartTime.</p>"""
    pending_authentication_strategy: NotRequired[
        "aws_sdk_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>The authentication strategy that will be applied when the broker is rebooted. The default is SIMPLE.</p>"""
    pending_engine_version: NotRequired["aws_sdk_mq.types.__string.__string"]
    r"""<p>The broker engine version to upgrade to. For more information, see the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html\">ActiveMQ version management</a> and the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html\">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    pending_host_instance_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    r"""<p>The broker's host instance type to upgrade to. For a list of supported instance types, see <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types\">Broker instance types</a>.</p>"""
    pending_ldap_server_metadata: NotRequired[
        "aws_sdk_mq.types.ldap_server_metadata_output.LdapServerMetadataOutput"
    ]
    """<p>The metadata of the LDAP server that will be used to authenticate and authorize connections to the broker after it is rebooted.</p>"""
    pending_security_groups: NotRequired[
        "aws_sdk_mq.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of pending security groups to authorize connections to brokers.</p>"""
    publicly_accessible: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables connections from applications outside of the VPC that hosts the broker's subnets.</p>"""
    security_groups: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.</p>"""
    storage_type: NotRequired["aws_sdk_mq.types.broker_storage_type.BrokerStorageType"]
    """<p>The broker's storage type.</p>"""
    subnet_ids: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones.</p>"""
    tags: NotRequired["aws_sdk_mq.types.__map_of__string.__mapOf__string"]
    """<p>The list of all tags associated with this broker.</p>"""
    users: NotRequired["aws_sdk_mq.types.__list_of_user_summary.__listOfUserSummary"]
    """<p>The list of all broker usernames for the specified broker.</p>"""
    data_replication_metadata: NotRequired[
        "aws_sdk_mq.types.data_replication_metadata_output.DataReplicationMetadataOutput"
    ]
    """<p>The replication details of the data replication-enabled broker. Only returned if dataReplicationMode is set to CRDR.</p>"""
    data_replication_mode: NotRequired[
        "aws_sdk_mq.types.data_replication_mode.DataReplicationMode"
    ]
    """<p>Describes whether this broker is a part of a data replication pair.</p>"""
    pending_data_replication_metadata: NotRequired[
        "aws_sdk_mq.types.data_replication_metadata_output.DataReplicationMetadataOutput"
    ]
    """<p>The pending replication details of the data replication-enabled broker. Only returned if pendingDataReplicationMode is set to CRDR.</p>"""
    pending_data_replication_mode: NotRequired[
        "aws_sdk_mq.types.data_replication_mode.DataReplicationMode"
    ]
    """<p>Describes whether this broker will be a part of a data replication pair after reboot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrokerResponse) -> dict:
    out: dict = {}
    if "actions_required" in value:
        import aws_sdk_mq.types.__list_of_action_required

        out["actionsRequired"] = (
            aws_sdk_mq.types.__list_of_action_required.serialize_json(
                value["actions_required"]
            )
        )
    if "authentication_strategy" in value:
        import aws_sdk_mq.types.authentication_strategy

        out["authenticationStrategy"] = (
            aws_sdk_mq.types.authentication_strategy.serialize_json(
                value["authentication_strategy"]
            )
        )
    if "auto_minor_version_upgrade" in value:
        out["autoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "broker_arn" in value:
        out["brokerArn"] = value["broker_arn"]
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "broker_instances" in value:
        import aws_sdk_mq.types.__list_of_broker_instance

        out["brokerInstances"] = (
            aws_sdk_mq.types.__list_of_broker_instance.serialize_json(
                value["broker_instances"]
            )
        )
    if "broker_name" in value:
        out["brokerName"] = value["broker_name"]
    if "broker_state" in value:
        import aws_sdk_mq.types.broker_state

        out["brokerState"] = aws_sdk_mq.types.broker_state.serialize_json(
            value["broker_state"]
        )
    if "configurations" in value:
        import aws_sdk_mq.types.configurations

        out["configurations"] = aws_sdk_mq.types.configurations.serialize_json(
            value["configurations"]
        )
    if "created" in value:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.serialize_json(
            value["created"]
        )
    if "deployment_mode" in value:
        import aws_sdk_mq.types.deployment_mode

        out["deploymentMode"] = aws_sdk_mq.types.deployment_mode.serialize_json(
            value["deployment_mode"]
        )
    if "encryption_options" in value:
        import aws_sdk_mq.types.encryption_options

        out["encryptionOptions"] = aws_sdk_mq.types.encryption_options.serialize_json(
            value["encryption_options"]
        )
    if "engine_type" in value:
        import aws_sdk_mq.types.engine_type

        out["engineType"] = aws_sdk_mq.types.engine_type.serialize_json(
            value["engine_type"]
        )
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "host_instance_type" in value:
        out["hostInstanceType"] = value["host_instance_type"]
    if "ldap_server_metadata" in value:
        import aws_sdk_mq.types.ldap_server_metadata_output

        out["ldapServerMetadata"] = (
            aws_sdk_mq.types.ldap_server_metadata_output.serialize_json(
                value["ldap_server_metadata"]
            )
        )
    if "logs" in value:
        import aws_sdk_mq.types.logs_summary

        out["logs"] = aws_sdk_mq.types.logs_summary.serialize_json(value["logs"])
    if "maintenance_window_start_time" in value:
        import aws_sdk_mq.types.weekly_start_time

        out["maintenanceWindowStartTime"] = (
            aws_sdk_mq.types.weekly_start_time.serialize_json(
                value["maintenance_window_start_time"]
            )
        )
    if "pending_authentication_strategy" in value:
        import aws_sdk_mq.types.authentication_strategy

        out["pendingAuthenticationStrategy"] = (
            aws_sdk_mq.types.authentication_strategy.serialize_json(
                value["pending_authentication_strategy"]
            )
        )
    if "pending_engine_version" in value:
        out["pendingEngineVersion"] = value["pending_engine_version"]
    if "pending_host_instance_type" in value:
        out["pendingHostInstanceType"] = value["pending_host_instance_type"]
    if "pending_ldap_server_metadata" in value:
        import aws_sdk_mq.types.ldap_server_metadata_output

        out["pendingLdapServerMetadata"] = (
            aws_sdk_mq.types.ldap_server_metadata_output.serialize_json(
                value["pending_ldap_server_metadata"]
            )
        )
    if "pending_security_groups" in value:
        import aws_sdk_mq.types.__list_of__string

        out["pendingSecurityGroups"] = (
            aws_sdk_mq.types.__list_of__string.serialize_json(
                value["pending_security_groups"]
            )
        )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "security_groups" in value:
        import aws_sdk_mq.types.__list_of__string

        out["securityGroups"] = aws_sdk_mq.types.__list_of__string.serialize_json(
            value["security_groups"]
        )
    if "storage_type" in value:
        import aws_sdk_mq.types.broker_storage_type

        out["storageType"] = aws_sdk_mq.types.broker_storage_type.serialize_json(
            value["storage_type"]
        )
    if "subnet_ids" in value:
        import aws_sdk_mq.types.__list_of__string

        out["subnetIds"] = aws_sdk_mq.types.__list_of__string.serialize_json(
            value["subnet_ids"]
        )
    if "tags" in value:
        import aws_sdk_mq.types.__map_of__string

        out["tags"] = aws_sdk_mq.types.__map_of__string.serialize_json(value["tags"])
    if "users" in value:
        import aws_sdk_mq.types.__list_of_user_summary

        out["users"] = aws_sdk_mq.types.__list_of_user_summary.serialize_json(
            value["users"]
        )
    if "data_replication_metadata" in value:
        import aws_sdk_mq.types.data_replication_metadata_output

        out["dataReplicationMetadata"] = (
            aws_sdk_mq.types.data_replication_metadata_output.serialize_json(
                value["data_replication_metadata"]
            )
        )
    if "data_replication_mode" in value:
        import aws_sdk_mq.types.data_replication_mode

        out["dataReplicationMode"] = (
            aws_sdk_mq.types.data_replication_mode.serialize_json(
                value["data_replication_mode"]
            )
        )
    if "pending_data_replication_metadata" in value:
        import aws_sdk_mq.types.data_replication_metadata_output

        out["pendingDataReplicationMetadata"] = (
            aws_sdk_mq.types.data_replication_metadata_output.serialize_json(
                value["pending_data_replication_metadata"]
            )
        )
    if "pending_data_replication_mode" in value:
        import aws_sdk_mq.types.data_replication_mode

        out["pendingDataReplicationMode"] = (
            aws_sdk_mq.types.data_replication_mode.serialize_json(
                value["pending_data_replication_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeBrokerResponse:
    out: DescribeBrokerResponse = {}  # type: ignore[typeddict-item]
    if "actionsRequired" in data:
        import aws_sdk_mq.types.__list_of_action_required

        out["actions_required"] = (
            aws_sdk_mq.types.__list_of_action_required.deserialize_json(
                data["actionsRequired"]
            )
        )
    if "authenticationStrategy" in data:
        import aws_sdk_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            aws_sdk_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if "autoMinorVersionUpgrade" in data:
        out["auto_minor_version_upgrade"] = data["autoMinorVersionUpgrade"]
    if "brokerArn" in data:
        out["broker_arn"] = data["brokerArn"]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    if "brokerInstances" in data:
        import aws_sdk_mq.types.__list_of_broker_instance

        out["broker_instances"] = (
            aws_sdk_mq.types.__list_of_broker_instance.deserialize_json(
                data["brokerInstances"]
            )
        )
    if "brokerName" in data:
        out["broker_name"] = data["brokerName"]
    if "brokerState" in data:
        import aws_sdk_mq.types.broker_state

        out["broker_state"] = aws_sdk_mq.types.broker_state.deserialize_json(
            data["brokerState"]
        )
    if "configurations" in data:
        import aws_sdk_mq.types.configurations

        out["configurations"] = aws_sdk_mq.types.configurations.deserialize_json(
            data["configurations"]
        )
    if "created" in data:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if "deploymentMode" in data:
        import aws_sdk_mq.types.deployment_mode

        out["deployment_mode"] = aws_sdk_mq.types.deployment_mode.deserialize_json(
            data["deploymentMode"]
        )
    if "encryptionOptions" in data:
        import aws_sdk_mq.types.encryption_options

        out["encryption_options"] = (
            aws_sdk_mq.types.encryption_options.deserialize_json(
                data["encryptionOptions"]
            )
        )
    if "engineType" in data:
        import aws_sdk_mq.types.engine_type

        out["engine_type"] = aws_sdk_mq.types.engine_type.deserialize_json(
            data["engineType"]
        )
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    if "hostInstanceType" in data:
        out["host_instance_type"] = data["hostInstanceType"]
    if "ldapServerMetadata" in data:
        import aws_sdk_mq.types.ldap_server_metadata_output

        out["ldap_server_metadata"] = (
            aws_sdk_mq.types.ldap_server_metadata_output.deserialize_json(
                data["ldapServerMetadata"]
            )
        )
    if "logs" in data:
        import aws_sdk_mq.types.logs_summary

        out["logs"] = aws_sdk_mq.types.logs_summary.deserialize_json(data["logs"])
    if "maintenanceWindowStartTime" in data:
        import aws_sdk_mq.types.weekly_start_time

        out["maintenance_window_start_time"] = (
            aws_sdk_mq.types.weekly_start_time.deserialize_json(
                data["maintenanceWindowStartTime"]
            )
        )
    if "pendingAuthenticationStrategy" in data:
        import aws_sdk_mq.types.authentication_strategy

        out["pending_authentication_strategy"] = (
            aws_sdk_mq.types.authentication_strategy.deserialize_json(
                data["pendingAuthenticationStrategy"]
            )
        )
    if "pendingEngineVersion" in data:
        out["pending_engine_version"] = data["pendingEngineVersion"]
    if "pendingHostInstanceType" in data:
        out["pending_host_instance_type"] = data["pendingHostInstanceType"]
    if "pendingLdapServerMetadata" in data:
        import aws_sdk_mq.types.ldap_server_metadata_output

        out["pending_ldap_server_metadata"] = (
            aws_sdk_mq.types.ldap_server_metadata_output.deserialize_json(
                data["pendingLdapServerMetadata"]
            )
        )
    if "pendingSecurityGroups" in data:
        import aws_sdk_mq.types.__list_of__string

        out["pending_security_groups"] = (
            aws_sdk_mq.types.__list_of__string.deserialize_json(
                data["pendingSecurityGroups"]
            )
        )
    if "publiclyAccessible" in data:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if "securityGroups" in data:
        import aws_sdk_mq.types.__list_of__string

        out["security_groups"] = aws_sdk_mq.types.__list_of__string.deserialize_json(
            data["securityGroups"]
        )
    if "storageType" in data:
        import aws_sdk_mq.types.broker_storage_type

        out["storage_type"] = aws_sdk_mq.types.broker_storage_type.deserialize_json(
            data["storageType"]
        )
    if "subnetIds" in data:
        import aws_sdk_mq.types.__list_of__string

        out["subnet_ids"] = aws_sdk_mq.types.__list_of__string.deserialize_json(
            data["subnetIds"]
        )
    if "tags" in data:
        import aws_sdk_mq.types.__map_of__string

        out["tags"] = aws_sdk_mq.types.__map_of__string.deserialize_json(data["tags"])
    if "users" in data:
        import aws_sdk_mq.types.__list_of_user_summary

        out["users"] = aws_sdk_mq.types.__list_of_user_summary.deserialize_json(
            data["users"]
        )
    if "dataReplicationMetadata" in data:
        import aws_sdk_mq.types.data_replication_metadata_output

        out["data_replication_metadata"] = (
            aws_sdk_mq.types.data_replication_metadata_output.deserialize_json(
                data["dataReplicationMetadata"]
            )
        )
    if "dataReplicationMode" in data:
        import aws_sdk_mq.types.data_replication_mode

        out["data_replication_mode"] = (
            aws_sdk_mq.types.data_replication_mode.deserialize_json(
                data["dataReplicationMode"]
            )
        )
    if "pendingDataReplicationMetadata" in data:
        import aws_sdk_mq.types.data_replication_metadata_output

        out["pending_data_replication_metadata"] = (
            aws_sdk_mq.types.data_replication_metadata_output.deserialize_json(
                data["pendingDataReplicationMetadata"]
            )
        )
    if "pendingDataReplicationMode" in data:
        import aws_sdk_mq.types.data_replication_mode

        out["pending_data_replication_mode"] = (
            aws_sdk_mq.types.data_replication_mode.deserialize_json(
                data["pendingDataReplicationMode"]
            )
        )
    return out
