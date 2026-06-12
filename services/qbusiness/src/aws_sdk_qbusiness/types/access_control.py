"""Generated from Smithy shape ``com.amazonaws.qbusiness#AccessControl``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.member_relation
    import aws_sdk_qbusiness.types.principals

class AccessControl(TypedDict):
    principals: "aws_sdk_qbusiness.types.principals.Principals"
    """<p>Contains a list of principals, where a principal can be either a <code>USER</code> or a <code>GROUP</code>. Each principal can be have the following type of document access: <code>ALLOW</code> or <code>DENY</code>.</p>"""
    member_relation: NotRequired["aws_sdk_qbusiness.types.member_relation.MemberRelation"]
    """<p>Describes the member relation within a principal list.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AccessControl) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.principals
    out["principals"] = aws_sdk_qbusiness.types.principals.serialize_json(value["principals"])
    if "member_relation" in value:
        import aws_sdk_qbusiness.types.member_relation
        out["memberRelation"] = aws_sdk_qbusiness.types.member_relation.serialize_json(value["member_relation"])
    return out


def deserialize_json(data: dict) -> AccessControl:
    out: AccessControl = {}  # type: ignore[typeddict-item]
    if "principals" in data:
        import aws_sdk_qbusiness.types.principals
        out["principals"] = aws_sdk_qbusiness.types.principals.deserialize_json(data["principals"])
    else:
        raise DeserializationError("AccessControl.principals required")
    if "memberRelation" in data:
        import aws_sdk_qbusiness.types.member_relation
        out["member_relation"] = aws_sdk_qbusiness.types.member_relation.deserialize_json(data["memberRelation"])
    return out