"""Generated from Smithy shape ``com.amazonaws.deadline#DependencyCounts``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.integer


class DependencyCounts(TypedDict):
    dependencies_resolved: "aws_sdk_deadline.types.integer.Integer"
    """<p>The number of resolved dependencies.</p>"""
    dependencies_unresolved: "aws_sdk_deadline.types.integer.Integer"
    """<p>The number of unresolved dependencies.</p>"""
    consumers_resolved: "aws_sdk_deadline.types.integer.Integer"
    """<p>The number of consumers resolved.</p>"""
    consumers_unresolved: "aws_sdk_deadline.types.integer.Integer"
    """<p>The number of unresolved consumers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyCounts) -> dict:
    out: dict = {}
    out["dependenciesResolved"] = value["dependencies_resolved"]
    out["dependenciesUnresolved"] = value["dependencies_unresolved"]
    out["consumersResolved"] = value["consumers_resolved"]
    out["consumersUnresolved"] = value["consumers_unresolved"]
    return out


def deserialize_json(data: dict) -> DependencyCounts:
    out: DependencyCounts = {}  # type: ignore[typeddict-item]
    if "dependenciesResolved" in data:
        out["dependencies_resolved"] = data["dependenciesResolved"]
    else:
        raise DeserializationError("DependencyCounts.dependencies_resolved required")
    if "dependenciesUnresolved" in data:
        out["dependencies_unresolved"] = data["dependenciesUnresolved"]
    else:
        raise DeserializationError("DependencyCounts.dependencies_unresolved required")
    if "consumersResolved" in data:
        out["consumers_resolved"] = data["consumersResolved"]
    else:
        raise DeserializationError("DependencyCounts.consumers_resolved required")
    if "consumersUnresolved" in data:
        out["consumers_unresolved"] = data["consumersUnresolved"]
    else:
        raise DeserializationError("DependencyCounts.consumers_unresolved required")
    return out
