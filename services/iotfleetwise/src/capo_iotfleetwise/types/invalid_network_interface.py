"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidNetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.interface_id
    import capo_iotfleetwise.types.network_interface_failure_reason


class InvalidNetworkInterface(TypedDict, closed=True):
    interface_id: NotRequired["capo_iotfleetwise.types.interface_id.InterfaceId"]
    """<p>The ID of the interface that isn't valid.</p>"""
    reason: NotRequired[
        "capo_iotfleetwise.types.network_interface_failure_reason.NetworkInterfaceFailureReason"
    ]
    """<p>A message about why the interface isn't valid. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidNetworkInterface) -> dict:
    out: dict = {}
    if "interface_id" in value:
        out["interfaceId"] = value["interface_id"]
    if "reason" in value:
        import capo_iotfleetwise.types.network_interface_failure_reason

        out["reason"] = (
            capo_iotfleetwise.types.network_interface_failure_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidNetworkInterface:
    out: InvalidNetworkInterface = {}  # type: ignore[typeddict-item]
    if "interfaceId" in data:
        out["interface_id"] = data["interfaceId"]
    if "reason" in data:
        import capo_iotfleetwise.types.network_interface_failure_reason

        out["reason"] = (
            capo_iotfleetwise.types.network_interface_failure_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    return out
