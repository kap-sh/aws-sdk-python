"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemeAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.theme_alias


class UpdateThemeAliasResponse(TypedDict, closed=True):
    theme_alias: NotRequired["capo_quicksight.types.theme_alias.ThemeAlias"]
    """<p>Information about the theme alias.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeAliasResponse) -> dict:
    out: dict = {}
    if "theme_alias" in value:
        import capo_quicksight.types.theme_alias

        out["ThemeAlias"] = capo_quicksight.types.theme_alias.serialize_json(
            value["theme_alias"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateThemeAliasResponse:
    out: UpdateThemeAliasResponse = {}  # type: ignore[typeddict-item]
    if "ThemeAlias" in data:
        import capo_quicksight.types.theme_alias

        out["theme_alias"] = capo_quicksight.types.theme_alias.deserialize_json(
            data["ThemeAlias"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
