"""Generated from Smithy shape ``com.amazonaws.emrserverless#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_arn
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.application_name
    import aws_sdk_emr_serverless.types.application_state
    import aws_sdk_emr_serverless.types.architecture
    import aws_sdk_emr_serverless.types.date
    import aws_sdk_emr_serverless.types.engine_type
    import aws_sdk_emr_serverless.types.release_label
    import aws_sdk_emr_serverless.types.string256


class ApplicationSummary(TypedDict, closed=True):
    id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    name: NotRequired["aws_sdk_emr_serverless.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    arn: "aws_sdk_emr_serverless.types.application_arn.ApplicationArn"
    """<p>The ARN of the application.</p>"""
    release_label: "aws_sdk_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release associated with the application.</p>"""
    type: "aws_sdk_emr_serverless.types.engine_type.EngineType"
    """<p>The type of application, such as Spark or Hive.</p>"""
    state: "aws_sdk_emr_serverless.types.application_state.ApplicationState"
    """<p>The state of the application.</p>"""
    state_details: NotRequired["aws_sdk_emr_serverless.types.string256.String256"]
    """<p>The state details of the application.</p>"""
    created_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the application was created.</p>"""
    updated_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the application was last updated.</p>"""
    architecture: NotRequired["aws_sdk_emr_serverless.types.architecture.Architecture"]
    """<p>The CPU architecture of an application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["releaseLabel"] = value["release_label"]
    out["type"] = value["type"]
    out["state"] = value["state"]
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    import aws_sdk_emr_serverless.types.date

    out["createdAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import aws_sdk_emr_serverless.types.date

    out["updatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ApplicationSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ApplicationSummary.arn required")
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("ApplicationSummary.release_label required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ApplicationSummary.type required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("ApplicationSummary.state required")
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    if "createdAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ApplicationSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ApplicationSummary.updated_at required")
    if "architecture" in data:
        out["architecture"] = data["architecture"]
    return out
