"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeThemeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.theme


class DescribeThemeResponse(TypedDict):
    theme: NotRequired["aws_sdk_quicksight.types.theme.Theme"]
    """<p>The information about the theme that you are describing.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThemeResponse) -> dict:
    out: dict = {}
    if "theme" in value:
        import aws_sdk_quicksight.types.theme

        out["Theme"] = aws_sdk_quicksight.types.theme.serialize_json(value["theme"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeThemeResponse:
    out: DescribeThemeResponse = {}  # type: ignore[typeddict-item]
    if "Theme" in data:
        import aws_sdk_quicksight.types.theme

        out["theme"] = aws_sdk_quicksight.types.theme.deserialize_json(data["Theme"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
