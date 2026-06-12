"""Generated from Smithy shape ``com.amazonaws.schemas#UpdateDiscovererRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__boolean
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.__string_min0_max256


class UpdateDiscovererRequest(TypedDict):
    description: NotRequired[
        "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
    ]
    """<p>The description of the discoverer to update.</p>"""
    discoverer_id: "aws_sdk_schemas.types.__string.__string"
    """<p>The ID of the discoverer.</p>"""
    cross_account: NotRequired["aws_sdk_schemas.types.__boolean.__boolean"]
    """<p>Support discovery of schemas in events sent to the bus from another account. (default: true)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDiscovererRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "cross_account" in value:
        out["CrossAccount"] = value["cross_account"]
    return out


def deserialize_json(data: dict) -> UpdateDiscovererRequest:
    out: UpdateDiscovererRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CrossAccount" in data:
        out["cross_account"] = data["CrossAccount"]
    return out
