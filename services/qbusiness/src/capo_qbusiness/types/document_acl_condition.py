"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAclCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.document_acl_groups
    import capo_qbusiness.types.document_acl_users
    import capo_qbusiness.types.member_relation


class DocumentAclCondition(TypedDict, closed=True):
    member_relation: NotRequired["capo_qbusiness.types.member_relation.MemberRelation"]
    """<p>The logical relation between members in the condition, determining how multiple user or group conditions are combined.</p>"""
    users: NotRequired["capo_qbusiness.types.document_acl_users.DocumentAclUsers"]
    """<p>An array of user identifiers that this condition applies to. Users listed here are subject to the access rule defined by this condition.</p>"""
    groups: NotRequired["capo_qbusiness.types.document_acl_groups.DocumentAclGroups"]
    """<p>An array of group identifiers that this condition applies to. Groups listed here are subject to the access rule defined by this condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAclCondition) -> dict:
    out: dict = {}
    if "member_relation" in value:
        import capo_qbusiness.types.member_relation

        out["memberRelation"] = capo_qbusiness.types.member_relation.serialize_json(
            value["member_relation"]
        )
    if "users" in value:
        import capo_qbusiness.types.document_acl_users

        out["users"] = capo_qbusiness.types.document_acl_users.serialize_json(
            value["users"]
        )
    if "groups" in value:
        import capo_qbusiness.types.document_acl_groups

        out["groups"] = capo_qbusiness.types.document_acl_groups.serialize_json(
            value["groups"]
        )
    return out


def deserialize_json(data: dict) -> DocumentAclCondition:
    out: DocumentAclCondition = {}  # type: ignore[typeddict-item]
    if "memberRelation" in data:
        import capo_qbusiness.types.member_relation

        out["member_relation"] = capo_qbusiness.types.member_relation.deserialize_json(
            data["memberRelation"]
        )
    if "users" in data:
        import capo_qbusiness.types.document_acl_users

        out["users"] = capo_qbusiness.types.document_acl_users.deserialize_json(
            data["users"]
        )
    if "groups" in data:
        import capo_qbusiness.types.document_acl_groups

        out["groups"] = capo_qbusiness.types.document_acl_groups.deserialize_json(
            data["groups"]
        )
    return out
