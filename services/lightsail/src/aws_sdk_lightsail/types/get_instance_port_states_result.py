"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstancePortStatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_port_state_list


class GetInstancePortStatesResult(TypedDict, closed=True):
    port_states: NotRequired[
        "aws_sdk_lightsail.types.instance_port_state_list.InstancePortStateList"
    ]
    """<p>An array of objects that describe the firewall port states for the specified instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstancePortStatesResult) -> dict:
    out: dict = {}
    if "port_states" in value:
        import aws_sdk_lightsail.types.instance_port_state_list

        out["portStates"] = (
            aws_sdk_lightsail.types.instance_port_state_list.serialize_aws_json_1_1(
                value["port_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstancePortStatesResult:
    out: GetInstancePortStatesResult = {}  # type: ignore[typeddict-item]
    if "portStates" in data:
        import aws_sdk_lightsail.types.instance_port_state_list

        out["port_states"] = (
            aws_sdk_lightsail.types.instance_port_state_list.deserialize_aws_json_1_1(
                data["portStates"]
            )
        )
    return out
