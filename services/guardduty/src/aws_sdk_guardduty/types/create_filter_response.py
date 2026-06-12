"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateFilterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.filter_name


class CreateFilterResponse(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.filter_name.FilterName"]
    """<p>The name of the successfully created filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFilterResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateFilterResponse:
    out: CreateFilterResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
