"""Generated from Smithy shape ``com.amazonaws.glue#EvaluateDataQualityMultiFrame``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.dq_additional_options
    import aws_sdk_glue.types.dq_results_publishing_options
    import aws_sdk_glue.types.dq_stop_job_on_failure_options
    import aws_sdk_glue.types.dqdl_aliases
    import aws_sdk_glue.types.dqdl_string
    import aws_sdk_glue.types.many_inputs
    import aws_sdk_glue.types.node_name


class EvaluateDataQualityMultiFrame(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data quality evaluation.</p>"""
    inputs: "aws_sdk_glue.types.many_inputs.ManyInputs"
    """<p>The inputs of your data quality evaluation. The first input in this list is the primary data source.</p>"""
    additional_data_sources: NotRequired["aws_sdk_glue.types.dqdl_aliases.DQDLAliases"]
    """<p>The aliases of all data sources except primary.</p>"""
    ruleset: "aws_sdk_glue.types.dqdl_string.DQDLString"
    """<p>The ruleset for your data quality evaluation.</p>"""
    publishing_options: NotRequired[
        "aws_sdk_glue.types.dq_results_publishing_options.DQResultsPublishingOptions"
    ]
    """<p>Options to configure how your results are published.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.dq_additional_options.DQAdditionalOptions"
    ]
    """<p>Options to configure runtime behavior of the transform.</p>"""
    stop_job_on_failure_options: NotRequired[
        "aws_sdk_glue.types.dq_stop_job_on_failure_options.DQStopJobOnFailureOptions"
    ]
    """<p>Options to configure how your job will stop if your data quality evaluation fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluateDataQualityMultiFrame) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.many_inputs

    out["Inputs"] = aws_sdk_glue.types.many_inputs.serialize_aws_json_1_1(
        value["inputs"]
    )
    if "additional_data_sources" in value:
        import aws_sdk_glue.types.dqdl_aliases

        out["AdditionalDataSources"] = (
            aws_sdk_glue.types.dqdl_aliases.serialize_aws_json_1_1(
                value["additional_data_sources"]
            )
        )
    out["Ruleset"] = value["ruleset"]
    if "publishing_options" in value:
        import aws_sdk_glue.types.dq_results_publishing_options

        out["PublishingOptions"] = (
            aws_sdk_glue.types.dq_results_publishing_options.serialize_aws_json_1_1(
                value["publishing_options"]
            )
        )
    if "additional_options" in value:
        import aws_sdk_glue.types.dq_additional_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.dq_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "stop_job_on_failure_options" in value:
        import aws_sdk_glue.types.dq_stop_job_on_failure_options

        out["StopJobOnFailureOptions"] = (
            aws_sdk_glue.types.dq_stop_job_on_failure_options.serialize_aws_json_1_1(
                value["stop_job_on_failure_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluateDataQualityMultiFrame:
    out: EvaluateDataQualityMultiFrame = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("EvaluateDataQualityMultiFrame.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.many_inputs

        out["inputs"] = aws_sdk_glue.types.many_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("EvaluateDataQualityMultiFrame.inputs required")
    if "AdditionalDataSources" in data:
        import aws_sdk_glue.types.dqdl_aliases

        out["additional_data_sources"] = (
            aws_sdk_glue.types.dqdl_aliases.deserialize_aws_json_1_1(
                data["AdditionalDataSources"]
            )
        )
    if "Ruleset" in data:
        out["ruleset"] = data["Ruleset"]
    else:
        raise DeserializationError("EvaluateDataQualityMultiFrame.ruleset required")
    if "PublishingOptions" in data:
        import aws_sdk_glue.types.dq_results_publishing_options

        out["publishing_options"] = (
            aws_sdk_glue.types.dq_results_publishing_options.deserialize_aws_json_1_1(
                data["PublishingOptions"]
            )
        )
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.dq_additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.dq_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "StopJobOnFailureOptions" in data:
        import aws_sdk_glue.types.dq_stop_job_on_failure_options

        out["stop_job_on_failure_options"] = (
            aws_sdk_glue.types.dq_stop_job_on_failure_options.deserialize_aws_json_1_1(
                data["StopJobOnFailureOptions"]
            )
        )
    return out
