"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberFabricLogPublishingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.log_configurations


class MemberFabricLogPublishingConfiguration(TypedDict):
    ca_logs: NotRequired[
        "aws_sdk_managedblockchain.types.log_configurations.LogConfigurations"
    ]
    """<p>Configuration properties for logging events associated with a member's Certificate Authority (CA). CA logs help you determine when a member in your account joins the network, or when new peers register with a member CA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFabricLogPublishingConfiguration) -> dict:
    out: dict = {}
    if "ca_logs" in value:
        import aws_sdk_managedblockchain.types.log_configurations

        out["CaLogs"] = (
            aws_sdk_managedblockchain.types.log_configurations.serialize_json(
                value["ca_logs"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemberFabricLogPublishingConfiguration:
    out: MemberFabricLogPublishingConfiguration = {}  # type: ignore[typeddict-item]
    if "CaLogs" in data:
        import aws_sdk_managedblockchain.types.log_configurations

        out["ca_logs"] = (
            aws_sdk_managedblockchain.types.log_configurations.deserialize_json(
                data["CaLogs"]
            )
        )
    return out
