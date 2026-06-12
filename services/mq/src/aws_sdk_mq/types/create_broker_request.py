"""Generated from Smithy shape ``com.amazonaws.mq#CreateBrokerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.__list_of_user
    import aws_sdk_mq.types.__map_of__string
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.authentication_strategy
    import aws_sdk_mq.types.broker_storage_type
    import aws_sdk_mq.types.configuration_id
    import aws_sdk_mq.types.data_replication_mode
    import aws_sdk_mq.types.deployment_mode
    import aws_sdk_mq.types.encryption_options
    import aws_sdk_mq.types.engine_type
    import aws_sdk_mq.types.ldap_server_metadata_input
    import aws_sdk_mq.types.logs
    import aws_sdk_mq.types.weekly_start_time


class CreateBrokerRequest(TypedDict):
    authentication_strategy: NotRequired[
        "aws_sdk_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
    auto_minor_version_upgrade: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. Set to true by default, if no value is specified.</p> <note><p>Must be set to true for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above.</p></note>"""
    broker_name: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The broker's name. This value must be unique in your Amazon Web Services account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.</p> <important><p>Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker names are not intended to be used for private or sensitive data.</p></important>"""
    configuration: NotRequired["aws_sdk_mq.types.configuration_id.ConfigurationId"]
    """<p>A list of information about the configuration.</p>"""
    creator_request_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action.</p> <note><p>We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the creatorRequestId if your application doesn't require idempotency.</p></note>"""
    deployment_mode: NotRequired["aws_sdk_mq.types.deployment_mode.DeploymentMode"]
    """<p>Required. The broker's deployment mode.</p>"""
    encryption_options: NotRequired[
        "aws_sdk_mq.types.encryption_options.EncryptionOptions"
    ]
    """<p>Encryption options for the broker.</p>"""
    engine_type: NotRequired["aws_sdk_mq.types.engine_type.EngineType"]
    """<p>Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>"""
    engine_version: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html\">ActiveMQ version management</a> and the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html\">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    host_instance_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The broker's instance type.</p>"""
    ldap_server_metadata: NotRequired[
        "aws_sdk_mq.types.ldap_server_metadata_input.LdapServerMetadataInput"
    ]
    """<p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.</p>"""
    logs: NotRequired["aws_sdk_mq.types.logs.Logs"]
    """<p>Enables Amazon CloudWatch logging for brokers.</p>"""
    maintenance_window_start_time: NotRequired[
        "aws_sdk_mq.types.weekly_start_time.WeeklyStartTime"
    ]
    """<p>The parameters that determine the WeeklyStartTime.</p>"""
    publicly_accessible: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables connections from applications outside of the VPC that hosts the broker's subnets. Set to false by default, if no value is provided.</p>"""
    security_groups: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.</p>"""
    storage_type: NotRequired["aws_sdk_mq.types.broker_storage_type.BrokerStorageType"]
    """<p>The broker's storage type.</p>"""
    subnet_ids: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ Amazon MQ for ActiveMQ deployment requires two subnets. A CLUSTER_MULTI_AZ Amazon MQ for RabbitMQ deployment has no subnet requirements when deployed with public accessibility. Deployment without public accessibility requires at least one subnet.</p> <important><p>If you specify subnets in a <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html\">shared VPC</a> for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your Amazon Web Services account. Amazon MQ will not be able to create VPC endpoints in VPCs that are not owned by your Amazon Web Services account.</p></important>"""
    tags: NotRequired["aws_sdk_mq.types.__map_of__string.__mapOf__string"]
    """<p>Create tags when creating the broker.</p>"""
    users: NotRequired["aws_sdk_mq.types.__list_of_user.__listOfUser"]
    """<p>The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, an administrative user is required if using simple authentication and authorization. For brokers using OAuth2, this user is optional. When provided, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.</p>"""
    data_replication_mode: NotRequired[
        "aws_sdk_mq.types.data_replication_mode.DataReplicationMode"
    ]
    """<p>Defines whether this broker is a part of a data replication pair.</p>"""
    data_replication_primary_broker_arn: NotRequired[
        "aws_sdk_mq.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the primary broker that is used to replicate data from in a data replication pair, and is applied to the replica broker. Must be set when dataReplicationMode is set to CRDR.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrokerRequest) -> dict:
    out: dict = {}
    if "authentication_strategy" in value:
        import aws_sdk_mq.types.authentication_strategy

        out["authenticationStrategy"] = (
            aws_sdk_mq.types.authentication_strategy.serialize_json(
                value["authentication_strategy"]
            )
        )
    if "auto_minor_version_upgrade" in value:
        out["autoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "broker_name" in value:
        out["brokerName"] = value["broker_name"]
    if "configuration" in value:
        import aws_sdk_mq.types.configuration_id

        out["configuration"] = aws_sdk_mq.types.configuration_id.serialize_json(
            value["configuration"]
        )
    if "creator_request_id" in value:
        out["creatorRequestId"] = value["creator_request_id"]
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
        import aws_sdk_mq.types.ldap_server_metadata_input

        out["ldapServerMetadata"] = (
            aws_sdk_mq.types.ldap_server_metadata_input.serialize_json(
                value["ldap_server_metadata"]
            )
        )
    if "logs" in value:
        import aws_sdk_mq.types.logs

        out["logs"] = aws_sdk_mq.types.logs.serialize_json(value["logs"])
    if "maintenance_window_start_time" in value:
        import aws_sdk_mq.types.weekly_start_time

        out["maintenanceWindowStartTime"] = (
            aws_sdk_mq.types.weekly_start_time.serialize_json(
                value["maintenance_window_start_time"]
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
        import aws_sdk_mq.types.__list_of_user

        out["users"] = aws_sdk_mq.types.__list_of_user.serialize_json(value["users"])
    if "data_replication_mode" in value:
        import aws_sdk_mq.types.data_replication_mode

        out["dataReplicationMode"] = (
            aws_sdk_mq.types.data_replication_mode.serialize_json(
                value["data_replication_mode"]
            )
        )
    if "data_replication_primary_broker_arn" in value:
        out["dataReplicationPrimaryBrokerArn"] = value[
            "data_replication_primary_broker_arn"
        ]
    return out


def deserialize_json(data: dict) -> CreateBrokerRequest:
    out: CreateBrokerRequest = {}  # type: ignore[typeddict-item]
    if "authenticationStrategy" in data:
        import aws_sdk_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            aws_sdk_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if "autoMinorVersionUpgrade" in data:
        out["auto_minor_version_upgrade"] = data["autoMinorVersionUpgrade"]
    if "brokerName" in data:
        out["broker_name"] = data["brokerName"]
    if "configuration" in data:
        import aws_sdk_mq.types.configuration_id

        out["configuration"] = aws_sdk_mq.types.configuration_id.deserialize_json(
            data["configuration"]
        )
    if "creatorRequestId" in data:
        out["creator_request_id"] = data["creatorRequestId"]
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
        import aws_sdk_mq.types.ldap_server_metadata_input

        out["ldap_server_metadata"] = (
            aws_sdk_mq.types.ldap_server_metadata_input.deserialize_json(
                data["ldapServerMetadata"]
            )
        )
    if "logs" in data:
        import aws_sdk_mq.types.logs

        out["logs"] = aws_sdk_mq.types.logs.deserialize_json(data["logs"])
    if "maintenanceWindowStartTime" in data:
        import aws_sdk_mq.types.weekly_start_time

        out["maintenance_window_start_time"] = (
            aws_sdk_mq.types.weekly_start_time.deserialize_json(
                data["maintenanceWindowStartTime"]
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
        import aws_sdk_mq.types.__list_of_user

        out["users"] = aws_sdk_mq.types.__list_of_user.deserialize_json(data["users"])
    if "dataReplicationMode" in data:
        import aws_sdk_mq.types.data_replication_mode

        out["data_replication_mode"] = (
            aws_sdk_mq.types.data_replication_mode.deserialize_json(
                data["dataReplicationMode"]
            )
        )
    if "dataReplicationPrimaryBrokerArn" in data:
        out["data_replication_primary_broker_arn"] = data[
            "dataReplicationPrimaryBrokerArn"
        ]
    return out
