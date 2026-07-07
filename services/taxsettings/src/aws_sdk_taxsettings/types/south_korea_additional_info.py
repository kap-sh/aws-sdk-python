"""Generated from Smithy shape ``com.amazonaws.taxsettings#SouthKoreaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.business_representative_name
    import aws_sdk_taxsettings.types.item_of_business
    import aws_sdk_taxsettings.types.line_of_business


class SouthKoreaAdditionalInfo(TypedDict, closed=True):
    business_representative_name: "aws_sdk_taxsettings.types.business_representative_name.BusinessRepresentativeName"
    """<p>The business legal name based on the most recently uploaded tax registration certificate.</p>"""
    line_of_business: "aws_sdk_taxsettings.types.line_of_business.LineOfBusiness"
    """<p>Line of business based on the most recently uploaded tax registration certificate.</p>"""
    item_of_business: "aws_sdk_taxsettings.types.item_of_business.ItemOfBusiness"
    """<p>Item of business based on the most recently uploaded tax registration certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SouthKoreaAdditionalInfo) -> dict:
    out: dict = {}
    out["businessRepresentativeName"] = value["business_representative_name"]
    out["lineOfBusiness"] = value["line_of_business"]
    out["itemOfBusiness"] = value["item_of_business"]
    return out


def deserialize_json(data: dict) -> SouthKoreaAdditionalInfo:
    out: SouthKoreaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "businessRepresentativeName" in data:
        out["business_representative_name"] = data["businessRepresentativeName"]
    else:
        raise DeserializationError(
            "SouthKoreaAdditionalInfo.business_representative_name required"
        )
    if "lineOfBusiness" in data:
        out["line_of_business"] = data["lineOfBusiness"]
    else:
        raise DeserializationError("SouthKoreaAdditionalInfo.line_of_business required")
    if "itemOfBusiness" in data:
        out["item_of_business"] = data["itemOfBusiness"]
    else:
        raise DeserializationError("SouthKoreaAdditionalInfo.item_of_business required")
    return out
