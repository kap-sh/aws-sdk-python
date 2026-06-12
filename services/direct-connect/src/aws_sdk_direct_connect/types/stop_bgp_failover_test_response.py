"""Generated from Smithy shape ``com.amazonaws.directconnect#StopBgpFailoverTestResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.virtual_interface_test_history


class StopBgpFailoverTestResponse(TypedDict):
    virtual_interface_test: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_test_history.VirtualInterfaceTestHistory"
    ]
    """<p>Information about the virtual interface failover test.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopBgpFailoverTestResponse) -> dict:
    out: dict = {}
    if "virtual_interface_test" in value:
        import aws_sdk_direct_connect.types.virtual_interface_test_history

        out["virtualInterfaceTest"] = (
            aws_sdk_direct_connect.types.virtual_interface_test_history.serialize_aws_json_1_1(
                value["virtual_interface_test"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopBgpFailoverTestResponse:
    out: StopBgpFailoverTestResponse = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceTest" in data:
        import aws_sdk_direct_connect.types.virtual_interface_test_history

        out["virtual_interface_test"] = (
            aws_sdk_direct_connect.types.virtual_interface_test_history.deserialize_aws_json_1_1(
                data["virtualInterfaceTest"]
            )
        )
    return out
