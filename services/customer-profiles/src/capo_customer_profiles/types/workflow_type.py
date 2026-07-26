"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowType``."""

from typing import Literal, TypeAlias, cast

WorkflowType: TypeAlias = Literal["APPFLOW_INTEGRATION",]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowType) -> str:
    return value


def deserialize_json(data: str) -> WorkflowType:
    return cast(WorkflowType, data)
