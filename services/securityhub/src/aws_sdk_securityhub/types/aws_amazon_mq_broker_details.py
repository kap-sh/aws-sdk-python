"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_encryption_options_details
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_details
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_users_list
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsAmazonMqBrokerDetails(TypedDict, closed=True):
    authentication_strategy: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The authentication strategy used to secure the broker. The default is <code>SIMPLE</code>. </p>"""
    auto_minor_version_upgrade: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Whether automatically upgrade new minor versions for brokers, as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window of the broker or after a manual broker reboot. </p>"""
    broker_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the broker. </p>"""
    broker_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The broker's name. </p>"""
    deployment_mode: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The broker's deployment mode. </p>"""
    encryption_options: NotRequired[
        "aws_sdk_securityhub.types.aws_amazon_mq_broker_encryption_options_details.AwsAmazonMqBrokerEncryptionOptionsDetails"
    ]
    """<p> Encryption options for the broker. Doesn’t apply to RabbitMQ brokers. </p>"""
    engine_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of broker engine. </p>"""
    engine_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The version of the broker engine. </p>"""
    host_instance_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The broker's instance type. </p>"""
    broker_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The unique ID that Amazon MQ generates for the broker. </p>"""
    ldap_server_metadata: NotRequired[
        "aws_sdk_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details.AwsAmazonMqBrokerLdapServerMetadataDetails"
    ]
    """<p> The metadata of the Lightweight Directory Access Protocol (LDAP) server used to authenticate and authorize connections to the broker. This is an optional failover server. </p>"""
    logs: NotRequired[
        "aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_details.AwsAmazonMqBrokerLogsDetails"
    ]
    """<p> Turns on Amazon CloudWatch logging for brokers. </p>"""
    maintenance_window_start_time: NotRequired[
        "aws_sdk_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details.AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails"
    ]
    """<p> The scheduled time period (UTC) during which Amazon MQ begins to apply pending updates or patches to the broker. </p>"""
    publicly_accessible: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Permits connections from applications outside of the VPC that hosts the broker's subnets. </p>"""
    security_groups: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> The list of rules (one minimum, 125 maximum) that authorize connections to brokers. </p>"""
    storage_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The broker's storage type. </p>"""
    subnet_ids: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p> The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. </p>"""
    users: NotRequired[
        "aws_sdk_securityhub.types.aws_amazon_mq_broker_users_list.AwsAmazonMqBrokerUsersList"
    ]
    """<p> The list of all broker usernames for the specified broker. Doesn't apply to RabbitMQ brokers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerDetails) -> dict:
    out: dict = {}
    if "authentication_strategy" in value:
        out["AuthenticationStrategy"] = value["authentication_strategy"]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "broker_arn" in value:
        out["BrokerArn"] = value["broker_arn"]
    if "broker_name" in value:
        out["BrokerName"] = value["broker_name"]
    if "deployment_mode" in value:
        out["DeploymentMode"] = value["deployment_mode"]
    if "encryption_options" in value:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_encryption_options_details

        out["EncryptionOptions"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_encryption_options_details.serialize_json(
                value["encryption_options"]
            )
        )
    if "engine_type" in value:
        out["EngineType"] = value["engine_type"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "host_instance_type" in value:
        out["HostInstanceType"] = value["host_instance_type"]
    if "broker_id" in value:
        out["BrokerId"] = value["broker_id"]
    if "ldap_server_metadata" in value:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details

        out["LdapServerMetadata"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details.serialize_json(
                value["ldap_server_metadata"]
            )
        )
    if "logs" in value:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_details

        out["Logs"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_details.serialize_json(
                value["logs"]
            )
        )
    if "maintenance_window_start_time" in value:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details

        out["MaintenanceWindowStartTime"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details.serialize_json(
                value["maintenance_window_start_time"]
            )
        )
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "security_groups" in value:
        import aws_sdk_securityhub.types.string_list

        out["SecurityGroups"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["security_groups"]
        )
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "subnet_ids" in value:
        import aws_sdk_securityhub.types.string_list

        out["SubnetIds"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "users" in value:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_users_list

        out["Users"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_users_list.serialize_json(
                value["users"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerDetails:
    out: AwsAmazonMqBrokerDetails = {}  # type: ignore[typeddict-item]
    if "AuthenticationStrategy" in data:
        out["authentication_strategy"] = data["AuthenticationStrategy"]
    if "AutoMinorVersionUpgrade" in data:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if "BrokerArn" in data:
        out["broker_arn"] = data["BrokerArn"]
    if "BrokerName" in data:
        out["broker_name"] = data["BrokerName"]
    if "DeploymentMode" in data:
        out["deployment_mode"] = data["DeploymentMode"]
    if "EncryptionOptions" in data:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_encryption_options_details

        out["encryption_options"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_encryption_options_details.deserialize_json(
                data["EncryptionOptions"]
            )
        )
    if "EngineType" in data:
        out["engine_type"] = data["EngineType"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "HostInstanceType" in data:
        out["host_instance_type"] = data["HostInstanceType"]
    if "BrokerId" in data:
        out["broker_id"] = data["BrokerId"]
    if "LdapServerMetadata" in data:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details

        out["ldap_server_metadata"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_ldap_server_metadata_details.deserialize_json(
                data["LdapServerMetadata"]
            )
        )
    if "Logs" in data:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_details

        out["logs"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_details.deserialize_json(
                data["Logs"]
            )
        )
    if "MaintenanceWindowStartTime" in data:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details

        out["maintenance_window_start_time"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_maintenance_window_start_time_details.deserialize_json(
                data["MaintenanceWindowStartTime"]
            )
        )
    if "PubliclyAccessible" in data:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if "SecurityGroups" in data:
        import aws_sdk_securityhub.types.string_list

        out["security_groups"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["SecurityGroups"]
        )
    if "StorageType" in data:
        out["storage_type"] = data["StorageType"]
    if "SubnetIds" in data:
        import aws_sdk_securityhub.types.string_list

        out["subnet_ids"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["SubnetIds"]
        )
    if "Users" in data:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_users_list

        out["users"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_users_list.deserialize_json(
                data["Users"]
            )
        )
    return out
