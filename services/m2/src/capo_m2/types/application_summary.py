"""Generated from Smithy shape ``com.amazonaws.m2#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.application_deployment_lifecycle
    import capo_m2.types.application_lifecycle
    import capo_m2.types.application_version_lifecycle
    import capo_m2.types.arn
    import capo_m2.types.engine_type
    import capo_m2.types.entity_description
    import capo_m2.types.entity_name
    import capo_m2.types.identifier
    import capo_m2.types.timestamp
    import capo_m2.types.version


class ApplicationSummary(TypedDict, closed=True):
    name: "capo_m2.types.entity_name.EntityName"
    """<p>The name of the application.</p>"""
    description: NotRequired["capo_m2.types.entity_description.EntityDescription"]
    """<p>The description of the application.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""
    application_arn: "capo_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_version: "capo_m2.types.version.Version"
    """<p>The version of the application.</p>"""
    status: "capo_m2.types.application_lifecycle.ApplicationLifecycle"
    """<p>The status of the application.</p>"""
    engine_type: "capo_m2.types.engine_type.EngineType"
    """<p>The type of the target platform for this application.</p>"""
    creation_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the application was created.</p>"""
    environment_id: NotRequired["capo_m2.types.identifier.Identifier"]
    """<p>The unique identifier of the runtime environment that hosts this application.</p>"""
    last_start_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when you last started the application. Null until the application runs for the first time.</p>"""
    version_status: NotRequired[
        "capo_m2.types.application_version_lifecycle.ApplicationVersionLifecycle"
    ]
    """<p>Indicates the status of the latest version of the application.</p>"""
    deployment_status: NotRequired[
        "capo_m2.types.application_deployment_lifecycle.ApplicationDeploymentLifecycle"
    ]
    """<p>Indicates either an ongoing deployment or if the application has ever deployed successfully.</p>"""
    role_arn: NotRequired["capo_m2.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the role associated with the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["applicationId"] = value["application_id"]
    out["applicationArn"] = value["application_arn"]
    out["applicationVersion"] = value["application_version"]
    out["status"] = value["status"]
    out["engineType"] = value["engine_type"]
    import capo_m2.types.timestamp

    out["creationTime"] = capo_m2.types.timestamp.serialize_json(value["creation_time"])
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "last_start_time" in value:
        import capo_m2.types.timestamp

        out["lastStartTime"] = capo_m2.types.timestamp.serialize_json(
            value["last_start_time"]
        )
    if "version_status" in value:
        out["versionStatus"] = value["version_status"]
    if "deployment_status" in value:
        out["deploymentStatus"] = value["deployment_status"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ApplicationSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("ApplicationSummary.application_id required")
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    else:
        raise DeserializationError("ApplicationSummary.application_arn required")
    if "applicationVersion" in data:
        out["application_version"] = data["applicationVersion"]
    else:
        raise DeserializationError("ApplicationSummary.application_version required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ApplicationSummary.status required")
    if "engineType" in data:
        out["engine_type"] = data["engineType"]
    else:
        raise DeserializationError("ApplicationSummary.engine_type required")
    if "creationTime" in data:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ApplicationSummary.creation_time required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "lastStartTime" in data:
        import capo_m2.types.timestamp

        out["last_start_time"] = capo_m2.types.timestamp.deserialize_json(
            data["lastStartTime"]
        )
    if "versionStatus" in data:
        out["version_status"] = data["versionStatus"]
    if "deploymentStatus" in data:
        out["deployment_status"] = data["deploymentStatus"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
