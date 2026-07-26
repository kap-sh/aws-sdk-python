"""Generated from Smithy shape ``com.amazonaws.firehose#Processor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.processor_parameter_list
    import capo_firehose.types.processor_type


class Processor(TypedDict, closed=True):
    type: "capo_firehose.types.processor_type.ProcessorType"
    """<p>The type of processor.</p>"""
    parameters: NotRequired[
        "capo_firehose.types.processor_parameter_list.ProcessorParameterList"
    ]
    """<p>The processor parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Processor) -> dict:
    out: dict = {}
    import capo_firehose.types.processor_type

    out["Type"] = capo_firehose.types.processor_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "parameters" in value:
        import capo_firehose.types.processor_parameter_list

        out["Parameters"] = (
            capo_firehose.types.processor_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Processor:
    out: Processor = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_firehose.types.processor_type

        out["type"] = capo_firehose.types.processor_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("Processor.type required")
    if "Parameters" in data:
        import capo_firehose.types.processor_parameter_list

        out["parameters"] = (
            capo_firehose.types.processor_parameter_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
