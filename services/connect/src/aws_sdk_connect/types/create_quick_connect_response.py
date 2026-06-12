"""Generated from Smithy shape ``com.amazonaws.connect#CreateQuickConnectResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.quick_connect_id


class CreateQuickConnectResponse(TypedDict):
    quick_connect_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the quick connect. </p>"""
    quick_connect_id: NotRequired[
        "aws_sdk_connect.types.quick_connect_id.QuickConnectId"
    ]
    """<p>The identifier for the quick connect. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuickConnectResponse) -> dict:
    out: dict = {}
    if "quick_connect_arn" in value:
        out["QuickConnectARN"] = value["quick_connect_arn"]
    if "quick_connect_id" in value:
        out["QuickConnectId"] = value["quick_connect_id"]
    return out


def deserialize_json(data: dict) -> CreateQuickConnectResponse:
    out: CreateQuickConnectResponse = {}  # type: ignore[typeddict-item]
    if "QuickConnectARN" in data:
        out["quick_connect_arn"] = data["QuickConnectARN"]
    if "QuickConnectId" in data:
        out["quick_connect_id"] = data["QuickConnectId"]
    return out
