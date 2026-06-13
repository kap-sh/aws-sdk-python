"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#InstanceState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.instance_state_name


class InstanceState(TypedDict):
    code: NotRequired["int"]
    """<p>The state of the instance as a 16-bit unsigned integer. </p> <p>The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored. </p> <p>The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255. </p> <p>The valid values for the instance state code are all in the range of the low byte. These values are: </p> <ul> <li> <p> <code>0</code> : <code>pending</code> </p> </li> <li> <p> <code>16</code> : <code>running</code> </p> </li> <li> <p> <code>32</code> : <code>shutting-down</code> </p> </li> <li> <p> <code>48</code> : <code>terminated</code> </p> </li> <li> <p> <code>64</code> : <code>stopping</code> </p> </li> <li> <p> <code>80</code> : <code>stopped</code> </p> </li> </ul> <p>You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal. </p>"""
    name: NotRequired[
        "aws_sdk_snow_device_management.types.instance_state_name.InstanceStateName"
    ]
    """<p>The current state of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceState) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> InstanceState:
    out: InstanceState = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "name" in data:
        out["name"] = data["name"]
    return out
