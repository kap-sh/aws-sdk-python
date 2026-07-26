"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeThemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.theme


class DescribeThemeResponse(TypedDict, closed=True):
    theme: NotRequired["capo_quicksight.types.theme.Theme"]
    """<p>The information about the theme that you are describing.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThemeResponse) -> dict:
    out: dict = {}
    if "theme" in value:
        import capo_quicksight.types.theme

        out["Theme"] = capo_quicksight.types.theme.serialize_json(value["theme"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeThemeResponse:
    out: DescribeThemeResponse = {}  # type: ignore[typeddict-item]
    if "Theme" in data:
        import capo_quicksight.types.theme

        out["theme"] = capo_quicksight.types.theme.deserialize_json(data["Theme"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
