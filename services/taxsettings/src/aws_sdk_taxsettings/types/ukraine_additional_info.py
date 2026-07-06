"""Generated from Smithy shape ``com.amazonaws.taxsettings#UkraineAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.ukraine_trn_type


class UkraineAdditionalInfo(TypedDict, closed=True):
    ukraine_trn_type: "aws_sdk_taxsettings.types.ukraine_trn_type.UkraineTrnType"
    """<p> The tax registration type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UkraineAdditionalInfo) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.ukraine_trn_type

    out["ukraineTrnType"] = aws_sdk_taxsettings.types.ukraine_trn_type.serialize_json(
        value["ukraine_trn_type"]
    )
    return out


def deserialize_json(data: dict) -> UkraineAdditionalInfo:
    out: UkraineAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "ukraineTrnType" in data:
        import aws_sdk_taxsettings.types.ukraine_trn_type

        out["ukraine_trn_type"] = (
            aws_sdk_taxsettings.types.ukraine_trn_type.deserialize_json(
                data["ukraineTrnType"]
            )
        )
    else:
        raise DeserializationError("UkraineAdditionalInfo.ukraine_trn_type required")
    return out
