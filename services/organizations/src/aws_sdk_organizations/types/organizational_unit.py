"""Generated from Smithy shape ``com.amazonaws.organizations#OrganizationalUnit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.organizational_unit_arn
    import aws_sdk_organizations.types.organizational_unit_id
    import aws_sdk_organizations.types.organizational_unit_name
    import aws_sdk_organizations.types.path


class OrganizationalUnit(TypedDict):
    id: NotRequired[
        "aws_sdk_organizations.types.organizational_unit_id.OrganizationalUnitId"
    ]
    r"""<p>The unique identifier (ID) associated with this OU. The ID is unique to the organization only.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for an organizational unit ID string requires \"ou-\" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second \"-\" dash and from 8 to 32 additional lowercase letters or digits.</p>"""
    arn: NotRequired[
        "aws_sdk_organizations.types.organizational_unit_arn.OrganizationalUnitArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of this OU.</p> <p>For more information about ARNs in Organizations, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies\">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    name: NotRequired[
        "aws_sdk_organizations.types.organizational_unit_name.OrganizationalUnitName"
    ]
    r"""<p>The friendly name of this OU.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    path: NotRequired["aws_sdk_organizations.types.path.Path"]
    """<p>The path in the organization where this OU exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationalUnit) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationalUnit:
    out: OrganizationalUnit = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Path" in data:
        out["path"] = data["Path"]
    return out
