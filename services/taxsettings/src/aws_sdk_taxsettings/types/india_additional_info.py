"""Generated from Smithy shape ``com.amazonaws.taxsettings#IndiaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.pan


class IndiaAdditionalInfo(TypedDict, closed=True):
    pan: NotRequired["aws_sdk_taxsettings.types.pan.Pan"]
    """<p> India pan information associated with the account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndiaAdditionalInfo) -> dict:
    out: dict = {}
    if "pan" in value:
        out["pan"] = value["pan"]
    return out


def deserialize_json(data: dict) -> IndiaAdditionalInfo:
    out: IndiaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "pan" in data:
        out["pan"] = data["pan"]
    return out
