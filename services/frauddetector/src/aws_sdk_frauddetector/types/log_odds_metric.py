"""Generated from Smithy shape ``com.amazonaws.frauddetector#LogOddsMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float
    import aws_sdk_frauddetector.types.string


class LogOddsMetric(TypedDict, closed=True):
    variable_name: "aws_sdk_frauddetector.types.string.string"
    """<p>The name of the variable.</p>"""
    variable_type: "aws_sdk_frauddetector.types.string.string"
    """<p>The type of variable.</p>"""
    variable_importance: "aws_sdk_frauddetector.types.float.float"
    r"""<p>The relative importance of the variable. For more information, see <a href=\"https://docs.aws.amazon.com/frauddetector/latest/ug/model-variable-importance.html\">Model variable importance</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogOddsMetric) -> dict:
    out: dict = {}
    out["variableName"] = value["variable_name"]
    out["variableType"] = value["variable_type"]
    out["variableImportance"] = value["variable_importance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LogOddsMetric:
    out: LogOddsMetric = {}  # type: ignore[typeddict-item]
    if "variableName" in data:
        out["variable_name"] = data["variableName"]
    else:
        raise DeserializationError("LogOddsMetric.variable_name required")
    if "variableType" in data:
        out["variable_type"] = data["variableType"]
    else:
        raise DeserializationError("LogOddsMetric.variable_type required")
    if "variableImportance" in data:
        out["variable_importance"] = data["variableImportance"]
    else:
        raise DeserializationError("LogOddsMetric.variable_importance required")
    return out
