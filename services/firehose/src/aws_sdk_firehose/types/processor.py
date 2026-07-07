"""Generated from Smithy shape ``com.amazonaws.firehose#Processor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.processor_parameter_list
    import aws_sdk_firehose.types.processor_type


class Processor(TypedDict, closed=True):
    type: "aws_sdk_firehose.types.processor_type.ProcessorType"
    """<p>The type of processor.</p>"""
    parameters: NotRequired[
        "aws_sdk_firehose.types.processor_parameter_list.ProcessorParameterList"
    ]
    """<p>The processor parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Processor) -> dict:
    out: dict = {}
    import aws_sdk_firehose.types.processor_type

    out["Type"] = aws_sdk_firehose.types.processor_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "parameters" in value:
        import aws_sdk_firehose.types.processor_parameter_list

        out["Parameters"] = (
            aws_sdk_firehose.types.processor_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Processor:
    out: Processor = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_firehose.types.processor_type

        out["type"] = aws_sdk_firehose.types.processor_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("Processor.type required")
    if "Parameters" in data:
        import aws_sdk_firehose.types.processor_parameter_list

        out["parameters"] = (
            aws_sdk_firehose.types.processor_parameter_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
