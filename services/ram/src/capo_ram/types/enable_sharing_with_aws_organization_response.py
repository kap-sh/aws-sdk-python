"""Generated from Smithy shape ``com.amazonaws.ram#EnableSharingWithAwsOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.boolean


class EnableSharingWithAwsOrganizationResponse(TypedDict, closed=True):
    return_value: NotRequired["capo_ram.types.boolean.Boolean"]
    """<p>A return value of <code>true</code> indicates that the request succeeded. A value of <code>false</code> indicates that the request failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableSharingWithAwsOrganizationResponse) -> dict:
    out: dict = {}
    if "return_value" in value:
        out["returnValue"] = value["return_value"]
    return out


def deserialize_json(data: dict) -> EnableSharingWithAwsOrganizationResponse:
    out: EnableSharingWithAwsOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "returnValue" in data:
        out["return_value"] = data["returnValue"]
    return out
