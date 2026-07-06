"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardCustomizationVisualOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visual_customization_fields_configuration


class DashboardCustomizationVisualOptions(TypedDict, closed=True):
    fields_configuration: NotRequired[
        "aws_sdk_quicksight.types.visual_customization_fields_configuration.VisualCustomizationFieldsConfiguration"
    ]
    """<p>The configuration that controls field customization options available to dashboard readers for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardCustomizationVisualOptions) -> dict:
    out: dict = {}
    if "fields_configuration" in value:
        import aws_sdk_quicksight.types.visual_customization_fields_configuration

        out["FieldsConfiguration"] = (
            aws_sdk_quicksight.types.visual_customization_fields_configuration.serialize_json(
                value["fields_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashboardCustomizationVisualOptions:
    out: DashboardCustomizationVisualOptions = {}  # type: ignore[typeddict-item]
    if "FieldsConfiguration" in data:
        import aws_sdk_quicksight.types.visual_customization_fields_configuration

        out["fields_configuration"] = (
            aws_sdk_quicksight.types.visual_customization_fields_configuration.deserialize_json(
                data["FieldsConfiguration"]
            )
        )
    return out
