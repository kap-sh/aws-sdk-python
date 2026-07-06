"""Generated from Smithy shape ``com.amazonaws.synthetics#GetCanaryRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary_runs
    import aws_sdk_synthetics.types.token


class GetCanaryRunsResponse(TypedDict, closed=True):
    canary_runs: NotRequired["aws_sdk_synthetics.types.canary_runs.CanaryRuns"]
    """<p>An array of structures. Each structure contains the details of one of the retrieved canary runs.</p>"""
    next_token: NotRequired["aws_sdk_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>GetCanaryRuns</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCanaryRunsResponse) -> dict:
    out: dict = {}
    if "canary_runs" in value:
        import aws_sdk_synthetics.types.canary_runs

        out["CanaryRuns"] = aws_sdk_synthetics.types.canary_runs.serialize_json(
            value["canary_runs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCanaryRunsResponse:
    out: GetCanaryRunsResponse = {}  # type: ignore[typeddict-item]
    if "CanaryRuns" in data:
        import aws_sdk_synthetics.types.canary_runs

        out["canary_runs"] = aws_sdk_synthetics.types.canary_runs.deserialize_json(
            data["CanaryRuns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
