"""Generated from Smithy shape ``com.amazonaws.devicefarm#IncompatibilityMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_attribute
    import capo_device_farm.types.message


class IncompatibilityMessage(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A message about the incompatibility.</p>"""
    type: NotRequired["capo_device_farm.types.device_attribute.DeviceAttribute"]
    """<p>The type of incompatibility.</p> <p>Allowed values include:</p> <ul> <li> <p>ARN</p> </li> <li> <p>FORM_FACTOR (for example, phone or tablet)</p> </li> <li> <p>MANUFACTURER</p> </li> <li> <p>PLATFORM (for example, Android or iOS)</p> </li> <li> <p>REMOTE_ACCESS_ENABLED</p> </li> <li> <p>APPIUM_VERSION</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibilityMessage) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "type" in value:
        import capo_device_farm.types.device_attribute

        out["type"] = capo_device_farm.types.device_attribute.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IncompatibilityMessage:
    out: IncompatibilityMessage = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "type" in data:
        import capo_device_farm.types.device_attribute

        out["type"] = capo_device_farm.types.device_attribute.deserialize_aws_json_1_1(
            data["type"]
        )
    return out
