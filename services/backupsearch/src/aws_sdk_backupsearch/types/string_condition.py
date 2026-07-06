"""Generated from Smithy shape ``com.amazonaws.backupsearch#StringCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.string_condition_operator


class StringCondition(TypedDict, closed=True):
    value: "str"
    """<p>The value of the string.</p>"""
    operator: (
        "aws_sdk_backupsearch.types.string_condition_operator.StringConditionOperator"
    )
    """<p>A string that defines what values will be returned.</p> <p>If this is included, avoid combinations of operators that will return all possible values. For example, including both <code>EQUALS_TO</code> and <code>NOT_EQUALS_TO</code> with a value of <code>4</code> will return all values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringCondition) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import aws_sdk_backupsearch.types.string_condition_operator

    out["Operator"] = (
        aws_sdk_backupsearch.types.string_condition_operator.serialize_json(
            value.get("operator", "EQUALS_TO")
        )
    )
    return out


def deserialize_json(data: dict) -> StringCondition:
    out: StringCondition = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("StringCondition.value required")
    if "Operator" in data:
        import aws_sdk_backupsearch.types.string_condition_operator

        out["operator"] = (
            aws_sdk_backupsearch.types.string_condition_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        out["operator"] = "EQUALS_TO"
    return out
