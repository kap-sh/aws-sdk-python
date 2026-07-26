"""Generated from Smithy shape ``com.amazonaws.amplify#StartDeploymentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.job_summary


class StartDeploymentResult(TypedDict, closed=True):
    job_summary: "capo_amplify.types.job_summary.JobSummary"
    """<p>The summary for the job. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeploymentResult) -> dict:
    out: dict = {}
    import capo_amplify.types.job_summary

    out["jobSummary"] = capo_amplify.types.job_summary.serialize_json(
        value["job_summary"]
    )
    return out


def deserialize_json(data: dict) -> StartDeploymentResult:
    out: StartDeploymentResult = {}  # type: ignore[typeddict-item]
    if "jobSummary" in data:
        import capo_amplify.types.job_summary

        out["job_summary"] = capo_amplify.types.job_summary.deserialize_json(
            data["jobSummary"]
        )
    else:
        raise DeserializationError("StartDeploymentResult.job_summary required")
    return out
