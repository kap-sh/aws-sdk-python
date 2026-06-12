"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateTransitVirtualInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.virtual_interface


class CreateTransitVirtualInterfaceResult(TypedDict):
    virtual_interface: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
    ]
    """<p>Information about a virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTransitVirtualInterfaceResult) -> dict:
    out: dict = {}
    if "virtual_interface" in value:
        import aws_sdk_direct_connect.types.virtual_interface

        out["virtualInterface"] = (
            aws_sdk_direct_connect.types.virtual_interface.serialize_aws_json_1_1(
                value["virtual_interface"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTransitVirtualInterfaceResult:
    out: CreateTransitVirtualInterfaceResult = {}  # type: ignore[typeddict-item]
    if "virtualInterface" in data:
        import aws_sdk_direct_connect.types.virtual_interface

        out["virtual_interface"] = (
            aws_sdk_direct_connect.types.virtual_interface.deserialize_aws_json_1_1(
                data["virtualInterface"]
            )
        )
    return out
