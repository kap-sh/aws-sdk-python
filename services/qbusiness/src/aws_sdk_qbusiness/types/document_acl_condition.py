"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.document_acl_groups
    import aws_sdk_qbusiness.types.document_acl_users
    import aws_sdk_qbusiness.types.member_relation


class DocumentAclCondition(TypedDict, closed=True):
    member_relation: NotRequired[
        "aws_sdk_qbusiness.types.member_relation.MemberRelation"
    ]
    """<p>The logical relation between members in the condition, determining how multiple user or group conditions are combined.</p>"""
    users: NotRequired["aws_sdk_qbusiness.types.document_acl_users.DocumentAclUsers"]
    """<p>An array of user identifiers that this condition applies to. Users listed here are subject to the access rule defined by this condition.</p>"""
    groups: NotRequired["aws_sdk_qbusiness.types.document_acl_groups.DocumentAclGroups"]
    """<p>An array of group identifiers that this condition applies to. Groups listed here are subject to the access rule defined by this condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclCondition) -> dict:
    out: dict = {}
    if "member_relation" in value:
        import aws_sdk_qbusiness.types.member_relation

        out["memberRelation"] = aws_sdk_qbusiness.types.member_relation.serialize_json(
            value["member_relation"]
        )
    if "users" in value:
        import aws_sdk_qbusiness.types.document_acl_users

        out["users"] = aws_sdk_qbusiness.types.document_acl_users.serialize_json(
            value["users"]
        )
    if "groups" in value:
        import aws_sdk_qbusiness.types.document_acl_groups

        out["groups"] = aws_sdk_qbusiness.types.document_acl_groups.serialize_json(
            value["groups"]
        )
    return out


def deserialize_json(data: dict) -> DocumentAclCondition:
    out: DocumentAclCondition = {}  # type: ignore[typeddict-item]
    if "memberRelation" in data:
        import aws_sdk_qbusiness.types.member_relation

        out["member_relation"] = (
            aws_sdk_qbusiness.types.member_relation.deserialize_json(
                data["memberRelation"]
            )
        )
    if "users" in data:
        import aws_sdk_qbusiness.types.document_acl_users

        out["users"] = aws_sdk_qbusiness.types.document_acl_users.deserialize_json(
            data["users"]
        )
    if "groups" in data:
        import aws_sdk_qbusiness.types.document_acl_groups

        out["groups"] = aws_sdk_qbusiness.types.document_acl_groups.deserialize_json(
            data["groups"]
        )
    return out
