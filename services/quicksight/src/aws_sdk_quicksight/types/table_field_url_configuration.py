"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldURLConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_field_image_configuration
    import aws_sdk_quicksight.types.table_field_link_configuration


class TableFieldURLConfiguration(TypedDict):
    link_configuration: NotRequired[
        "aws_sdk_quicksight.types.table_field_link_configuration.TableFieldLinkConfiguration"
    ]
    """<p>The link configuration of a table field URL.</p>"""
    image_configuration: NotRequired[
        "aws_sdk_quicksight.types.table_field_image_configuration.TableFieldImageConfiguration"
    ]
    """<p>The image configuration of a table field URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldURLConfiguration) -> dict:
    out: dict = {}
    if "link_configuration" in value:
        import aws_sdk_quicksight.types.table_field_link_configuration

        out["LinkConfiguration"] = (
            aws_sdk_quicksight.types.table_field_link_configuration.serialize_json(
                value["link_configuration"]
            )
        )
    if "image_configuration" in value:
        import aws_sdk_quicksight.types.table_field_image_configuration

        out["ImageConfiguration"] = (
            aws_sdk_quicksight.types.table_field_image_configuration.serialize_json(
                value["image_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldURLConfiguration:
    out: TableFieldURLConfiguration = {}  # type: ignore[typeddict-item]
    if "LinkConfiguration" in data:
        import aws_sdk_quicksight.types.table_field_link_configuration

        out["link_configuration"] = (
            aws_sdk_quicksight.types.table_field_link_configuration.deserialize_json(
                data["LinkConfiguration"]
            )
        )
    if "ImageConfiguration" in data:
        import aws_sdk_quicksight.types.table_field_image_configuration

        out["image_configuration"] = (
            aws_sdk_quicksight.types.table_field_image_configuration.deserialize_json(
                data["ImageConfiguration"]
            )
        )
    return out
