"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeCanariesLastRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.canaries_last_run
    import capo_synthetics.types.token


class DescribeCanariesLastRunResponse(TypedDict, closed=True):
    canaries_last_run: NotRequired[
        "capo_synthetics.types.canaries_last_run.CanariesLastRun"
    ]
    """<p>An array that contains the information from the most recent run of each canary.</p>"""
    next_token: NotRequired["capo_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>DescribeCanariesLastRun</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCanariesLastRunResponse) -> dict:
    out: dict = {}
    if "canaries_last_run" in value:
        import capo_synthetics.types.canaries_last_run

        out["CanariesLastRun"] = capo_synthetics.types.canaries_last_run.serialize_json(
            value["canaries_last_run"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeCanariesLastRunResponse:
    out: DescribeCanariesLastRunResponse = {}  # type: ignore[typeddict-item]
    if "CanariesLastRun" in data:
        import capo_synthetics.types.canaries_last_run

        out["canaries_last_run"] = (
            capo_synthetics.types.canaries_last_run.deserialize_json(
                data["CanariesLastRun"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
