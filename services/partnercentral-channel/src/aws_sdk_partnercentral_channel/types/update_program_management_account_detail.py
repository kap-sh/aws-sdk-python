"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#UpdateProgramManagementAccountDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.arn
    import aws_sdk_partnercentral_channel.types.program_management_account_display_name
    import aws_sdk_partnercentral_channel.types.program_management_account_id
    import aws_sdk_partnercentral_channel.types.revision


class UpdateProgramManagementAccountDetail(TypedDict):
    id: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_management_account_id.ProgramManagementAccountId"
    ]
    """<p>The unique identifier of the updated program management account.</p>"""
    arn: NotRequired["aws_sdk_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the updated program management account.</p>"""
    revision: NotRequired["aws_sdk_partnercentral_channel.types.revision.Revision"]
    """<p>The new revision number of the program management account.</p>"""
    display_name: NotRequired[
        "aws_sdk_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
    ]
    """<p>The updated display name of the program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProgramManagementAccountDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProgramManagementAccountDetail:
    out: UpdateProgramManagementAccountDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
