"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTrunkInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.trunk_interface_association


class AssociateTrunkInterfaceResult(TypedDict):
    interface_association: NotRequired[
        "aws_sdk_ec2.types.trunk_interface_association.TrunkInterfaceAssociation"
    ]
    """<p>Information about the association between the trunk network interface and branch network interface.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
