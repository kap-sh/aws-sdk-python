"""Generated from Smithy shape ``com.amazonaws.managedblockchain#UpdateMemberInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.member_log_publishing_configuration
    import aws_sdk_managedblockchain.types.resource_id_string


class UpdateMemberInput(TypedDict):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the Managed Blockchain network to which the member belongs.</p>"""
    member_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member.</p>"""
    log_publishing_configuration: NotRequired[
        "aws_sdk_managedblockchain.types.member_log_publishing_configuration.MemberLogPublishingConfiguration"
    ]
    """<p>Configuration properties for publishing to Amazon CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMemberInput) -> dict:
    out: dict = {}
    if "log_publishing_configuration" in value:
        import aws_sdk_managedblockchain.types.member_log_publishing_configuration

        out["LogPublishingConfiguration"] = (
            aws_sdk_managedblockchain.types.member_log_publishing_configuration.serialize_json(
                value["log_publishing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMemberInput:
    out: UpdateMemberInput = {}  # type: ignore[typeddict-item]
    if "LogPublishingConfiguration" in data:
        import aws_sdk_managedblockchain.types.member_log_publishing_configuration

        out["log_publishing_configuration"] = (
            aws_sdk_managedblockchain.types.member_log_publishing_configuration.deserialize_json(
                data["LogPublishingConfiguration"]
            )
        )
    return out
