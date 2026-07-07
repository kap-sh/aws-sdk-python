"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.colors_configuration
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.column_role
    import aws_sdk_quicksight.types.decal_settings_configuration
    import aws_sdk_quicksight.types.format_configuration


class ColumnConfiguration(TypedDict, closed=True):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column.</p>"""
    format_configuration: NotRequired[
        "aws_sdk_quicksight.types.format_configuration.FormatConfiguration"
    ]
    """<p>The format configuration of a column.</p>"""
    role: NotRequired["aws_sdk_quicksight.types.column_role.ColumnRole"]
    """<p>The role of the column.</p>"""
    colors_configuration: NotRequired[
        "aws_sdk_quicksight.types.colors_configuration.ColorsConfiguration"
    ]
    """<p>The color configurations of the column.</p>"""
    decal_settings_configuration: NotRequired[
        "aws_sdk_quicksight.types.decal_settings_configuration.DecalSettingsConfiguration"
    ]
    """<p>Decal configuration of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "format_configuration" in value:
        import aws_sdk_quicksight.types.format_configuration

        out["FormatConfiguration"] = (
            aws_sdk_quicksight.types.format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    if "role" in value:
        import aws_sdk_quicksight.types.column_role

        out["Role"] = aws_sdk_quicksight.types.column_role.serialize_json(value["role"])
    if "colors_configuration" in value:
        import aws_sdk_quicksight.types.colors_configuration

        out["ColorsConfiguration"] = (
            aws_sdk_quicksight.types.colors_configuration.serialize_json(
                value["colors_configuration"]
            )
        )
    if "decal_settings_configuration" in value:
        import aws_sdk_quicksight.types.decal_settings_configuration

        out["DecalSettingsConfiguration"] = (
            aws_sdk_quicksight.types.decal_settings_configuration.serialize_json(
                value["decal_settings_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnConfiguration:
    out: ColumnConfiguration = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("ColumnConfiguration.column required")
    if "FormatConfiguration" in data:
        import aws_sdk_quicksight.types.format_configuration

        out["format_configuration"] = (
            aws_sdk_quicksight.types.format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    if "Role" in data:
        import aws_sdk_quicksight.types.column_role

        out["role"] = aws_sdk_quicksight.types.column_role.deserialize_json(
            data["Role"]
        )
    if "ColorsConfiguration" in data:
        import aws_sdk_quicksight.types.colors_configuration

        out["colors_configuration"] = (
            aws_sdk_quicksight.types.colors_configuration.deserialize_json(
                data["ColorsConfiguration"]
            )
        )
    if "DecalSettingsConfiguration" in data:
        import aws_sdk_quicksight.types.decal_settings_configuration

        out["decal_settings_configuration"] = (
            aws_sdk_quicksight.types.decal_settings_configuration.deserialize_json(
                data["DecalSettingsConfiguration"]
            )
        )
    return out
