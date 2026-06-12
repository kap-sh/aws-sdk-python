"""Generated from Smithy shape ``com.amazonaws.emrserverless#SessionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.date
    import aws_sdk_emr_serverless.types.iam_role_arn
    import aws_sdk_emr_serverless.types.release_label
    import aws_sdk_emr_serverless.types.request_identity_user_arn
    import aws_sdk_emr_serverless.types.session_arn
    import aws_sdk_emr_serverless.types.session_id
    import aws_sdk_emr_serverless.types.session_state
    import aws_sdk_emr_serverless.types.string256
    import aws_sdk_emr_serverless.types.string1024


class SessionSummary(TypedDict):
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


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("SessionSummary.application_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionSummary.session_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SessionSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("SessionSummary.state required")
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    else:
        raise DeserializationError("SessionSummary.state_details required")
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("SessionSummary.release_label required")
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("SessionSummary.execution_role_arn required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("SessionSummary.created_by required")
    if "createdAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("SessionSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("SessionSummary.updated_at required")
    return out
