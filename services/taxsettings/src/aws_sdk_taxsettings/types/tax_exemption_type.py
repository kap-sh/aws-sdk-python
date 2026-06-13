"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxExemptionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.authorities
    import aws_sdk_taxsettings.types.display_name
    import aws_sdk_taxsettings.types.generic_string


class TaxExemptionType(TypedDict):
    display_name: NotRequired["aws_sdk_taxsettings.types.display_name.DisplayName"]
    """<p>The tax exemption's type display name. </p>"""
    description: NotRequired["aws_sdk_taxsettings.types.generic_string.GenericString"]
    """<p>The tax exemption's type description. </p>"""
    applicable_jurisdictions: NotRequired[
        "aws_sdk_taxsettings.types.authorities.Authorities"
    ]
    """<p>The tax exemption's applicable jurisdictions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxExemptionType) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "applicable_jurisdictions" in value:
        import aws_sdk_taxsettings.types.authorities

        out["applicableJurisdictions"] = (
            aws_sdk_taxsettings.types.authorities.serialize_json(
                value["applicable_jurisdictions"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaxExemptionType:
    out: TaxExemptionType = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "applicableJurisdictions" in data:
        import aws_sdk_taxsettings.types.authorities

        out["applicable_jurisdictions"] = (
            aws_sdk_taxsettings.types.authorities.deserialize_json(
                data["applicableJurisdictions"]
            )
        )
    return out
