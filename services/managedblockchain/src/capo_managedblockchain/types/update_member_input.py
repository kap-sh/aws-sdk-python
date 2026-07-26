"""Generated from Smithy shape ``com.amazonaws.managedblockchain#UpdateMemberInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.member_log_publishing_configuration
    import capo_managedblockchain.types.resource_id_string


class UpdateMemberInput(TypedDict, closed=True):
    network_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the Managed Blockchain network to which the member belongs.</p>"""
    member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member.</p>"""
    log_publishing_configuration: NotRequired[
        "capo_managedblockchain.types.member_log_publishing_configuration.MemberLogPublishingConfiguration"
    ]
    """<p>Configuration properties for publishing to Amazon CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMemberInput) -> dict:
    out: dict = {}
    if "log_publishing_configuration" in value:
        import capo_managedblockchain.types.member_log_publishing_configuration

        out["LogPublishingConfiguration"] = (
            capo_managedblockchain.types.member_log_publishing_configuration.serialize_json(
                value["log_publishing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMemberInput:
    out: UpdateMemberInput = {}  # type: ignore[typeddict-item]
    if "LogPublishingConfiguration" in data:
        import capo_managedblockchain.types.member_log_publishing_configuration

        out["log_publishing_configuration"] = (
            capo_managedblockchain.types.member_log_publishing_configuration.deserialize_json(
                data["LogPublishingConfiguration"]
            )
        )
    return out
