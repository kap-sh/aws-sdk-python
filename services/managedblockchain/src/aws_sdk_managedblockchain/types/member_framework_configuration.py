"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberFrameworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.member_fabric_configuration


class MemberFrameworkConfiguration(TypedDict):
    fabric: NotRequired[
        "aws_sdk_managedblockchain.types.member_fabric_configuration.MemberFabricConfiguration"
    ]
    """<p>Attributes of Hyperledger Fabric for a member on a Managed Blockchain network that uses Hyperledger Fabric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFrameworkConfiguration) -> dict:
    out: dict = {}
    if "fabric" in value:
        import aws_sdk_managedblockchain.types.member_fabric_configuration

        out["Fabric"] = (
            aws_sdk_managedblockchain.types.member_fabric_configuration.serialize_json(
                value["fabric"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberFrameworkConfiguration:
    out: MemberFrameworkConfiguration = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import aws_sdk_managedblockchain.types.member_fabric_configuration

        out["fabric"] = (
            aws_sdk_managedblockchain.types.member_fabric_configuration.deserialize_json(
                data["Fabric"]
            )
        )
    return out
