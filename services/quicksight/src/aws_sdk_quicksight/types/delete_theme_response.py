"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteThemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DeleteThemeResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    theme_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>An ID for the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThemeResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "theme_id" in value:
        out["ThemeId"] = value["theme_id"]
    return out


def deserialize_json(data: dict) -> DeleteThemeResponse:
    out: DeleteThemeResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "ThemeId" in data:
        out["theme_id"] = data["ThemeId"]
    return out
