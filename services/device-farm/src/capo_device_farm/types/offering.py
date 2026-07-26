"""Generated from Smithy shape ``com.amazonaws.devicefarm#Offering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_platform
    import capo_device_farm.types.message
    import capo_device_farm.types.offering_identifier
    import capo_device_farm.types.offering_type
    import capo_device_farm.types.recurring_charges


class Offering(TypedDict, closed=True):
    id: NotRequired["capo_device_farm.types.offering_identifier.OfferingIdentifier"]
    """<p>The ID that corresponds to a device offering.</p>"""
    description: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A string that describes the offering.</p>"""
    type: NotRequired["capo_device_farm.types.offering_type.OfferingType"]
    """<p>The type of offering (for example, <code>RECURRING</code>) for a device.</p>"""
    platform: NotRequired["capo_device_farm.types.device_platform.DevicePlatform"]
    """<p>The platform of the device (for example, <code>ANDROID</code> or <code>IOS</code>).</p>"""
    recurring_charges: NotRequired[
        "capo_device_farm.types.recurring_charges.RecurringCharges"
    ]
    """<p>Specifies whether there are recurring charges for the offering.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Offering) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import capo_device_farm.types.offering_type

        out["type"] = capo_device_farm.types.offering_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "platform" in value:
        import capo_device_farm.types.device_platform

        out["platform"] = capo_device_farm.types.device_platform.serialize_aws_json_1_1(
            value["platform"]
        )
    if "recurring_charges" in value:
        import capo_device_farm.types.recurring_charges

        out["recurringCharges"] = (
            capo_device_farm.types.recurring_charges.serialize_aws_json_1_1(
                value["recurring_charges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Offering:
    out: Offering = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import capo_device_farm.types.offering_type

        out["type"] = capo_device_farm.types.offering_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "platform" in data:
        import capo_device_farm.types.device_platform

        out["platform"] = (
            capo_device_farm.types.device_platform.deserialize_aws_json_1_1(
                data["platform"]
            )
        )
    if "recurringCharges" in data:
        import capo_device_farm.types.recurring_charges

        out["recurring_charges"] = (
            capo_device_farm.types.recurring_charges.deserialize_aws_json_1_1(
                data["recurringCharges"]
            )
        )
    return out
