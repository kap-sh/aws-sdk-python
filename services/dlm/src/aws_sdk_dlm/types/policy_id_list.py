"""Generated from Smithy shape ``com.amazonaws.dlm#PolicyIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.policy_id

PolicyIdList: TypeAlias = list["aws_sdk_dlm.types.policy_id.PolicyId"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyIdList:
    return list(data)
