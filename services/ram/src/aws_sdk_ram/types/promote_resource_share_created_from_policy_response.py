"""Generated from Smithy shape ``com.amazonaws.ram#PromoteResourceShareCreatedFromPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean


class PromoteResourceShareCreatedFromPolicyResponse(TypedDict, closed=True):
    return_value: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>A return value of <code>true</code> indicates that the request succeeded. A value of <code>false</code> indicates that the request failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromoteResourceShareCreatedFromPolicyResponse) -> dict:
    out: dict = {}
    if "return_value" in value:
        out["returnValue"] = value["return_value"]
    return out


def deserialize_json(data: dict) -> PromoteResourceShareCreatedFromPolicyResponse:
    out: PromoteResourceShareCreatedFromPolicyResponse = {}  # type: ignore[typeddict-item]
    if "returnValue" in data:
        out["return_value"] = data["returnValue"]
    return out
