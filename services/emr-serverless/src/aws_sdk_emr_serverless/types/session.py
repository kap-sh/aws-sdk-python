"""Generated from Smithy shape ``com.amazonaws.emrserverless#Session``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.date
    import aws_sdk_emr_serverless.types.duration
    import aws_sdk_emr_serverless.types.iam_role_arn
    import aws_sdk_emr_serverless.types.network_configuration
    import aws_sdk_emr_serverless.types.release_label
    import aws_sdk_emr_serverless.types.request_identity_user_arn
    import aws_sdk_emr_serverless.types.resource_utilization
    import aws_sdk_emr_serverless.types.session_arn
    import aws_sdk_emr_serverless.types.session_configuration_overrides
    import aws_sdk_emr_serverless.types.session_id
    import aws_sdk_emr_serverless.types.session_state
    import aws_sdk_emr_serverless.types.string256
    import aws_sdk_emr_serverless.types.string1024
    import aws_sdk_emr_serverless.types.tag_map
    import aws_sdk_emr_serverless.types.total_resource_utilization


class Session(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application that the session belongs to.</p>"""
    session_id: "aws_sdk_emr_serverless.types.session_id.SessionId"
    """<p>The ID of the session.</p>"""
    arn: "aws_sdk_emr_serverless.types.session_arn.SessionArn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    name: NotRequired["aws_sdk_emr_serverless.types.string256.String256"]
    """<p>The optional name of the session.</p>"""
    state: "aws_sdk_emr_serverless.types.session_state.SessionState"
    """<p>The state of the session.</p>"""
    state_details: "aws_sdk_emr_serverless.types.string1024.String1024"
    """<p>Additional details about the current state of the session.</p>"""
    release_label: "aws_sdk_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release label associated with the session.</p>"""
    execution_role_arn: "aws_sdk_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the execution role for the session.</p>"""
    created_by: (
        "aws_sdk_emr_serverless.types.request_identity_user_arn.RequestIdentityUserArn"
    )
    """<p>The IAM principal that created the session.</p>"""
    created_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time that the session was created.</p>"""
    updated_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time that the session was last updated.</p>"""
    started_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time that the session moved to a running state.</p>"""
    ended_at: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time that the session was terminated or failed.</p>"""
    idle_since: NotRequired["aws_sdk_emr_serverless.types.date.Date"]
    """<p>The date and time that the session became idle.</p>"""
    configuration_overrides: NotRequired[
        "aws_sdk_emr_serverless.types.session_configuration_overrides.SessionConfigurationOverrides"
    ]
    """<p>The configuration overrides for the session, including runtime configuration properties.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for customer VPC connectivity for the session.</p>"""
    idle_timeout_minutes: NotRequired["aws_sdk_emr_serverless.types.duration.Duration"]
    """<p>The idle timeout in minutes for the session. After the session remains idle for this duration, it is automatically terminated.</p>"""
    tags: NotRequired["aws_sdk_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags assigned to the session.</p>"""
    total_resource_utilization: NotRequired[
        "aws_sdk_emr_serverless.types.total_resource_utilization.TotalResourceUtilization"
    ]
    """<p>The aggregate vCPU, memory, and storage resources used from the time the session starts to execute, until the time the session terminates, rounded up to the nearest second.</p>"""
    billed_resource_utilization: NotRequired[
        "aws_sdk_emr_serverless.types.resource_utilization.ResourceUtilization"
    ]
    """<p>The aggregate vCPU, memory, and storage that Amazon Web Services has billed for the session. The billed resources include a 1-minute minimum usage for workers, plus additional storage over 20 GB per worker. Note that billed resources do not include usage for idle pre-initialized workers.</p>"""
    total_execution_duration_seconds: NotRequired["int"]
    """<p>The total execution duration of the session in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Session) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["sessionId"] = value["session_id"]
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    out["state"] = value["state"]
    out["stateDetails"] = value["state_details"]
    out["releaseLabel"] = value["release_label"]
    out["executionRoleArn"] = value["execution_role_arn"]
    out["createdBy"] = value["created_by"]
    import aws_sdk_emr_serverless.types.date

    out["createdAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import aws_sdk_emr_serverless.types.date

    out["updatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    if "started_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["startedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_emr_serverless.types.date

        out["endedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["ended_at"]
        )
    if "idle_since" in value:
        import aws_sdk_emr_serverless.types.date

        out["idleSince"] = aws_sdk_emr_serverless.types.date.serialize_json(
            value["idle_since"]
        )
    if "configuration_overrides" in value:
        import aws_sdk_emr_serverless.types.session_configuration_overrides

        out["configurationOverrides"] = (
            aws_sdk_emr_serverless.types.session_configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_emr_serverless.types.network_configuration

        out["networkConfiguration"] = (
            aws_sdk_emr_serverless.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "idle_timeout_minutes" in value:
        out["idleTimeoutMinutes"] = value["idle_timeout_minutes"]
    if "tags" in value:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "total_resource_utilization" in value:
        import aws_sdk_emr_serverless.types.total_resource_utilization

        out["totalResourceUtilization"] = (
            aws_sdk_emr_serverless.types.total_resource_utilization.serialize_json(
                value["total_resource_utilization"]
            )
        )
    if "billed_resource_utilization" in value:
        import aws_sdk_emr_serverless.types.resource_utilization

        out["billedResourceUtilization"] = (
            aws_sdk_emr_serverless.types.resource_utilization.serialize_json(
                value["billed_resource_utilization"]
            )
        )
    if "total_execution_duration_seconds" in value:
        out["totalExecutionDurationSeconds"] = value["total_execution_duration_seconds"]
    return out


def deserialize_json(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("Session.application_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("Session.session_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Session.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("Session.state required")
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    else:
        raise DeserializationError("Session.state_details required")
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("Session.release_label required")
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("Session.execution_role_arn required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("Session.created_by required")
    if "createdAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Session.created_at required")
    if "updatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Session.updated_at required")
    if "startedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["started_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["ended_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["endedAt"]
        )
    if "idleSince" in data:
        import aws_sdk_emr_serverless.types.date

        out["idle_since"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["idleSince"]
        )
    if "configurationOverrides" in data:
        import aws_sdk_emr_serverless.types.session_configuration_overrides

        out["configuration_overrides"] = (
            aws_sdk_emr_serverless.types.session_configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if "networkConfiguration" in data:
        import aws_sdk_emr_serverless.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_emr_serverless.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "idleTimeoutMinutes" in data:
        out["idle_timeout_minutes"] = data["idleTimeoutMinutes"]
    if "tags" in data:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "totalResourceUtilization" in data:
        import aws_sdk_emr_serverless.types.total_resource_utilization

        out["total_resource_utilization"] = (
            aws_sdk_emr_serverless.types.total_resource_utilization.deserialize_json(
                data["totalResourceUtilization"]
            )
        )
    if "billedResourceUtilization" in data:
        import aws_sdk_emr_serverless.types.resource_utilization

        out["billed_resource_utilization"] = (
            aws_sdk_emr_serverless.types.resource_utilization.deserialize_json(
                data["billedResourceUtilization"]
            )
        )
    if "totalExecutionDurationSeconds" in data:
        out["total_execution_duration_seconds"] = data["totalExecutionDurationSeconds"]
    return out
