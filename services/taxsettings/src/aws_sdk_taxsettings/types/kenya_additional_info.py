"""Generated from Smithy shape ``com.amazonaws.taxsettings#KenyaAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_taxsettings.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.person_type

class KenyaAdditionalInfo(TypedDict):
    person_type: "aws_sdk_taxsettings.types.person_type.PersonType"
    """<p>The legal person or physical person assigned to this TRN in Kenya.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: KenyaAdditionalInfo) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.person_type
    out["personType"] = aws_sdk_taxsettings.types.person_type.serialize_json(value["person_type"])
    return out


def deserialize_json(data: dict) -> KenyaAdditionalInfo:
    out: KenyaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "personType" in data:
        import aws_sdk_taxsettings.types.person_type
        out["person_type"] = aws_sdk_taxsettings.types.person_type.deserialize_json(data["personType"])
    else:
        raise DeserializationError("KenyaAdditionalInfo.person_type required")
    return out