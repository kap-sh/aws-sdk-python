"""Generated from Smithy shape ``com.amazonaws.quicksight#ContextualAccentPalette``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.palette


class ContextualAccentPalette(TypedDict, closed=True):
    connection: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    visualization: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    insight: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    automation: NotRequired["aws_sdk_quicksight.types.palette.Palette"]


# --- restJson1 ser/de ---
def serialize_json(value: ContextualAccentPalette) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_quicksight.types.palette

        out["Connection"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["connection"]
        )
    if "visualization" in value:
        import aws_sdk_quicksight.types.palette

        out["Visualization"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["visualization"]
        )
    if "insight" in value:
        import aws_sdk_quicksight.types.palette

        out["Insight"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["insight"]
        )
    if "automation" in value:
        import aws_sdk_quicksight.types.palette

        out["Automation"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["automation"]
        )
    return out


def deserialize_json(data: dict) -> ContextualAccentPalette:
    out: ContextualAccentPalette = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_quicksight.types.palette

        out["connection"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Connection"]
        )
    if "Visualization" in data:
        import aws_sdk_quicksight.types.palette

        out["visualization"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Visualization"]
        )
    if "Insight" in data:
        import aws_sdk_quicksight.types.palette

        out["insight"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Insight"]
        )
    if "Automation" in data:
        import aws_sdk_quicksight.types.palette

        out["automation"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Automation"]
        )
    return out
