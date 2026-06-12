"""Generated from Smithy shape ``com.amazonaws.taxsettings#GeorgiaAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_taxsettings.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.person_type

class GeorgiaAdditionalInfo(TypedDict):
    person_type: "aws_sdk_taxsettings.types.person_type.PersonType"
    """<p> The legal person or physical person assigned to this TRN in Georgia. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GeorgiaAdditionalInfo) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.person_type
    out["personType"] = aws_sdk_taxsettings.types.person_type.serialize_json(value["person_type"])
    return out


def deserialize_json(data: dict) -> GeorgiaAdditionalInfo:
    out: GeorgiaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "personType" in data:
        import aws_sdk_taxsettings.types.person_type
        out["person_type"] = aws_sdk_taxsettings.types.person_type.deserialize_json(data["personType"])
    else:
        raise DeserializationError("GeorgiaAdditionalInfo.person_type required")
    return out