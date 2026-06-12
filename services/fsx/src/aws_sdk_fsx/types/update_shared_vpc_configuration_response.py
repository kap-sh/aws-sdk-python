"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSharedVpcConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.verbose_flag


class UpdateSharedVpcConfigurationResponse(TypedDict):
    enable_fsx_route_table_updates_from_participant_accounts: NotRequired[
        "aws_sdk_fsx.types.verbose_flag.VerboseFlag"
    ]
    """<p>Indicates whether participant accounts can create FSx for ONTAP Multi-AZ file systems in shared subnets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSharedVpcConfigurationResponse) -> dict:
    out: dict = {}
    if "enable_fsx_route_table_updates_from_participant_accounts" in value:
        out["EnableFsxRouteTableUpdatesFromParticipantAccounts"] = value[
            "enable_fsx_route_table_updates_from_participant_accounts"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSharedVpcConfigurationResponse:
    out: UpdateSharedVpcConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "EnableFsxRouteTableUpdatesFromParticipantAccounts" in data:
        out["enable_fsx_route_table_updates_from_participant_accounts"] = data[
            "EnableFsxRouteTableUpdatesFromParticipantAccounts"
        ]
    return out
