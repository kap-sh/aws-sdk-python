"""Generated from Smithy shape ``com.amazonaws.directconnect#StartBgpFailoverTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.virtual_interface_test_history


class StartBgpFailoverTestResponse(TypedDict, closed=True):
    virtual_interface_test: NotRequired[
        "capo_direct_connect.types.virtual_interface_test_history.VirtualInterfaceTestHistory"
    ]
    """<p>Information about the virtual interface failover test.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBgpFailoverTestResponse) -> dict:
    out: dict = {}
    if "virtual_interface_test" in value:
        import capo_direct_connect.types.virtual_interface_test_history

        out["virtualInterfaceTest"] = (
            capo_direct_connect.types.virtual_interface_test_history.serialize_aws_json_1_1(
                value["virtual_interface_test"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBgpFailoverTestResponse:
    out: StartBgpFailoverTestResponse = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceTest" in data:
        import capo_direct_connect.types.virtual_interface_test_history

        out["virtual_interface_test"] = (
            capo_direct_connect.types.virtual_interface_test_history.deserialize_aws_json_1_1(
                data["virtualInterfaceTest"]
            )
        )
    return out
