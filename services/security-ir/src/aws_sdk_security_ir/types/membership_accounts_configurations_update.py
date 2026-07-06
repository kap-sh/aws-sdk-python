"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipAccountsConfigurationsUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.organizational_units


class MembershipAccountsConfigurationsUpdate(TypedDict, closed=True):
    cover_entire_organization: NotRequired["bool"]
    """<p>The <code>coverEntireOrganization</code> field is a boolean value that determines whether the membership configuration should be applied across the entire Amazon Web Services Organization. </p> <p>When set to <code>true</code>, the configuration will be applied to all accounts within the organization. When set to <code>false</code>, the configuration will only apply to specifically designated accounts. </p>"""
    organizational_units_to_add: NotRequired[
        "aws_sdk_security_ir.types.organizational_units.OrganizationalUnits"
    ]
    """<p>A list of organizational unit IDs to add to the membership configuration. Each organizational unit ID must match the pattern <code>ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}</code>. </p> <p>The list must contain between 1 and 5 organizational unit IDs.</p>"""
    organizational_units_to_remove: NotRequired[
        "aws_sdk_security_ir.types.organizational_units.OrganizationalUnits"
    ]
    """<p>A list of organizational unit IDs to remove from the membership configuration. Each organizational unit ID must match the pattern <code>ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}</code>. </p> <p>The list must contain between 1 and 5 organizational unit IDs per invocation of the API request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipAccountsConfigurationsUpdate) -> dict:
    out: dict = {}
    if "cover_entire_organization" in value:
        out["coverEntireOrganization"] = value["cover_entire_organization"]
    if "organizational_units_to_add" in value:
        import aws_sdk_security_ir.types.organizational_units

        out["organizationalUnitsToAdd"] = (
            aws_sdk_security_ir.types.organizational_units.serialize_json(
                value["organizational_units_to_add"]
            )
        )
    if "organizational_units_to_remove" in value:
        import aws_sdk_security_ir.types.organizational_units

        out["organizationalUnitsToRemove"] = (
            aws_sdk_security_ir.types.organizational_units.serialize_json(
                value["organizational_units_to_remove"]
            )
        )
    return out


def deserialize_json(data: dict) -> MembershipAccountsConfigurationsUpdate:
    out: MembershipAccountsConfigurationsUpdate = {}  # type: ignore[typeddict-item]
    if "coverEntireOrganization" in data:
        out["cover_entire_organization"] = data["coverEntireOrganization"]
    if "organizationalUnitsToAdd" in data:
        import aws_sdk_security_ir.types.organizational_units

        out["organizational_units_to_add"] = (
            aws_sdk_security_ir.types.organizational_units.deserialize_json(
                data["organizationalUnitsToAdd"]
            )
        )
    if "organizationalUnitsToRemove" in data:
        import aws_sdk_security_ir.types.organizational_units

        out["organizational_units_to_remove"] = (
            aws_sdk_security_ir.types.organizational_units.deserialize_json(
                data["organizationalUnitsToRemove"]
            )
        )
    return out
