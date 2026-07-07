"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_acl_conditions
    import aws_sdk_qbusiness.types.member_relation


class DocumentAclMembership(TypedDict, closed=True):
    member_relation: NotRequired[
        "aws_sdk_qbusiness.types.member_relation.MemberRelation"
    ]
    """<p>The logical relation between members in the membership rule, determining how multiple conditions are combined.</p>"""
    conditions: NotRequired[
        "aws_sdk_qbusiness.types.document_acl_conditions.DocumentAclConditions"
    ]
    """<p>An array of conditions that define the membership rules. Each condition specifies criteria for users or groups to be included in this membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclMembership) -> dict:
    out: dict = {}
    if "member_relation" in value:
        import aws_sdk_qbusiness.types.member_relation

        out["memberRelation"] = aws_sdk_qbusiness.types.member_relation.serialize_json(
            value["member_relation"]
        )
    if "conditions" in value:
        import aws_sdk_qbusiness.types.document_acl_conditions

        out["conditions"] = (
            aws_sdk_qbusiness.types.document_acl_conditions.serialize_json(
                value["conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentAclMembership:
    out: DocumentAclMembership = {}  # type: ignore[typeddict-item]
    if "memberRelation" in data:
        import aws_sdk_qbusiness.types.member_relation

        out["member_relation"] = (
            aws_sdk_qbusiness.types.member_relation.deserialize_json(
                data["memberRelation"]
            )
        )
    if "conditions" in data:
        import aws_sdk_qbusiness.types.document_acl_conditions

        out["conditions"] = (
            aws_sdk_qbusiness.types.document_acl_conditions.deserialize_json(
                data["conditions"]
            )
        )
    return out
