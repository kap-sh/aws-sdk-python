"""Generated from Smithy shape ``com.amazonaws.connect#DescribeViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.view_id
    import capo_connect.types.views_instance_id


class DescribeViewRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    view_id: "capo_connect.types.view_id.ViewId"
    """<p>The ViewId of the view. This must be an ARN for Amazon Web Services managed views.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeViewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeViewRequest:
    out: DescribeViewRequest = {}  # type: ignore[typeddict-item]
    return out
