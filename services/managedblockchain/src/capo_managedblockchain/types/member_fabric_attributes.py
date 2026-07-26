"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberFabricAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.string
    import capo_managedblockchain.types.username_string


class MemberFabricAttributes(TypedDict, closed=True):
    admin_username: NotRequired[
        "capo_managedblockchain.types.username_string.UsernameString"
    ]
    """<p>The user name for the initial administrator user for the member.</p>"""
    ca_endpoint: NotRequired["capo_managedblockchain.types.string.String"]
    """<p>The endpoint used to access the member's certificate authority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFabricAttributes) -> dict:
    out: dict = {}
    if "admin_username" in value:
        out["AdminUsername"] = value["admin_username"]
    if "ca_endpoint" in value:
        out["CaEndpoint"] = value["ca_endpoint"]
    return out


def deserialize_json(data: dict) -> MemberFabricAttributes:
    out: MemberFabricAttributes = {}  # type: ignore[typeddict-item]
    if "AdminUsername" in data:
        out["admin_username"] = data["AdminUsername"]
    if "CaEndpoint" in data:
        out["ca_endpoint"] = data["CaEndpoint"]
    return out
