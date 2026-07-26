"""Generated from Smithy shape ``com.amazonaws.auditmanager#ChangeLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.action_enum
    import capo_auditmanager.types.iam_arn
    import capo_auditmanager.types.non_empty_string
    import capo_auditmanager.types.object_type_enum
    import capo_auditmanager.types.timestamp


class ChangeLog(TypedDict, closed=True):
    object_type: NotRequired["capo_auditmanager.types.object_type_enum.ObjectTypeEnum"]
    """<p> The object that was changed, such as an assessment, control, or control set. </p>"""
    object_name: NotRequired["capo_auditmanager.types.non_empty_string.NonEmptyString"]
    """<p> The name of the object that changed. This could be the name of an assessment, control, or control set.</p>"""
    action: NotRequired["capo_auditmanager.types.action_enum.ActionEnum"]
    """<p> The action that was performed. </p>"""
    created_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the action was performed and the changelog record was created. </p>"""
    created_by: NotRequired["capo_auditmanager.types.iam_arn.IamArn"]
    """<p> The user or role that performed the action. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeLog) -> dict:
    out: dict = {}
    if "object_type" in value:
        import capo_auditmanager.types.object_type_enum

        out["objectType"] = capo_auditmanager.types.object_type_enum.serialize_json(
            value["object_type"]
        )
    if "object_name" in value:
        out["objectName"] = value["object_name"]
    if "action" in value:
        import capo_auditmanager.types.action_enum

        out["action"] = capo_auditmanager.types.action_enum.serialize_json(
            value["action"]
        )
    if "created_at" in value:
        import capo_auditmanager.types.timestamp

        out["createdAt"] = capo_auditmanager.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> ChangeLog:
    out: ChangeLog = {}  # type: ignore[typeddict-item]
    if "objectType" in data:
        import capo_auditmanager.types.object_type_enum

        out["object_type"] = capo_auditmanager.types.object_type_enum.deserialize_json(
            data["objectType"]
        )
    if "objectName" in data:
        out["object_name"] = data["objectName"]
    if "action" in data:
        import capo_auditmanager.types.action_enum

        out["action"] = capo_auditmanager.types.action_enum.deserialize_json(
            data["action"]
        )
    if "createdAt" in data:
        import capo_auditmanager.types.timestamp

        out["created_at"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    return out
