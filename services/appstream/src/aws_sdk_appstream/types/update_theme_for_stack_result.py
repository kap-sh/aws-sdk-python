"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateThemeForStackResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.theme


class UpdateThemeForStackResult(TypedDict):
    theme: NotRequired["aws_sdk_appstream.types.theme.Theme"]
    """<p> The theme object that contains the metadata of the custom branding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateThemeForStackResult) -> dict:
    out: dict = {}
    if "theme" in value:
        import aws_sdk_appstream.types.theme

        out["Theme"] = aws_sdk_appstream.types.theme.serialize_aws_json_1_1(
            value["theme"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateThemeForStackResult:
    out: UpdateThemeForStackResult = {}  # type: ignore[typeddict-item]
    if "Theme" in data:
        import aws_sdk_appstream.types.theme

        out["theme"] = aws_sdk_appstream.types.theme.deserialize_aws_json_1_1(
            data["Theme"]
        )
    return out
