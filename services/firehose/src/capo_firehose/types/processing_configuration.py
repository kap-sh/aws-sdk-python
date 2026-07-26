"""Generated from Smithy shape ``com.amazonaws.firehose#ProcessingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.processor_list


class ProcessingConfiguration(TypedDict, closed=True):
    enabled: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>Enables or disables data processing.</p>"""
    processors: NotRequired["capo_firehose.types.processor_list.ProcessorList"]
    """<p>The data processors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "processors" in value:
        import capo_firehose.types.processor_list

        out["Processors"] = capo_firehose.types.processor_list.serialize_aws_json_1_1(
            value["processors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingConfiguration:
    out: ProcessingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Processors" in data:
        import capo_firehose.types.processor_list

        out["processors"] = capo_firehose.types.processor_list.deserialize_aws_json_1_1(
            data["Processors"]
        )
    return out
