"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterfaces``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.pagination_token
    import aws_sdk_direct_connect.types.virtual_interface_list


class VirtualInterfaces(TypedDict):
    virtual_interfaces: NotRequired[
        "aws_sdk_direct_connect.types.virtual_interface_list.VirtualInterfaceList"
    ]
    """<p>The virtual interfaces</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterfaces) -> dict:
    out: dict = {}
    if "virtual_interfaces" in value:
        import aws_sdk_direct_connect.types.virtual_interface_list

        out["virtualInterfaces"] = (
            aws_sdk_direct_connect.types.virtual_interface_list.serialize_aws_json_1_1(
                value["virtual_interfaces"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VirtualInterfaces:
    out: VirtualInterfaces = {}  # type: ignore[typeddict-item]
    if "virtualInterfaces" in data:
        import aws_sdk_direct_connect.types.virtual_interface_list

        out["virtual_interfaces"] = (
            aws_sdk_direct_connect.types.virtual_interface_list.deserialize_aws_json_1_1(
                data["virtualInterfaces"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
