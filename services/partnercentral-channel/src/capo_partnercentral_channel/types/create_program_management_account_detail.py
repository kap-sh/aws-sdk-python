"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateProgramManagementAccountDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.arn
    import capo_partnercentral_channel.types.program_management_account_id


class CreateProgramManagementAccountDetail(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_channel.types.program_management_account_id.ProgramManagementAccountId"
    ]
    """<p>The unique identifier of the created program management account.</p>"""
    arn: NotRequired["capo_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the created program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProgramManagementAccountDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProgramManagementAccountDetail:
    out: CreateProgramManagementAccountDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
