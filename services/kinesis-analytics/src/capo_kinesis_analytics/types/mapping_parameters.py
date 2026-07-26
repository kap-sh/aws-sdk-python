"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#MappingParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.csv_mapping_parameters
    import capo_kinesis_analytics.types.json_mapping_parameters


class MappingParameters(TypedDict, closed=True):
    json_mapping_parameters: NotRequired[
        "capo_kinesis_analytics.types.json_mapping_parameters.JSONMappingParameters"
    ]
    """<p>Provides additional mapping information when JSON is the record format on the streaming source.</p>"""
    csv_mapping_parameters: NotRequired[
        "capo_kinesis_analytics.types.csv_mapping_parameters.CSVMappingParameters"
    ]
    """<p>Provides additional mapping information when the record format uses delimiters (for example, CSV).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MappingParameters) -> dict:
    out: dict = {}
    if "json_mapping_parameters" in value:
        import capo_kinesis_analytics.types.json_mapping_parameters

        out["JSONMappingParameters"] = (
            capo_kinesis_analytics.types.json_mapping_parameters.serialize_aws_json_1_1(
                value["json_mapping_parameters"]
            )
        )
    if "csv_mapping_parameters" in value:
        import capo_kinesis_analytics.types.csv_mapping_parameters

        out["CSVMappingParameters"] = (
            capo_kinesis_analytics.types.csv_mapping_parameters.serialize_aws_json_1_1(
                value["csv_mapping_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MappingParameters:
    out: MappingParameters = {}  # type: ignore[typeddict-item]
    if "JSONMappingParameters" in data:
        import capo_kinesis_analytics.types.json_mapping_parameters

        out["json_mapping_parameters"] = (
            capo_kinesis_analytics.types.json_mapping_parameters.deserialize_aws_json_1_1(
                data["JSONMappingParameters"]
            )
        )
    if "CSVMappingParameters" in data:
        import capo_kinesis_analytics.types.csv_mapping_parameters

        out["csv_mapping_parameters"] = (
            capo_kinesis_analytics.types.csv_mapping_parameters.deserialize_aws_json_1_1(
                data["CSVMappingParameters"]
            )
        )
    return out
