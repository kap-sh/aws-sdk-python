"""Generated from Smithy shape ``com.amazonaws.lambda#AddPermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.string


class AddPermissionResponse(TypedDict, closed=True):
    statement: NotRequired["capo_lambda.types.string.String"]
    """<p>The permission statement that's added to the function policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPermissionResponse) -> dict:
    out: dict = {}
    if "statement" in value:
        out["Statement"] = value["statement"]
    return out


def deserialize_json(data: dict) -> AddPermissionResponse:
    out: AddPermissionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Statement") is not None:
        out["statement"] = data["Statement"]
    return out
