"""Generated from Smithy shape ``com.amazonaws.organizations#ListOrganizationalUnitsForParentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.next_token
    import capo_organizations.types.organizational_units


class ListOrganizationalUnitsForParentResponse(TypedDict, closed=True):
    organizational_units: NotRequired[
        "capo_organizations.types.organizational_units.OrganizationalUnits"
    ]
    """<p>A list of the OUs in the specified root or parent OU.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOrganizationalUnitsForParentResponse) -> dict:
    out: dict = {}
    if "organizational_units" in value:
        import capo_organizations.types.organizational_units

        out["OrganizationalUnits"] = (
            capo_organizations.types.organizational_units.serialize_aws_json_1_1(
                value["organizational_units"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOrganizationalUnitsForParentResponse:
    out: ListOrganizationalUnitsForParentResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationalUnits" in data:
        import capo_organizations.types.organizational_units

        out["organizational_units"] = (
            capo_organizations.types.organizational_units.deserialize_aws_json_1_1(
                data["OrganizationalUnits"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
