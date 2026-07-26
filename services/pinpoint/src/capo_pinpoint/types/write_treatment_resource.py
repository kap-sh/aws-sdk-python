"""Generated from Smithy shape ``com.amazonaws.pinpoint#WriteTreatmentResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.custom_delivery_configuration
    import capo_pinpoint.types.message_configuration
    import capo_pinpoint.types.schedule
    import capo_pinpoint.types.template_configuration


class WriteTreatmentResource(TypedDict, closed=True):
    custom_delivery_configuration: NotRequired[
        "capo_pinpoint.types.custom_delivery_configuration.CustomDeliveryConfiguration"
    ]
    """<p>The delivery configuration settings for sending the treatment through a custom channel. This object is required if the MessageConfiguration object for the treatment specifies a CustomMessage object.</p>"""
    message_configuration: NotRequired[
        "capo_pinpoint.types.message_configuration.MessageConfiguration"
    ]
    """<p>The message configuration settings for the treatment.</p>"""
    schedule: NotRequired["capo_pinpoint.types.schedule.Schedule"]
    """<p>The schedule settings for the treatment.</p>"""
    size_percent: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The allocated percentage of users (segment members) to send the treatment to.</p>"""
    template_configuration: NotRequired[
        "capo_pinpoint.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The message template to use for the treatment.</p>"""
    treatment_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom description of the treatment.</p>"""
    treatment_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom name for the treatment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WriteTreatmentResource) -> dict:
    out: dict = {}
    if "custom_delivery_configuration" in value:
        import capo_pinpoint.types.custom_delivery_configuration

        out["CustomDeliveryConfiguration"] = (
            capo_pinpoint.types.custom_delivery_configuration.serialize_json(
                value["custom_delivery_configuration"]
            )
        )
    if "message_configuration" in value:
        import capo_pinpoint.types.message_configuration

        out["MessageConfiguration"] = (
            capo_pinpoint.types.message_configuration.serialize_json(
                value["message_configuration"]
            )
        )
    if "schedule" in value:
        import capo_pinpoint.types.schedule

        out["Schedule"] = capo_pinpoint.types.schedule.serialize_json(value["schedule"])
    if "size_percent" in value:
        out["SizePercent"] = value["size_percent"]
    if "template_configuration" in value:
        import capo_pinpoint.types.template_configuration

        out["TemplateConfiguration"] = (
            capo_pinpoint.types.template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "treatment_description" in value:
        out["TreatmentDescription"] = value["treatment_description"]
    if "treatment_name" in value:
        out["TreatmentName"] = value["treatment_name"]
    return out


def deserialize_json(data: dict) -> WriteTreatmentResource:
    out: WriteTreatmentResource = {}  # type: ignore[typeddict-item]
    if "CustomDeliveryConfiguration" in data:
        import capo_pinpoint.types.custom_delivery_configuration

        out["custom_delivery_configuration"] = (
            capo_pinpoint.types.custom_delivery_configuration.deserialize_json(
                data["CustomDeliveryConfiguration"]
            )
        )
    if "MessageConfiguration" in data:
        import capo_pinpoint.types.message_configuration

        out["message_configuration"] = (
            capo_pinpoint.types.message_configuration.deserialize_json(
                data["MessageConfiguration"]
            )
        )
    if "Schedule" in data:
        import capo_pinpoint.types.schedule

        out["schedule"] = capo_pinpoint.types.schedule.deserialize_json(
            data["Schedule"]
        )
    if "SizePercent" in data:
        out["size_percent"] = data["SizePercent"]
    if "TemplateConfiguration" in data:
        import capo_pinpoint.types.template_configuration

        out["template_configuration"] = (
            capo_pinpoint.types.template_configuration.deserialize_json(
                data["TemplateConfiguration"]
            )
        )
    if "TreatmentDescription" in data:
        out["treatment_description"] = data["TreatmentDescription"]
    if "TreatmentName" in data:
        out["treatment_name"] = data["TreatmentName"]
    return out
