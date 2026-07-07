"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_label
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.table_field_url_configuration
    import aws_sdk_quicksight.types.visibility


class TableFieldOption(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID for a table field.</p>"""
    width: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>The width for a table field.</p>"""
    custom_label: NotRequired["aws_sdk_quicksight.types.custom_label.CustomLabel"]
    """<p>The custom label for a table field.</p>"""
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility of a table field.</p>"""
    url_styling: NotRequired[
        "aws_sdk_quicksight.types.table_field_url_configuration.TableFieldURLConfiguration"
    ]
    """<p>The URL configuration for a table field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldOption) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "width" in value:
        out["Width"] = value["width"]
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "url_styling" in value:
        import aws_sdk_quicksight.types.table_field_url_configuration

        out["URLStyling"] = (
            aws_sdk_quicksight.types.table_field_url_configuration.serialize_json(
                value["url_styling"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldOption:
    out: TableFieldOption = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("TableFieldOption.field_id required")
    if "Width" in data:
        out["width"] = data["Width"]
    if "CustomLabel" in data:
        out["custom_label"] = data["CustomLabel"]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "URLStyling" in data:
        import aws_sdk_quicksight.types.table_field_url_configuration

        out["url_styling"] = (
            aws_sdk_quicksight.types.table_field_url_configuration.deserialize_json(
                data["URLStyling"]
            )
        )
    return out
