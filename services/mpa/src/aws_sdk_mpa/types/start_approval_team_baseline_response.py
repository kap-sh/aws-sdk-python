"""Generated from Smithy shape ``com.amazonaws.mpa#StartApprovalTeamBaselineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.session_arn


class StartApprovalTeamBaselineResponse(TypedDict):
    baseline_session_arn: NotRequired["aws_sdk_mpa.types.session_arn.SessionArn"]
    """<p>Amazon Resource Name (ARN) for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartApprovalTeamBaselineResponse) -> dict:
    out: dict = {}
    if "baseline_session_arn" in value:
        out["BaselineSessionArn"] = value["baseline_session_arn"]
    return out


def deserialize_json(data: dict) -> StartApprovalTeamBaselineResponse:
    out: StartApprovalTeamBaselineResponse = {}  # type: ignore[typeddict-item]
    if "BaselineSessionArn" in data:
        out["baseline_session_arn"] = data["BaselineSessionArn"]
    return out
