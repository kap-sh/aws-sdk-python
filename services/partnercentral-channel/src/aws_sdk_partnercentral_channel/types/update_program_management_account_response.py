"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#UpdateProgramManagementAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.update_program_management_account_detail


class UpdateProgramManagementAccountResponse(TypedDict):
    program_management_account_detail: NotRequired[
        "aws_sdk_partnercentral_channel.types.update_program_management_account_detail.UpdateProgramManagementAccountDetail"
    ]
    """<p>Details of the updated program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProgramManagementAccountResponse) -> dict:
    out: dict = {}
    if "program_management_account_detail" in value:
        import aws_sdk_partnercentral_channel.types.update_program_management_account_detail

        out["programManagementAccountDetail"] = (
            aws_sdk_partnercentral_channel.types.update_program_management_account_detail.serialize_aws_json_1_0(
                value["program_management_account_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProgramManagementAccountResponse:
    out: UpdateProgramManagementAccountResponse = {}  # type: ignore[typeddict-item]
    if "programManagementAccountDetail" in data:
        import aws_sdk_partnercentral_channel.types.update_program_management_account_detail

        out["program_management_account_detail"] = (
            aws_sdk_partnercentral_channel.types.update_program_management_account_detail.deserialize_aws_json_1_0(
                data["programManagementAccountDetail"]
            )
        )
    return out
