"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlComments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_comment

ControlComments: TypeAlias = list[
    "aws_sdk_auditmanager.types.control_comment.ControlComment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlComments) -> list:
    import aws_sdk_auditmanager.types.control_comment

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.control_comment.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlComments:
    import aws_sdk_auditmanager.types.control_comment

    out: ControlComments = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.control_comment.deserialize_json(item))
    return out
