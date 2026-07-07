"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkFrameworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.network_fabric_configuration


class NetworkFrameworkConfiguration(TypedDict, closed=True):
    fabric: NotRequired[
        "aws_sdk_managedblockchain.types.network_fabric_configuration.NetworkFabricConfiguration"
    ]
    """<p> Hyperledger Fabric configuration properties for a Managed Blockchain network that uses Hyperledger Fabric. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFrameworkConfiguration) -> dict:
    out: dict = {}
    if "fabric" in value:
        import aws_sdk_managedblockchain.types.network_fabric_configuration

        out["Fabric"] = (
            aws_sdk_managedblockchain.types.network_fabric_configuration.serialize_json(
                value["fabric"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkFrameworkConfiguration:
    out: NetworkFrameworkConfiguration = {}  # type: ignore[typeddict-item]
    if "Fabric" in data:
        import aws_sdk_managedblockchain.types.network_fabric_configuration

        out["fabric"] = (
            aws_sdk_managedblockchain.types.network_fabric_configuration.deserialize_json(
                data["Fabric"]
            )
        )
    return out
