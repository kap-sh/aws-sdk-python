"""Generated from Smithy shape ``com.amazonaws.mq#UpdateBrokerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__boolean
    import aws_sdk_mq.types.__list_of__string
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.authentication_strategy
    import aws_sdk_mq.types.configuration_id
    import aws_sdk_mq.types.data_replication_metadata_output
    import aws_sdk_mq.types.data_replication_mode
    import aws_sdk_mq.types.ldap_server_metadata_output
    import aws_sdk_mq.types.logs
    import aws_sdk_mq.types.weekly_start_time


class UpdateBrokerResponse(TypedDict):
    authentication_strategy: NotRequired[
        "aws_sdk_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
    auto_minor_version_upgrade: NotRequired["aws_sdk_mq.types.__boolean.__boolean"]
    """<p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.</p>"""
    broker_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The unique ID that Amazon MQ generates for the broker.</p>"""
    configuration: NotRequired["aws_sdk_mq.types.configuration_id.ConfigurationId"]
    """<p>The ID of the updated configuration.</p>"""
    engine_version: NotRequired["aws_sdk_mq.types.__string.__string"]
    r"""<p>The broker engine version to upgrade to. For more information, see the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html\">ActiveMQ version management</a> and the <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html\">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    host_instance_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    r"""<p>The broker's host instance type to upgrade to. For a list of supported instance types, see <a href=\"https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types\">Broker instance types</a>.</p>"""
    ldap_server_metadata: NotRequired[
        "aws_sdk_mq.types.ldap_server_metadata_output.LdapServerMetadataOutput"
    ]
    """<p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.</p>"""
    logs: NotRequired["aws_sdk_mq.types.logs.Logs"]
    """<p>The list of information about logs to be enabled for the specified broker.</p>"""
    maintenance_window_start_time: NotRequired[
        "aws_sdk_mq.types.weekly_start_time.WeeklyStartTime"
    ]
    """<p>The parameters that determine the WeeklyStartTime.</p>"""
    security_groups: NotRequired["aws_sdk_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of security groups (1 minimum, 5 maximum) that authorizes connections to brokers.</p>"""
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
def serialize_json(value: UpdateBrokerResponse) -> dict:
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
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "configuration" in value:
        import aws_sdk_mq.types.configuration_id

        out["configuration"] = aws_sdk_mq.types.configuration_id.serialize_json(
            value["configuration"]
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
        import aws_sdk_mq.types.logs

        out["logs"] = aws_sdk_mq.types.logs.serialize_json(value["logs"])
    if "maintenance_window_start_time" in value:
        import aws_sdk_mq.types.weekly_start_time

        out["maintenanceWindowStartTime"] = (
            aws_sdk_mq.types.weekly_start_time.serialize_json(
                value["maintenance_window_start_time"]
            )
        )
    if "security_groups" in value:
        import aws_sdk_mq.types.__list_of__string

        out["securityGroups"] = aws_sdk_mq.types.__list_of__string.serialize_json(
            value["security_groups"]
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


def deserialize_json(data: dict) -> UpdateBrokerResponse:
    out: UpdateBrokerResponse = {}  # type: ignore[typeddict-item]
    if "authenticationStrategy" in data:
        import aws_sdk_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            aws_sdk_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if "autoMinorVersionUpgrade" in data:
        out["auto_minor_version_upgrade"] = data["autoMinorVersionUpgrade"]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    if "configuration" in data:
        import aws_sdk_mq.types.configuration_id

        out["configuration"] = aws_sdk_mq.types.configuration_id.deserialize_json(
            data["configuration"]
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
        import aws_sdk_mq.types.logs

        out["logs"] = aws_sdk_mq.types.logs.deserialize_json(data["logs"])
    if "maintenanceWindowStartTime" in data:
        import aws_sdk_mq.types.weekly_start_time

        out["maintenance_window_start_time"] = (
            aws_sdk_mq.types.weekly_start_time.deserialize_json(
                data["maintenanceWindowStartTime"]
            )
        )
    if "securityGroups" in data:
        import aws_sdk_mq.types.__list_of__string

        out["security_groups"] = aws_sdk_mq.types.__list_of__string.deserialize_json(
            data["securityGroups"]
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
