"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeNodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_id
    import aws_sdk_panorama.types.package_owner_account


class DescribeNodeRequest(TypedDict):
    node_id: "aws_sdk_panorama.types.node_id.NodeId"
    """<p>The node's ID.</p>"""
    owner_account: NotRequired[
        "aws_sdk_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>The account ID of the node's owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNodeRequest:
    out: DescribeNodeRequest = {}  # type: ignore[typeddict-item]
    return out
