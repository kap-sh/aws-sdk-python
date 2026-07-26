"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteVPCConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.vpc_connection_resource_id_unrestricted


class DeleteVPCConnectionRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the account where you want to delete a VPC connection.</p>"""
    vpc_connection_id: "capo_quicksight.types.vpc_connection_resource_id_unrestricted.VPCConnectionResourceIdUnrestricted"
    """<p>The ID of the VPC connection that you're creating. This ID is a unique identifier for each Amazon Web Services Region in an Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVPCConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVPCConnectionRequest:
    out: DeleteVPCConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
