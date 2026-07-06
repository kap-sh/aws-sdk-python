"""Generated from Smithy shape ``com.amazonaws.taxsettings#EgyptAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.date_string
    import aws_sdk_taxsettings.types.unique_identification_number


class EgyptAdditionalInfo(TypedDict, closed=True):
    unique_identification_number: NotRequired[
        "aws_sdk_taxsettings.types.unique_identification_number.UniqueIdentificationNumber"
    ]
    """<p>The unique identification number provided by the Egypt Tax Authority.</p>"""
    unique_identification_number_expiration_date: NotRequired[
        "aws_sdk_taxsettings.types.date_string.DateString"
    ]
    """<p>The expiration date of the unique identification number provided by the Egypt Tax Authority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EgyptAdditionalInfo) -> dict:
    out: dict = {}
    if "unique_identification_number" in value:
        out["uniqueIdentificationNumber"] = value["unique_identification_number"]
    if "unique_identification_number_expiration_date" in value:
        out["uniqueIdentificationNumberExpirationDate"] = value[
            "unique_identification_number_expiration_date"
        ]
    return out


def deserialize_json(data: dict) -> EgyptAdditionalInfo:
    out: EgyptAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "uniqueIdentificationNumber" in data:
        out["unique_identification_number"] = data["uniqueIdentificationNumber"]
    if "uniqueIdentificationNumberExpirationDate" in data:
        out["unique_identification_number_expiration_date"] = data[
            "uniqueIdentificationNumberExpirationDate"
        ]
    return out
