"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomizationFieldsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_customization_status
    import aws_sdk_quicksight.types.visual_customization_additional_fields_list


class VisualCustomizationFieldsConfiguration(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_quicksight.types.dashboard_customization_status.DashboardCustomizationStatus"
    ]
    """<p>Specifies whether dashboard readers can customize fields for this visual. This option is <code>ENABLED</code> by default.</p>"""
    additional_fields: NotRequired[
        "aws_sdk_quicksight.types.visual_customization_additional_fields_list.VisualCustomizationAdditionalFieldsList"
    ]
    """<p>The additional dataset fields available for dashboard readers to customize the visual with, beyond the fields already configured on the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomizationFieldsConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_quicksight.types.dashboard_customization_status

        out["Status"] = (
            aws_sdk_quicksight.types.dashboard_customization_status.serialize_json(
                value["status"]
            )
        )
    if "additional_fields" in value:
        import aws_sdk_quicksight.types.visual_customization_additional_fields_list

        out["AdditionalFields"] = (
            aws_sdk_quicksight.types.visual_customization_additional_fields_list.serialize_json(
                value["additional_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualCustomizationFieldsConfiguration:
    out: VisualCustomizationFieldsConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_quicksight.types.dashboard_customization_status

        out["status"] = (
            aws_sdk_quicksight.types.dashboard_customization_status.deserialize_json(
                data["Status"]
            )
        )
    if "AdditionalFields" in data:
        import aws_sdk_quicksight.types.visual_customization_additional_fields_list

        out["additional_fields"] = (
            aws_sdk_quicksight.types.visual_customization_additional_fields_list.deserialize_json(
                data["AdditionalFields"]
            )
        )
    return out
