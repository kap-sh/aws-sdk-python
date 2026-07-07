"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateProgramManagementAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.create_program_management_account_detail


class CreateProgramManagementAccountResponse(TypedDict, closed=True):
    program_management_account_detail: NotRequired[
        "aws_sdk_partnercentral_channel.types.create_program_management_account_detail.CreateProgramManagementAccountDetail"
    ]
    """<p>Details of the created program management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProgramManagementAccountResponse) -> dict:
    out: dict = {}
    if "program_management_account_detail" in value:
        import aws_sdk_partnercentral_channel.types.create_program_management_account_detail

        out["programManagementAccountDetail"] = (
            aws_sdk_partnercentral_channel.types.create_program_management_account_detail.serialize_aws_json_1_0(
                value["program_management_account_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProgramManagementAccountResponse:
    out: CreateProgramManagementAccountResponse = {}  # type: ignore[typeddict-item]
    if "programManagementAccountDetail" in data:
        import aws_sdk_partnercentral_channel.types.create_program_management_account_detail

        out["program_management_account_detail"] = (
            aws_sdk_partnercentral_channel.types.create_program_management_account_detail.deserialize_aws_json_1_0(
                data["programManagementAccountDetail"]
            )
        )
    return out
