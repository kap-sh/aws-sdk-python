"""Generated from Smithy shape ``com.amazonaws.organizations#Child``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.child_id
    import aws_sdk_organizations.types.child_type


class Child(TypedDict, closed=True):
    id: NotRequired["aws_sdk_organizations.types.child_id.ChildId"]
    r"""<p>The unique identifier (ID) of this child entity.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for a child ID string requires one of the following:</p> <ul> <li> <p> <b>Account</b> - A string that consists of exactly 12 digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with \"ou-\" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second \"-\" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""
    type: NotRequired["aws_sdk_organizations.types.child_type.ChildType"]
    """<p>The type of this child entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Child) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import aws_sdk_organizations.types.child_type

        out["Type"] = aws_sdk_organizations.types.child_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Child:
    out: Child = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_organizations.types.child_type

        out["type"] = aws_sdk_organizations.types.child_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
