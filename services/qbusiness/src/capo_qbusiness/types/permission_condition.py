"""Generated from Smithy shape ``com.amazonaws.qbusiness#PermissionCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.permission_condition_key
    import capo_qbusiness.types.permission_condition_operator
    import capo_qbusiness.types.permission_condition_values


class PermissionCondition(TypedDict, closed=True):
    condition_operator: (
        "capo_qbusiness.types.permission_condition_operator.PermissionConditionOperator"
    )
    """<p>The operator to use for the condition evaluation. This determines how the condition values are compared.</p>"""
    condition_key: (
        "capo_qbusiness.types.permission_condition_key.PermissionConditionKey"
    )
    """<p>The key for the condition. This identifies the attribute that the condition applies to.</p>"""
    condition_values: (
        "capo_qbusiness.types.permission_condition_values.PermissionConditionValues"
    )
    """<p>The values to compare against using the specified condition operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionCondition) -> dict:
    out: dict = {}
    import capo_qbusiness.types.permission_condition_operator

    out["conditionOperator"] = (
        capo_qbusiness.types.permission_condition_operator.serialize_json(
            value["condition_operator"]
        )
    )
    out["conditionKey"] = value["condition_key"]
    import capo_qbusiness.types.permission_condition_values

    out["conditionValues"] = (
        capo_qbusiness.types.permission_condition_values.serialize_json(
            value["condition_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> PermissionCondition:
    out: PermissionCondition = {}  # type: ignore[typeddict-item]
    if "conditionOperator" in data:
        import capo_qbusiness.types.permission_condition_operator

        out["condition_operator"] = (
            capo_qbusiness.types.permission_condition_operator.deserialize_json(
                data["conditionOperator"]
            )
        )
    else:
        raise DeserializationError("PermissionCondition.condition_operator required")
    if "conditionKey" in data:
        out["condition_key"] = data["conditionKey"]
    else:
        raise DeserializationError("PermissionCondition.condition_key required")
    if "conditionValues" in data:
        import capo_qbusiness.types.permission_condition_values

        out["condition_values"] = (
            capo_qbusiness.types.permission_condition_values.deserialize_json(
                data["conditionValues"]
            )
        )
    else:
        raise DeserializationError("PermissionCondition.condition_values required")
    return out
