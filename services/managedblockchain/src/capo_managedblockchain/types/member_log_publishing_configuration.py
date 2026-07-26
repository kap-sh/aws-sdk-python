"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberLogPublishingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.member_fabric_log_publishing_configuration


class MemberLogPublishingConfiguration(TypedDict, closed=True):
    fabric: NotRequired[
        "capo_managedblockchain.types.member_fabric_log_publishing_configuration.MemberFabricLogPublishingConfiguration"
    ]
    """<p>Configuration properties for logging events associated with a member of a Managed Blockchain network using the Hyperledger Fabric framework.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberLogPublishingConfiguration) -> dict:
    out: dict = {}
    if "fabric" in value:
        import capo_managedblockchain.types.member_fabric_log_publishing_configuration

        out["Fabric"] = (
            capo_managedblockchain.types.member_fabric_log_publishing_configuration.serialize_json(
                value["fabric"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberLogPublishingConfiguration:
    out: MemberLogPublishingConfiguration = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import capo_managedblockchain.types.member_fabric_log_publishing_configuration

        out["fabric"] = (
            capo_managedblockchain.types.member_fabric_log_publishing_configuration.deserialize_json(
                data["Fabric"]
            )
        )
    return out
