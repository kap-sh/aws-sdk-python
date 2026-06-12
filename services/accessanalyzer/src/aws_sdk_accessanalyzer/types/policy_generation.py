"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PolicyGeneration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.job_id
    import aws_sdk_accessanalyzer.types.job_status
    import aws_sdk_accessanalyzer.types.principal_arn
    import aws_sdk_accessanalyzer.types.timestamp


class PolicyGeneration(TypedDict):
    job_id: "aws_sdk_accessanalyzer.types.job_id.JobId"
    """<p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>"""
    principal_arn: "aws_sdk_accessanalyzer.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM entity (user or role) for which you are generating a policy.</p>"""
    status: "aws_sdk_accessanalyzer.types.job_status.JobStatus"
    """<p>The status of the policy generation request.</p>"""
    started_on: "aws_sdk_accessanalyzer.types.timestamp.Timestamp"
    """<p>A timestamp of when the policy generation started.</p>"""
    completed_on: NotRequired["aws_sdk_accessanalyzer.types.timestamp.Timestamp"]
    """<p>A timestamp of when the policy generation was completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGeneration) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["principalArn"] = value["principal_arn"]
    out["status"] = value["status"]
    import aws_sdk_accessanalyzer.types.timestamp

    out["startedOn"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
        value["started_on"]
    )
    if "completed_on" in value:
        import aws_sdk_accessanalyzer.types.timestamp

        out["completedOn"] = aws_sdk_accessanalyzer.types.timestamp.serialize_json(
            value["completed_on"]
        )
    return out


def deserialize_json(data: dict) -> PolicyGeneration:
    out: PolicyGeneration = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("PolicyGeneration.job_id required")
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    else:
        raise DeserializationError("PolicyGeneration.principal_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("PolicyGeneration.status required")
    if "startedOn" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["started_on"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["startedOn"]
        )
    else:
        raise DeserializationError("PolicyGeneration.started_on required")
    if "completedOn" in data:
        import aws_sdk_accessanalyzer.types.timestamp

        out["completed_on"] = aws_sdk_accessanalyzer.types.timestamp.deserialize_json(
            data["completedOn"]
        )
    return out
