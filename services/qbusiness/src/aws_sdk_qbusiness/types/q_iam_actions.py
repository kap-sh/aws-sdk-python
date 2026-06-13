"""Generated from Smithy shape ``com.amazonaws.qbusiness#QIamActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.q_iam_action

QIamActions: TypeAlias = list["aws_sdk_qbusiness.types.q_iam_action.QIamAction"]


# --- restJson1 ser/de ---
def serialize_json(value: QIamActions) -> list:
    return list(value)


def deserialize_json(data: list) -> QIamActions:
    return list(data)
