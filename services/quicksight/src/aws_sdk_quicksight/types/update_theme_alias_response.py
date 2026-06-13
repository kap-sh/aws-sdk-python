"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemeAliasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.theme_alias


class UpdateThemeAliasResponse(TypedDict):
    theme_alias: NotRequired["aws_sdk_quicksight.types.theme_alias.ThemeAlias"]
    """<p>Information about the theme alias.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeAliasResponse) -> dict:
    out: dict = {}
    if "theme_alias" in value:
        import aws_sdk_quicksight.types.theme_alias

        out["ThemeAlias"] = aws_sdk_quicksight.types.theme_alias.serialize_json(
            value["theme_alias"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateThemeAliasResponse:
    out: UpdateThemeAliasResponse = {}  # type: ignore[typeddict-item]
    if "ThemeAlias" in data:
        import aws_sdk_quicksight.types.theme_alias

        out["theme_alias"] = aws_sdk_quicksight.types.theme_alias.deserialize_json(
            data["ThemeAlias"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
