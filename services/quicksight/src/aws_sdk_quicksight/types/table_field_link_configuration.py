"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldLinkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_field_link_content_configuration
    import aws_sdk_quicksight.types.url_target_configuration


class TableFieldLinkConfiguration(TypedDict, closed=True):
    target: "aws_sdk_quicksight.types.url_target_configuration.URLTargetConfiguration"
    """<p>The URL target (new tab, new window, same tab) for the table link configuration.</p>"""
    content: "aws_sdk_quicksight.types.table_field_link_content_configuration.TableFieldLinkContentConfiguration"
    """<p>The URL content (text, icon) for the table link configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldLinkConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.url_target_configuration

    out["Target"] = aws_sdk_quicksight.types.url_target_configuration.serialize_json(
        value["target"]
    )
    import aws_sdk_quicksight.types.table_field_link_content_configuration

    out["Content"] = (
        aws_sdk_quicksight.types.table_field_link_content_configuration.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> TableFieldLinkConfiguration:
    out: TableFieldLinkConfiguration = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        import aws_sdk_quicksight.types.url_target_configuration

        out["target"] = (
            aws_sdk_quicksight.types.url_target_configuration.deserialize_json(
                data["Target"]
            )
        )
    else:
        raise DeserializationError("TableFieldLinkConfiguration.target required")
    if "Content" in data:
        import aws_sdk_quicksight.types.table_field_link_content_configuration

        out["content"] = (
            aws_sdk_quicksight.types.table_field_link_content_configuration.deserialize_json(
                data["Content"]
            )
        )
    else:
        raise DeserializationError("TableFieldLinkConfiguration.content required")
    return out
