"""Generated from Smithy shape ``com.amazonaws.connect#DeleteViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.view_id
    import aws_sdk_connect.types.views_instance_id


class DeleteViewRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    view_id: "aws_sdk_connect.types.view_id.ViewId"
    """<p>The identifier of the view. Both <code>ViewArn</code> and <code>ViewId</code> can be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteViewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteViewRequest:
    out: DeleteViewRequest = {}  # type: ignore[typeddict-item]
    return out
