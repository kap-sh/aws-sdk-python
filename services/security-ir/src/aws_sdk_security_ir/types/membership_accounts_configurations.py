"""Generated from Smithy shape ``com.amazonaws.securityir#MembershipAccountsConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.organizational_units


class MembershipAccountsConfigurations(TypedDict, closed=True):
    cover_entire_organization: NotRequired["bool"]
    """<p>The <code>coverEntireOrganization</code> field is a boolean value that determines whether the membership configuration applies to all accounts within an Amazon Web Services Organization. </p> <p>When set to <code>true</code>, the configuration will be applied across all accounts in the organization. When set to <code>false</code>, the configuration will only apply to specifically designated accounts under the AWS Organizational Units specificied. </p>"""
    organizational_units: NotRequired[
        "aws_sdk_security_ir.types.organizational_units.OrganizationalUnits"
    ]
    """<p>A list of organizational unit IDs that follow the pattern <code>ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}</code>. These IDs represent the organizational units within an Amazon Web Services Organizations structure that are covered by the membership. </p> <p>Each organizational unit ID in the list must:</p> <ul> <li> <p>Begin with the prefix 'ou-'</p> </li> <li> <p>Contain between 4 and 32 alphanumeric characters in the first segment</p> </li> <li> <p>Contain between 8 and 32 alphanumeric characters in the second segment</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipAccountsConfigurations) -> dict:
    out: dict = {}
    if "cover_entire_organization" in value:
        out["coverEntireOrganization"] = value["cover_entire_organization"]
    if "organizational_units" in value:
        import aws_sdk_security_ir.types.organizational_units

        out["organizationalUnits"] = (
            aws_sdk_security_ir.types.organizational_units.serialize_json(
                value["organizational_units"]
            )
        )
    return out


def deserialize_json(data: dict) -> MembershipAccountsConfigurations:
    out: MembershipAccountsConfigurations = {}  # type: ignore[typeddict-item]
    if "coverEntireOrganization" in data:
        out["cover_entire_organization"] = data["coverEntireOrganization"]
    if "organizationalUnits" in data:
        import aws_sdk_security_ir.types.organizational_units

        out["organizational_units"] = (
            aws_sdk_security_ir.types.organizational_units.deserialize_json(
                data["organizationalUnits"]
            )
        )
    return out
