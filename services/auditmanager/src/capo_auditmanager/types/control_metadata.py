"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.control_name
    import capo_auditmanager.types.control_sources
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class ControlMetadata(TypedDict, closed=True):
    arn: NotRequired["capo_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the control. </p>"""
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the control. </p>"""
    name: NotRequired["capo_auditmanager.types.control_name.ControlName"]
    """<p> The name of the control. </p>"""
    control_sources: NotRequired[
        "capo_auditmanager.types.control_sources.ControlSources"
    ]
    """<p> The data source that determines where Audit Manager collects evidence from for the control. </p>"""
    created_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the control was created. </p>"""
    last_updated_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the control was most recently updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "control_sources" in value:
        out["controlSources"] = value["control_sources"]
    if "created_at" in value:
        import capo_auditmanager.types.timestamp

        out["createdAt"] = capo_auditmanager.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdatedAt"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ControlMetadata:
    out: ControlMetadata = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "controlSources" in data:
        out["control_sources"] = data["controlSources"]
    if "createdAt" in data:
        import capo_auditmanager.types.timestamp

        out["created_at"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_auditmanager.types.timestamp

        out["last_updated_at"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
