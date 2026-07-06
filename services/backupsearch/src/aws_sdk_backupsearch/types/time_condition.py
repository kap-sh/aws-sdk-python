"""Generated from Smithy shape ``com.amazonaws.backupsearch#TimeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_backupsearch.types.time_condition_operator


class TimeCondition(TypedDict, closed=True):
    value: "datetime.datetime"
    """<p>This is the timestamp value of the time condition.</p>"""
    operator: "aws_sdk_backupsearch.types.time_condition_operator.TimeConditionOperator"
    """<p>A string that defines what values will be returned.</p> <p>If this is included, avoid combinations of operators that will return all possible values. For example, including both <code>EQUALS_TO</code> and <code>NOT_EQUALS_TO</code> with a value of <code>4</code> will return all values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeCondition) -> dict:
    out: dict = {}
    import aws_sdk_backupsearch.types._prelude.timestamp

    out["Value"] = aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
        value["value"]
    )
    import aws_sdk_backupsearch.types.time_condition_operator

    out["Operator"] = aws_sdk_backupsearch.types.time_condition_operator.serialize_json(
        value.get("operator", "EQUALS_TO")
    )
    return out


def deserialize_json(data: dict) -> TimeCondition:
    out: TimeCondition = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["value"] = aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
            data["Value"]
        )
    else:
        raise DeserializationError("TimeCondition.value required")
    if "Operator" in data:
        import aws_sdk_backupsearch.types.time_condition_operator

        out["operator"] = (
            aws_sdk_backupsearch.types.time_condition_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        out["operator"] = "EQUALS_TO"
    return out
