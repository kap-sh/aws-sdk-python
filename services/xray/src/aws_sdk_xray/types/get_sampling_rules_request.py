"""Generated from Smithy shape ``com.amazonaws.xray#GetSamplingRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.string


class GetSamplingRulesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingRulesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSamplingRulesRequest:
    out: GetSamplingRulesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
