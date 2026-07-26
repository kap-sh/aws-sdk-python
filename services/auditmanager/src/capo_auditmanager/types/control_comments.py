"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlComments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control_comment

ControlComments: TypeAlias = list[
    "capo_auditmanager.types.control_comment.ControlComment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlComments) -> list:
    import capo_auditmanager.types.control_comment

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.control_comment.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlComments:
    import capo_auditmanager.types.control_comment

    out: ControlComments = []
    for item in data:
        out.append(capo_auditmanager.types.control_comment.deserialize_json(item))
    return out
