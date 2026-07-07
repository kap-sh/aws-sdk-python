"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.dev_environment_repository_summaries
    import aws_sdk_codecatalyst.types.dev_environment_status
    import aws_sdk_codecatalyst.types.ides
    import aws_sdk_codecatalyst.types.inactivity_timeout_minutes
    import aws_sdk_codecatalyst.types.instance_type
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.persistent_storage
    import aws_sdk_codecatalyst.types.status_reason
    import aws_sdk_codecatalyst.types.timestamp
    import aws_sdk_codecatalyst.types.uuid


class DevEnvironmentSummary(TypedDict, closed=True):
    space_name: NotRequired["aws_sdk_codecatalyst.types.name_string.NameString"]
    """<p>The name of the space.</p>"""
    project_name: NotRequired["aws_sdk_codecatalyst.types.name_string.NameString"]
    """<p>The name of the project in the space.</p>"""
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID for the Dev Environment. </p>"""
    last_updated_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The time when the Dev Environment was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    creator_id: "str"
    """<p>The system-generated unique ID of the user who created the Dev Environment. </p>"""
    status: "aws_sdk_codecatalyst.types.dev_environment_status.DevEnvironmentStatus"
    """<p>The status of the Dev Environment. </p>"""
    status_reason: NotRequired["aws_sdk_codecatalyst.types.status_reason.StatusReason"]
    """<p>The reason for the status.</p>"""
    repositories: "aws_sdk_codecatalyst.types.dev_environment_repository_summaries.DevEnvironmentRepositorySummaries"
    """<p>Information about the repositories that will be cloned into the Dev Environment. If no rvalue is specified, no repository is cloned.</p>"""
    alias: NotRequired["str"]
    """<p>The user-specified alias for the Dev Environment.</p>"""
    ides: NotRequired["aws_sdk_codecatalyst.types.ides.Ides"]
    """<p>Information about the integrated development environment (IDE) configured for a Dev Environment.</p>"""
    instance_type: "aws_sdk_codecatalyst.types.instance_type.InstanceType"
    """<p>The Amazon EC2 instace type used for the Dev Environment. </p>"""
    inactivity_timeout_minutes: (
        "aws_sdk_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
    )
    """<p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Dev Environments consume compute minutes when running.</p>"""
    persistent_storage: (
        "aws_sdk_codecatalyst.types.persistent_storage.PersistentStorage"
    )
    """<p>Information about the configuration of persistent storage for the Dev Environment.</p>"""
    vpc_connection_name: NotRequired[
        "aws_sdk_codecatalyst.types.name_string.NameString"
    ]
    """<p>The name of the connection used to connect to Amazon VPC used when the Dev Environment was created, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentSummary) -> dict:
    out: dict = {}
    if "space_name" in value:
        out["spaceName"] = value["space_name"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    import aws_sdk_codecatalyst.types.timestamp

    out["lastUpdatedTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    out["creatorId"] = value["creator_id"]
    out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import aws_sdk_codecatalyst.types.dev_environment_repository_summaries

    out["repositories"] = (
        aws_sdk_codecatalyst.types.dev_environment_repository_summaries.serialize_json(
            value["repositories"]
        )
    )
    if "alias" in value:
        out["alias"] = value["alias"]
    if "ides" in value:
        import aws_sdk_codecatalyst.types.ides

        out["ides"] = aws_sdk_codecatalyst.types.ides.serialize_json(value["ides"])
    out["instanceType"] = value["instance_type"]
    out["inactivityTimeoutMinutes"] = value.get("inactivity_timeout_minutes", 0)
    import aws_sdk_codecatalyst.types.persistent_storage

    out["persistentStorage"] = (
        aws_sdk_codecatalyst.types.persistent_storage.serialize_json(
            value["persistent_storage"]
        )
    )
    if "vpc_connection_name" in value:
        out["vpcConnectionName"] = value["vpc_connection_name"]
    return out


def deserialize_json(data: dict) -> DevEnvironmentSummary:
    out: DevEnvironmentSummary = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DevEnvironmentSummary.id required")
    if "lastUpdatedTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_codecatalyst.types.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("DevEnvironmentSummary.last_updated_time required")
    if "creatorId" in data:
        out["creator_id"] = data["creatorId"]
    else:
        raise DeserializationError("DevEnvironmentSummary.creator_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("DevEnvironmentSummary.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "repositories" in data:
        import aws_sdk_codecatalyst.types.dev_environment_repository_summaries

        out["repositories"] = (
            aws_sdk_codecatalyst.types.dev_environment_repository_summaries.deserialize_json(
                data["repositories"]
            )
        )
    else:
        raise DeserializationError("DevEnvironmentSummary.repositories required")
    if "alias" in data:
        out["alias"] = data["alias"]
    if "ides" in data:
        import aws_sdk_codecatalyst.types.ides

        out["ides"] = aws_sdk_codecatalyst.types.ides.deserialize_json(data["ides"])
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("DevEnvironmentSummary.instance_type required")
    if "inactivityTimeoutMinutes" in data:
        out["inactivity_timeout_minutes"] = data["inactivityTimeoutMinutes"]
    else:
        out["inactivity_timeout_minutes"] = 0
    if "persistentStorage" in data:
        import aws_sdk_codecatalyst.types.persistent_storage

        out["persistent_storage"] = (
            aws_sdk_codecatalyst.types.persistent_storage.deserialize_json(
                data["persistentStorage"]
            )
        )
    else:
        raise DeserializationError("DevEnvironmentSummary.persistent_storage required")
    if "vpcConnectionName" in data:
        out["vpc_connection_name"] = data["vpcConnectionName"]
    return out
