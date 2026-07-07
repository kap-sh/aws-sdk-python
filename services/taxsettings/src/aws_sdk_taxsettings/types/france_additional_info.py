"""Generated from Smithy shape ``com.amazonaws.taxsettings#FranceAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.siren_number


class FranceAdditionalInfo(TypedDict, closed=True):
    siren_number: "aws_sdk_taxsettings.types.siren_number.SirenNumber"
    """<p>The SIREN number for the company in France. Must be a 9-digit number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FranceAdditionalInfo) -> dict:
    out: dict = {}
    out["sirenNumber"] = value["siren_number"]
    return out


def deserialize_json(data: dict) -> FranceAdditionalInfo:
    out: FranceAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "sirenNumber" in data:
        out["siren_number"] = data["sirenNumber"]
    else:
        raise DeserializationError("FranceAdditionalInfo.siren_number required")
    return out
