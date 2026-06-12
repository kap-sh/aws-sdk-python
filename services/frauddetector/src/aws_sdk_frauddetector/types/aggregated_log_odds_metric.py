"""Generated from Smithy shape ``com.amazonaws.frauddetector#AggregatedLogOddsMetric``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float
    import aws_sdk_frauddetector.types.list_of_strings


class AggregatedLogOddsMetric(TypedDict):
    variable_names: "aws_sdk_frauddetector.types.list_of_strings.ListOfStrings"
    """<p> The names of all the variables. </p>"""
    aggregated_variables_importance: "aws_sdk_frauddetector.types.float.float"
    """<p> The relative importance of the variables in the list to the other event variable. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedLogOddsMetric) -> dict:
    out: dict = {}
    import aws_sdk_frauddetector.types.list_of_strings

    out["variableNames"] = (
        aws_sdk_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value["variable_names"]
        )
    )
    out["aggregatedVariablesImportance"] = value["aggregated_variables_importance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatedLogOddsMetric:
    out: AggregatedLogOddsMetric = {}  # type: ignore[typeddict-item]
    if "variableNames" in data:
        import aws_sdk_frauddetector.types.list_of_strings

        out["variable_names"] = (
            aws_sdk_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["variableNames"]
            )
        )
    else:
        raise DeserializationError("AggregatedLogOddsMetric.variable_names required")
    if "aggregatedVariablesImportance" in data:
        out["aggregated_variables_importance"] = data["aggregatedVariablesImportance"]
    else:
        raise DeserializationError(
            "AggregatedLogOddsMetric.aggregated_variables_importance required"
        )
    return out
