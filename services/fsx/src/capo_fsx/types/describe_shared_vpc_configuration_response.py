"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeSharedVpcConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.verbose_flag


class DescribeSharedVpcConfigurationResponse(TypedDict, closed=True):
    enable_fsx_route_table_updates_from_participant_accounts: NotRequired[
        "capo_fsx.types.verbose_flag.VerboseFlag"
    ]
    """<p>Indicates whether participant accounts can create FSx for ONTAP Multi-AZ file systems in shared subnets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSharedVpcConfigurationResponse) -> dict:
    out: dict = {}
    if "enable_fsx_route_table_updates_from_participant_accounts" in value:
        out["EnableFsxRouteTableUpdatesFromParticipantAccounts"] = value[
            "enable_fsx_route_table_updates_from_participant_accounts"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSharedVpcConfigurationResponse:
    out: DescribeSharedVpcConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "EnableFsxRouteTableUpdatesFromParticipantAccounts" in data:
        out["enable_fsx_route_table_updates_from_participant_accounts"] = data[
            "EnableFsxRouteTableUpdatesFromParticipantAccounts"
        ]
    return out
