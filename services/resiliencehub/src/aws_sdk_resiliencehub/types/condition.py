"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.condition_operator_type
    import aws_sdk_resiliencehub.types.string255


class Condition(TypedDict, closed=True):
    field: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Indicates the field in the metric.</p>"""
    operator: (
        "aws_sdk_resiliencehub.types.condition_operator_type.ConditionOperatorType"
    )
    """<p>Indicates the type of operator or comparison to be used when evaluating a condition against the specified field. </p>"""
    value: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Indicates the value or data against which a condition is evaluated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    import aws_sdk_resiliencehub.types.condition_operator_type

    out["operator"] = (
        aws_sdk_resiliencehub.types.condition_operator_type.serialize_json(
            value["operator"]
        )
    )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    else:
        raise DeserializationError("Condition.field required")
    if "operator" in data:
        import aws_sdk_resiliencehub.types.condition_operator_type

        out["operator"] = (
            aws_sdk_resiliencehub.types.condition_operator_type.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("Condition.operator required")
    if "value" in data:
        out["value"] = data["value"]
    return out
