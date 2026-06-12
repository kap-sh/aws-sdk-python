"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeOrganizationalUnitRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.organizational_unit_id


class DescribeOrganizationalUnitRequest(TypedDict):
    organizational_unit_id: (
        "aws_sdk_organizations.types.organizational_unit_id.OrganizationalUnitId"
    )
    """<p>ID for the organizational unit that you want details about. You can get the ID from the <a>ListOrganizationalUnitsForParent</a> operation.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for an organizational unit ID string requires \"ou-\" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second \"-\" dash and from 8 to 32 additional lowercase letters or digits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrganizationalUnitRequest) -> dict:
    out: dict = {}
    out["OrganizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOrganizationalUnitRequest:
    out: DescribeOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationalUnitId" in data:
        out["organizational_unit_id"] = data["OrganizationalUnitId"]
    else:
        raise DeserializationError(
            "DescribeOrganizationalUnitRequest.organizational_unit_id required"
        )
    return out
