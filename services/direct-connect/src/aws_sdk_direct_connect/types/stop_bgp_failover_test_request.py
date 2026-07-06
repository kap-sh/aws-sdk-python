"""Generated from Smithy shape ``com.amazonaws.directconnect#StopBgpFailoverTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.virtual_interface_id


class StopBgpFailoverTestRequest(TypedDict, closed=True):
    virtual_interface_id: (
        "aws_sdk_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    )
    """<p>The ID of the virtual interface you no longer want to test.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopBgpFailoverTestRequest) -> dict:
    out: dict = {}
    out["virtualInterfaceId"] = value["virtual_interface_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopBgpFailoverTestRequest:
    out: StopBgpFailoverTestRequest = {}  # type: ignore[typeddict-item]
    if "virtualInterfaceId" in data:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    else:
        raise DeserializationError(
            "StopBgpFailoverTestRequest.virtual_interface_id required"
        )
    return out
