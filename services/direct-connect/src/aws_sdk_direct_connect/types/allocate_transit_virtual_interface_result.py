"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocateTransitVirtualInterfaceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.virtual_interface


class AllocateTransitVirtualInterfaceResult(TypedDict, closed=True):
    virtual_interface: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
    ]
    """<p>Information about the transit virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocateTransitVirtualInterfaceResult) -> dict:
    out: dict = {}
    if "virtual_interface" in value:
        import aws_sdk_direct_connect.types.virtual_interface

        out["virtualInterface"] = (
            aws_sdk_direct_connect.types.virtual_interface.serialize_aws_json_1_1(
                value["virtual_interface"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocateTransitVirtualInterfaceResult:
    out: AllocateTransitVirtualInterfaceResult = {}  # type: ignore[typeddict-item]
    if "virtualInterface" in data:
        import aws_sdk_direct_connect.types.virtual_interface

        out["virtual_interface"] = (
            aws_sdk_direct_connect.types.virtual_interface.deserialize_aws_json_1_1(
                data["virtualInterface"]
            )
        )
    return out
