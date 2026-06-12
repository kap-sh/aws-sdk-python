"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.processor_list


class ProcessingConfiguration(TypedDict):
    enabled: NotRequired["aws_sdk_firehose.types.boolean_object.BooleanObject"]
    """<p>Enables or disables data processing.</p>"""
    processors: NotRequired["aws_sdk_firehose.types.processor_list.ProcessorList"]
    """<p>The data processors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "processors" in value:
        import aws_sdk_firehose.types.processor_list

        out["Processors"] = (
            aws_sdk_firehose.types.processor_list.serialize_aws_json_1_1(
                value["processors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingConfiguration:
    out: ProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Processors" in data:
        import aws_sdk_firehose.types.processor_list

        out["processors"] = (
            aws_sdk_firehose.types.processor_list.deserialize_aws_json_1_1(
                data["Processors"]
            )
        )
    return out
