"""Generated from Smithy shape ``com.amazonaws.lambda#AddPermissionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class AddPermissionResponse(TypedDict):
    statement: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The permission statement that's added to the function policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPermissionResponse) -> dict:
    out: dict = {}
    if "statement" in value:
        out["Statement"] = value["statement"]
    return out


def deserialize_json(data: dict) -> AddPermissionResponse:
    out: AddPermissionResponse = {}  # type: ignore[typeddict-item]
    if "Statement" in data:
        out["statement"] = data["Statement"]
    return out
