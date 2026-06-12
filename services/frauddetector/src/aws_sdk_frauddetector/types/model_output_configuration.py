"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.csv_index_to_variable_map
    import aws_sdk_frauddetector.types.json_key_to_variable_map
    import aws_sdk_frauddetector.types.model_output_data_format


class ModelOutputConfiguration(TypedDict):
    format: "aws_sdk_frauddetector.types.model_output_data_format.ModelOutputDataFormat"
    """<p>The format of the model output configuration.</p>"""
    json_key_to_variable_map: NotRequired[
        "aws_sdk_frauddetector.types.json_key_to_variable_map.JsonKeyToVariableMap"
    ]
    """<p>A map of JSON keys in response from SageMaker to the Amazon Fraud Detector variables. </p>"""
    csv_index_to_variable_map: NotRequired[
        "aws_sdk_frauddetector.types.csv_index_to_variable_map.CsvIndexToVariableMap"
    ]
    """<p>A map of CSV index values in the SageMaker response to the Amazon Fraud Detector variables. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelOutputConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_frauddetector.types.model_output_data_format

    out["format"] = (
        aws_sdk_frauddetector.types.model_output_data_format.serialize_aws_json_1_1(
            value["format"]
        )
    )
    if "json_key_to_variable_map" in value:
        import aws_sdk_frauddetector.types.json_key_to_variable_map

        out["jsonKeyToVariableMap"] = (
            aws_sdk_frauddetector.types.json_key_to_variable_map.serialize_aws_json_1_1(
                value["json_key_to_variable_map"]
            )
        )
    if "csv_index_to_variable_map" in value:
        import aws_sdk_frauddetector.types.csv_index_to_variable_map

        out["csvIndexToVariableMap"] = (
            aws_sdk_frauddetector.types.csv_index_to_variable_map.serialize_aws_json_1_1(
                value["csv_index_to_variable_map"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelOutputConfiguration:
    out: ModelOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "format" in data:
        import aws_sdk_frauddetector.types.model_output_data_format

        out["format"] = (
            aws_sdk_frauddetector.types.model_output_data_format.deserialize_aws_json_1_1(
                data["format"]
            )
        )
    else:
        raise DeserializationError("ModelOutputConfiguration.format required")
    if "jsonKeyToVariableMap" in data:
        import aws_sdk_frauddetector.types.json_key_to_variable_map

        out["json_key_to_variable_map"] = (
            aws_sdk_frauddetector.types.json_key_to_variable_map.deserialize_aws_json_1_1(
                data["jsonKeyToVariableMap"]
            )
        )
    if "csvIndexToVariableMap" in data:
        import aws_sdk_frauddetector.types.csv_index_to_variable_map

        out["csv_index_to_variable_map"] = (
            aws_sdk_frauddetector.types.csv_index_to_variable_map.deserialize_aws_json_1_1(
                data["csvIndexToVariableMap"]
            )
        )
    return out
