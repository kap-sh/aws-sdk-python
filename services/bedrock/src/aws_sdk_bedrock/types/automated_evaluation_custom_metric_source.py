"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedEvaluationCustomMetricSource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_metric_definition


class _AutomatedEvaluationCustomMetricSource_customMetricDefinition(TypedDict):
    customMetricDefinition: (
        "aws_sdk_bedrock.types.custom_metric_definition.CustomMetricDefinition"
    )


AutomatedEvaluationCustomMetricSource: TypeAlias = (
    _AutomatedEvaluationCustomMetricSource_customMetricDefinition
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEvaluationCustomMetricSource) -> dict:
    if "customMetricDefinition" in value:
        import aws_sdk_bedrock.types.custom_metric_definition

        return {
            "customMetricDefinition": aws_sdk_bedrock.types.custom_metric_definition.serialize_json(
                value["customMetricDefinition"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedEvaluationCustomMetricSource: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedEvaluationCustomMetricSource:
    if "customMetricDefinition" in data:
        import aws_sdk_bedrock.types.custom_metric_definition

        return {
            "customMetricDefinition": aws_sdk_bedrock.types.custom_metric_definition.deserialize_json(
                data["customMetricDefinition"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedEvaluationCustomMetricSource: no recognized variant key"
        )
