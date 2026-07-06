"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldLinkContentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_field_custom_icon_content
    import aws_sdk_quicksight.types.table_field_custom_text_content


class TableFieldLinkContentConfiguration(TypedDict, closed=True):
    custom_text_content: NotRequired[
        "aws_sdk_quicksight.types.table_field_custom_text_content.TableFieldCustomTextContent"
    ]
    """<p>The custom text content (value, font configuration) for the table link content configuration.</p>"""
    custom_icon_content: NotRequired[
        "aws_sdk_quicksight.types.table_field_custom_icon_content.TableFieldCustomIconContent"
    ]
    """<p>The custom icon content for the table link content configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldLinkContentConfiguration) -> dict:
    out: dict = {}
    if "custom_text_content" in value:
        import aws_sdk_quicksight.types.table_field_custom_text_content

        out["CustomTextContent"] = (
            aws_sdk_quicksight.types.table_field_custom_text_content.serialize_json(
                value["custom_text_content"]
            )
        )
    if "custom_icon_content" in value:
        import aws_sdk_quicksight.types.table_field_custom_icon_content

        out["CustomIconContent"] = (
            aws_sdk_quicksight.types.table_field_custom_icon_content.serialize_json(
                value["custom_icon_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldLinkContentConfiguration:
    out: TableFieldLinkContentConfiguration = {}  # type: ignore[typeddict-item]
    if "CustomTextContent" in data:
        import aws_sdk_quicksight.types.table_field_custom_text_content

        out["custom_text_content"] = (
            aws_sdk_quicksight.types.table_field_custom_text_content.deserialize_json(
                data["CustomTextContent"]
            )
        )
    if "CustomIconContent" in data:
        import aws_sdk_quicksight.types.table_field_custom_icon_content

        out["custom_icon_content"] = (
            aws_sdk_quicksight.types.table_field_custom_icon_content.deserialize_json(
                data["CustomIconContent"]
            )
        )
    return out
