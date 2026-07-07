"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CustomDecodingInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.custom_decoding_signal_interface_name


class CustomDecodingInterface(TypedDict, closed=True):
    name: "aws_sdk_iotfleetwise.types.custom_decoding_signal_interface_name.CustomDecodingSignalInterfaceName"
    """<p>The name of the interface.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomDecodingInterface) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomDecodingInterface:
    out: CustomDecodingInterface = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CustomDecodingInterface.name required")
    return out
