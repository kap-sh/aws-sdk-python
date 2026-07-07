"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberFrameworkAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.member_fabric_attributes


class MemberFrameworkAttributes(TypedDict, closed=True):
    fabric: NotRequired[
        "aws_sdk_managedblockchain.types.member_fabric_attributes.MemberFabricAttributes"
    ]
    """<p>Attributes of Hyperledger Fabric relevant to a member on a Managed Blockchain network that uses Hyperledger Fabric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFrameworkAttributes) -> dict:
    out: dict = {}
    if "fabric" in value:
        import aws_sdk_managedblockchain.types.member_fabric_attributes

        out["Fabric"] = (
            aws_sdk_managedblockchain.types.member_fabric_attributes.serialize_json(
                value["fabric"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberFrameworkAttributes:
    out: MemberFrameworkAttributes = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import aws_sdk_managedblockchain.types.member_fabric_attributes

        out["fabric"] = (
            aws_sdk_managedblockchain.types.member_fabric_attributes.deserialize_json(
                data["Fabric"]
            )
        )
    return out
