"""Generated from Smithy shape ``com.amazonaws.emr#Session``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.certificate_authority
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.iam_role_arn
    import aws_sdk_emr.types.long
    import aws_sdk_emr.types.session_id
    import aws_sdk_emr.types.session_monitoring_configuration
    import aws_sdk_emr.types.session_state
    import aws_sdk_emr.types.tag_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class Session(TypedDict, closed=True):
    id: NotRequired["aws_sdk_emr.types.session_id.SessionId"]
    """<p>The ID of the session.</p>"""
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster that the session belongs to.</p>"""
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the session, if one was provided at creation time.</p>"""
    arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    state: NotRequired["aws_sdk_emr.types.session_state.SessionState"]
    """<p>The current state of the session. Valid values are <code>SUBMITTED</code>, <code>STARTING</code>, <code>STARTED</code>, <code>IDLE</code>, <code>BUSY</code>, <code>TERMINATING</code>, <code>TERMINATED</code>, and <code>FAILED</code>.</p>"""
    state_change_reason: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>A human-readable message describing the most recent state change.</p>"""
    release_label: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Amazon EMR release label of the cluster that the session is running on.</p>"""
    execution_role_arn: NotRequired["aws_sdk_emr.types.iam_role_arn.IAMRoleArn"]
    """<p>The execution role ARN for the session. Amazon EMR uses this role to access Amazon Web Services resources on your behalf during session execution.</p>"""
    account_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Amazon Web Services account ID that owns the session.</p>"""
    created_at: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time that the session was created.</p>"""
    updated_at: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time that the session was last updated.</p>"""
    started_at: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time that the session entered the <code>STARTED</code> state.</p>"""
    ended_at: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time that the session was terminated or failed.</p>"""
    idle_since: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time that the session last entered the <code>IDLE</code> state.</p>"""
    engine_configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>The configuration overrides for the session. Only runtime configuration overrides are supported.</p>"""
    monitoring_configuration: NotRequired[
        "aws_sdk_emr.types.session_monitoring_configuration.SessionMonitoringConfiguration"
    ]
    """<p>The monitoring configuration for the session.</p>"""
    session_idle_timeout_in_minutes: NotRequired["aws_sdk_emr.types.long.Long"]
    """<p>The idle timeout, in minutes. If the session is idle for this duration, Amazon EMR automatically terminates it.</p>"""
    certificate_authority: NotRequired[
        "aws_sdk_emr.types.certificate_authority.CertificateAuthority"
    ]
    """<p>The certificate authority used to establish an mTLS connection to the Spark Connect server when connecting directly over VPC peering.</p>"""
    server_url: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Spark Connect server URL for the session. Use this URL with the <code>Credentials</code> returned by <code>GetSessionEndpoint</code> to connect directly to the session over VPC peering.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>The tags associated with the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "state" in value:
        import aws_sdk_emr.types.session_state

        out["State"] = aws_sdk_emr.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        out["StateChangeReason"] = value["state_change_reason"]
    if "release_label" in value:
        out["ReleaseLabel"] = value["release_label"]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_at" in value:
        import aws_sdk_emr.types.date

        out["CreatedAt"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_emr.types.date

        out["UpdatedAt"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "started_at" in value:
        import aws_sdk_emr.types.date

        out["StartedAt"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_emr.types.date

        out["EndedAt"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["ended_at"]
        )
    if "idle_since" in value:
        import aws_sdk_emr.types.date

        out["IdleSince"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["idle_since"]
        )
    if "engine_configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["EngineConfigurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["engine_configurations"]
            )
        )
    if "monitoring_configuration" in value:
        import aws_sdk_emr.types.session_monitoring_configuration

        out["MonitoringConfiguration"] = (
            aws_sdk_emr.types.session_monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "session_idle_timeout_in_minutes" in value:
        out["SessionIdleTimeoutInMinutes"] = value["session_idle_timeout_in_minutes"]
    if "certificate_authority" in value:
        import aws_sdk_emr.types.certificate_authority

        out["CertificateAuthority"] = (
            aws_sdk_emr.types.certificate_authority.serialize_aws_json_1_1(
                value["certificate_authority"]
            )
        )
    if "server_url" in value:
        out["ServerUrl"] = value["server_url"]
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "State" in data:
        import aws_sdk_emr.types.session_state

        out["state"] = aws_sdk_emr.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        out["state_change_reason"] = data["StateChangeReason"]
    if "ReleaseLabel" in data:
        out["release_label"] = data["ReleaseLabel"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CreatedAt" in data:
        import aws_sdk_emr.types.date

        out["created_at"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_emr.types.date

        out["updated_at"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if "StartedAt" in data:
        import aws_sdk_emr.types.date

        out["started_at"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["StartedAt"]
        )
    if "EndedAt" in data:
        import aws_sdk_emr.types.date

        out["ended_at"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["EndedAt"]
        )
    if "IdleSince" in data:
        import aws_sdk_emr.types.date

        out["idle_since"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["IdleSince"]
        )
    if "EngineConfigurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["engine_configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["EngineConfigurations"]
            )
        )
    if "MonitoringConfiguration" in data:
        import aws_sdk_emr.types.session_monitoring_configuration

        out["monitoring_configuration"] = (
            aws_sdk_emr.types.session_monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if "SessionIdleTimeoutInMinutes" in data:
        out["session_idle_timeout_in_minutes"] = data["SessionIdleTimeoutInMinutes"]
    if "CertificateAuthority" in data:
        import aws_sdk_emr.types.certificate_authority

        out["certificate_authority"] = (
            aws_sdk_emr.types.certificate_authority.deserialize_aws_json_1_1(
                data["CertificateAuthority"]
            )
        )
    if "ServerUrl" in data:
        out["server_url"] = data["ServerUrl"]
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
