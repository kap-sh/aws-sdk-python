"""Generated from Smithy shape ``com.amazonaws.organizations#ListOutboundResponsibilityTransfersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.next_token
    import aws_sdk_organizations.types.responsibility_transfers


class ListOutboundResponsibilityTransfersResponse(TypedDict, closed=True):
    responsibility_transfers: NotRequired[
        "aws_sdk_organizations.types.responsibility_transfers.ResponsibilityTransfers"
    ]
    """<p>An array of <code>ResponsibilityTransfer</code> objects. Contains details for a transfer.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOutboundResponsibilityTransfersResponse) -> dict:
    out: dict = {}
    if "responsibility_transfers" in value:
        import aws_sdk_organizations.types.responsibility_transfers

        out["ResponsibilityTransfers"] = (
            aws_sdk_organizations.types.responsibility_transfers.serialize_aws_json_1_1(
                value["responsibility_transfers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOutboundResponsibilityTransfersResponse:
    out: ListOutboundResponsibilityTransfersResponse = {}  # type: ignore[typeddict-item]
    if "ResponsibilityTransfers" in data:
        import aws_sdk_organizations.types.responsibility_transfers

        out["responsibility_transfers"] = (
            aws_sdk_organizations.types.responsibility_transfers.deserialize_aws_json_1_1(
                data["ResponsibilityTransfers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
