"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.byoip_cidr_events
    import aws_sdk_global_accelerator.types.byoip_cidr_state
    import aws_sdk_global_accelerator.types.generic_string


class ByoipCidr(TypedDict, closed=True):
    cidr: NotRequired["aws_sdk_global_accelerator.types.generic_string.GenericString"]
    r"""<p>The address range, in CIDR notation.</p> <p> For more information, see <a href=\"https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html\">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""
    state: NotRequired[
        "aws_sdk_global_accelerator.types.byoip_cidr_state.ByoipCidrState"
    ]
    """<p>The state of the address pool.</p>"""
    events: NotRequired[
        "aws_sdk_global_accelerator.types.byoip_cidr_events.ByoipCidrEvents"
    ]
    """<p>A history of status changes for an IP address range that you bring to Global Accelerator through bring your own IP address (BYOIP).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByoipCidr) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "state" in value:
        import aws_sdk_global_accelerator.types.byoip_cidr_state

        out["State"] = (
            aws_sdk_global_accelerator.types.byoip_cidr_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "events" in value:
        import aws_sdk_global_accelerator.types.byoip_cidr_events

        out["Events"] = (
            aws_sdk_global_accelerator.types.byoip_cidr_events.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ByoipCidr:
    out: ByoipCidr = {}  # type: ignore[typeddict-item]
    if "Cidr" in data:
        out["cidr"] = data["Cidr"]
    if "State" in data:
        import aws_sdk_global_accelerator.types.byoip_cidr_state

        out["state"] = (
            aws_sdk_global_accelerator.types.byoip_cidr_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "Events" in data:
        import aws_sdk_global_accelerator.types.byoip_cidr_events

        out["events"] = (
            aws_sdk_global_accelerator.types.byoip_cidr_events.deserialize_aws_json_1_1(
                data["Events"]
            )
        )
    return out
