"""Generated from Smithy shape ``com.amazonaws.backup#ConditionParameter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_backup.types.condition_key
    import aws_sdk_backup.types.condition_value

class ConditionParameter(TypedDict):
    condition_key: NotRequired["aws_sdk_backup.types.condition_key.ConditionKey"]
    """<p>The key in a key-value pair. For example, in the tag <code>Department: Accounting</code>, <code>Department</code> is the key.</p>"""
    condition_value: NotRequired["aws_sdk_backup.types.condition_value.ConditionValue"]
    """<p>The value in a key-value pair. For example, in the tag <code>Department: Accounting</code>, <code>Accounting</code> is the value.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConditionParameter) -> dict:
    out: dict = {}
    if "condition_key" in value:
        out["ConditionKey"] = value["condition_key"]
    if "condition_value" in value:
        out["ConditionValue"] = value["condition_value"]
    return out


def deserialize_json(data: dict) -> ConditionParameter:
    out: ConditionParameter = {}  # type: ignore[typeddict-item]
    if "ConditionKey" in data:
        out["condition_key"] = data["ConditionKey"]
    if "ConditionValue" in data:
        out["condition_value"] = data["ConditionValue"]
    return out