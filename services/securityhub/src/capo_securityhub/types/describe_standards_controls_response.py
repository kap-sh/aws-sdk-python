"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeStandardsControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.next_token
    import capo_securityhub.types.standards_controls


class DescribeStandardsControlsResponse(TypedDict, closed=True):
    controls: NotRequired["capo_securityhub.types.standards_controls.StandardsControls"]
    """<p>A list of security standards controls.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStandardsControlsResponse) -> dict:
    out: dict = {}
    if "controls" in value:
        import capo_securityhub.types.standards_controls

        out["Controls"] = capo_securityhub.types.standards_controls.serialize_json(
            value["controls"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeStandardsControlsResponse:
    out: DescribeStandardsControlsResponse = {}  # type: ignore[typeddict-item]
    if "Controls" in data:
        import capo_securityhub.types.standards_controls

        out["controls"] = capo_securityhub.types.standards_controls.deserialize_json(
            data["Controls"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
