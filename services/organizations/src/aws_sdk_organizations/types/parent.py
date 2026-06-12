"""Generated from Smithy shape ``com.amazonaws.organizations#Parent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.parent_id
    import aws_sdk_organizations.types.parent_type


class Parent(TypedDict):
    id: NotRequired["aws_sdk_organizations.types.parent_id.ParentId"]
    """<p>The unique identifier (ID) of the parent entity.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for a parent ID string requires one of the following:</p> <ul> <li> <p> <b>Root</b> - A string that begins with \"r-\" followed by from 4 to 32 lowercase letters or digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with \"ou-\" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second \"-\" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""
    type: NotRequired["aws_sdk_organizations.types.parent_type.ParentType"]
    """<p>The type of the parent entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parent) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import aws_sdk_organizations.types.parent_type

        out["Type"] = aws_sdk_organizations.types.parent_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Parent:
    out: Parent = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_organizations.types.parent_type

        out["type"] = aws_sdk_organizations.types.parent_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
