"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SqlApplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.inputs
    import capo_kinesis_analytics_v2.types.outputs
    import capo_kinesis_analytics_v2.types.reference_data_sources


class SqlApplicationConfiguration(TypedDict, closed=True):
    inputs: NotRequired["capo_kinesis_analytics_v2.types.inputs.Inputs"]
    """<p>The array of <a>Input</a> objects describing the input streams used by the application.</p>"""
    outputs: NotRequired["capo_kinesis_analytics_v2.types.outputs.Outputs"]
    """<p>The array of <a>Output</a> objects describing the destination streams used by the application.</p>"""
    reference_data_sources: NotRequired[
        "capo_kinesis_analytics_v2.types.reference_data_sources.ReferenceDataSources"
    ]
    """<p>The array of <a>ReferenceDataSource</a> objects describing the reference data sources used by the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlApplicationConfiguration) -> dict:
    out: dict = {}
    if "inputs" in value:
        import capo_kinesis_analytics_v2.types.inputs

        out["Inputs"] = capo_kinesis_analytics_v2.types.inputs.serialize_aws_json_1_1(
            value["inputs"]
        )
    if "outputs" in value:
        import capo_kinesis_analytics_v2.types.outputs

        out["Outputs"] = capo_kinesis_analytics_v2.types.outputs.serialize_aws_json_1_1(
            value["outputs"]
        )
    if "reference_data_sources" in value:
        import capo_kinesis_analytics_v2.types.reference_data_sources

        out["ReferenceDataSources"] = (
            capo_kinesis_analytics_v2.types.reference_data_sources.serialize_aws_json_1_1(
                value["reference_data_sources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlApplicationConfiguration:
    out: SqlApplicationConfiguration = {}  # type: ignore[typeddict-item]
    if "Inputs" in data:
        import capo_kinesis_analytics_v2.types.inputs

        out["inputs"] = capo_kinesis_analytics_v2.types.inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    if "Outputs" in data:
        import capo_kinesis_analytics_v2.types.outputs

        out["outputs"] = (
            capo_kinesis_analytics_v2.types.outputs.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if "ReferenceDataSources" in data:
        import capo_kinesis_analytics_v2.types.reference_data_sources

        out["reference_data_sources"] = (
            capo_kinesis_analytics_v2.types.reference_data_sources.deserialize_aws_json_1_1(
                data["ReferenceDataSources"]
            )
        )
    return out
