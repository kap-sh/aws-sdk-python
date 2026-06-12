"""Generated from Smithy shape ``com.amazonaws.amplify#Job``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.job_summary
    import aws_sdk_amplify.types.steps


class Job(TypedDict):
    summary: "aws_sdk_amplify.types.job_summary.JobSummary"
    """<p> Describes the summary for an execution job for an Amplify app. </p>"""
    steps: "aws_sdk_amplify.types.steps.Steps"
    """<p> The execution steps for an execution job, for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.job_summary

    out["summary"] = aws_sdk_amplify.types.job_summary.serialize_json(value["summary"])
    import aws_sdk_amplify.types.steps

    out["steps"] = aws_sdk_amplify.types.steps.serialize_json(value["steps"])
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_amplify.types.job_summary

        out["summary"] = aws_sdk_amplify.types.job_summary.deserialize_json(
            data["summary"]
        )
    else:
        raise DeserializationError("Job.summary required")
    if "steps" in data:
        import aws_sdk_amplify.types.steps

        out["steps"] = aws_sdk_amplify.types.steps.deserialize_json(data["steps"])
    else:
        raise DeserializationError("Job.steps required")
    return out
