"""Generated from Smithy shape ``com.amazonaws.guardduty#SecurityContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean


class SecurityContext(TypedDict, closed=True):
    privileged: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Whether the container is privileged.</p>"""
    allow_privilege_escalation: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Whether or not a container or a Kubernetes pod is allowed to gain more privileges than its parent process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityContext) -> dict:
    out: dict = {}
    if "privileged" in value:
        out["privileged"] = value["privileged"]
    if "allow_privilege_escalation" in value:
        out["allowPrivilegeEscalation"] = value["allow_privilege_escalation"]
    return out


def deserialize_json(data: dict) -> SecurityContext:
    out: SecurityContext = {}  # type: ignore[typeddict-item]
    if "privileged" in data:
        out["privileged"] = data["privileged"]
    if "allowPrivilegeEscalation" in data:
        out["allow_privilege_escalation"] = data["allowPrivilegeEscalation"]
    return out
