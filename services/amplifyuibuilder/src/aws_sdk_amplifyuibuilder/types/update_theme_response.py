"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#UpdateThemeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.theme


class UpdateThemeResponse(TypedDict):
    entity: NotRequired["aws_sdk_amplifyuibuilder.types.theme.Theme"]
    """<p>Describes the configuration of the updated theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import aws_sdk_amplifyuibuilder.types.theme

        out["entity"] = aws_sdk_amplifyuibuilder.types.theme.serialize_json(
            value["entity"]
        )
    return out


def deserialize_json(data: dict) -> UpdateThemeResponse:
    out: UpdateThemeResponse = {}  # type: ignore[typeddict-item]
    if "entity" in data:
        import aws_sdk_amplifyuibuilder.types.theme

        out["entity"] = aws_sdk_amplifyuibuilder.types.theme.deserialize_json(
            data["entity"]
        )
    return out
