"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CancelPolicyGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.job_id


class CancelPolicyGenerationRequest(TypedDict, closed=True):
    job_id: "aws_sdk_accessanalyzer.types.job_id.JobId"
    """<p>The <code>JobId</code> that is returned by the <code>StartPolicyGeneration</code> operation. The <code>JobId</code> can be used with <code>GetGeneratedPolicy</code> to retrieve the generated policies or used with <code>CancelPolicyGeneration</code> to cancel the policy generation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelPolicyGenerationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelPolicyGenerationRequest:
    out: CancelPolicyGenerationRequest = {}  # type: ignore[typeddict-item]
    return out
