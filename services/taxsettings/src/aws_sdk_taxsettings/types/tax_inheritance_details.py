"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxInheritanceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_id
    import aws_sdk_taxsettings.types.inheritance_obtained_reason


class TaxInheritanceDetails(TypedDict):
    parent_entity_id: NotRequired["aws_sdk_taxsettings.types.account_id.AccountId"]
    """<p> Tax inheritance parent account information associated with the account. </p>"""
    inheritance_obtained_reason: NotRequired[
        "aws_sdk_taxsettings.types.inheritance_obtained_reason.InheritanceObtainedReason"
    ]
    """<p> Tax inheritance reason information associated with the account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxInheritanceDetails) -> dict:
    out: dict = {}
    if "parent_entity_id" in value:
        out["parentEntityId"] = value["parent_entity_id"]
    if "inheritance_obtained_reason" in value:
        out["inheritanceObtainedReason"] = value["inheritance_obtained_reason"]
    return out


def deserialize_json(data: dict) -> TaxInheritanceDetails:
    out: TaxInheritanceDetails = {}  # type: ignore[typeddict-item]
    if "parentEntityId" in data:
        out["parent_entity_id"] = data["parentEntityId"]
    if "inheritanceObtainedReason" in data:
        out["inheritance_obtained_reason"] = data["inheritanceObtainedReason"]
    return out
