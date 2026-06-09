"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_state_name
    import aws_sdk_ec2.types.integer


class InstanceState(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The state of the instance as a 16-bit unsigned integer. </p> <p>The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored.</p> <p>The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255. </p> <p>The valid values for instance-state-code will all be in the range of the low byte and they are:</p> <ul> <li> <p> <code>0</code> : <code>pending</code> </p> </li> <li> <p> <code>16</code> : <code>running</code> </p> </li> <li> <p> <code>32</code> : <code>shutting-down</code> </p> </li> <li> <p> <code>48</code> : <code>terminated</code> </p> </li> <li> <p> <code>64</code> : <code>stopping</code> </p> </li> <li> <p> <code>80</code> : <code>stopped</code> </p> </li> </ul> <p>You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal.</p>"""
    name: NotRequired["aws_sdk_ec2.types.instance_state_name.InstanceStateName"]
    """<p>The current state of the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        pairs.append((f"{prefix}.Code", str(value["code"])))
    if "name" in value:
        import aws_sdk_ec2.types.instance_state_name

        aws_sdk_ec2.types.instance_state_name.serialize_ec2_query(
            value["name"], pairs, f"{prefix}.Name"
        )


def deserialize_ec2_query(el: Element) -> InstanceState:
    out: InstanceState = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = int(child_code.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        import aws_sdk_ec2.types.instance_state_name

        out["name"] = aws_sdk_ec2.types.instance_state_name.deserialize_ec2_query(
            child_name
        )
    return out
