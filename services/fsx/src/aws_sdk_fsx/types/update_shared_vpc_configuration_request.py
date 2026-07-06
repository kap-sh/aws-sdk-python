"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSharedVpcConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.verbose_flag


class UpdateSharedVpcConfigurationRequest(TypedDict, closed=True):
    enable_fsx_route_table_updates_from_participant_accounts: NotRequired[
        "aws_sdk_fsx.types.verbose_flag.VerboseFlag"
    ]
    """<p>Specifies whether participant accounts can create FSx for ONTAP Multi-AZ file systems in shared subnets. Set to <code>true</code> to enable or <code>false</code> to disable.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSharedVpcConfigurationRequest) -> dict:
    out: dict = {}
    if "enable_fsx_route_table_updates_from_participant_accounts" in value:
        out["EnableFsxRouteTableUpdatesFromParticipantAccounts"] = value[
            "enable_fsx_route_table_updates_from_participant_accounts"
        ]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSharedVpcConfigurationRequest:
    out: UpdateSharedVpcConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "EnableFsxRouteTableUpdatesFromParticipantAccounts" in data:
        out["enable_fsx_route_table_updates_from_participant_accounts"] = data[
            "EnableFsxRouteTableUpdatesFromParticipantAccounts"
        ]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
