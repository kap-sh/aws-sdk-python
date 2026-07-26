"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.audit_target_entity


class AuditTarget(TypedDict, closed=True):
    type: "str"
    """<p>The type of entity being audited, such as <code>service</code>, <code>SLO</code>, <code>service_operation</code>, or <code>canary</code>. </p>"""
    data: "capo_application_signals.types.audit_target_entity.AuditTargetEntity"
    """<p>The specific data identifying the audit target entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditTarget) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    import capo_application_signals.types.audit_target_entity

    out["Data"] = capo_application_signals.types.audit_target_entity.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> AuditTarget:
    out: AuditTarget = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("AuditTarget.type required")
    if "Data" in data:
        import capo_application_signals.types.audit_target_entity

        out["data"] = (
            capo_application_signals.types.audit_target_entity.deserialize_json(
                data["Data"]
            )
        )
    else:
        raise DeserializationError("AuditTarget.data required")
    return out
