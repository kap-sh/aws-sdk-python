"""Generated from Smithy shape ``com.amazonaws.sagemaker#ChannelSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.channel_name
    import aws_sdk_sagemaker.types.compression_types
    import aws_sdk_sagemaker.types.content_types
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.input_modes


class ChannelSpecification(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.channel_name.ChannelName"]
    """<p>The name of the channel.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A brief description of the channel.</p>"""
    is_required: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Indicates whether the channel is required by the algorithm.</p>"""
    supported_content_types: NotRequired[
        "aws_sdk_sagemaker.types.content_types.ContentTypes"
    ]
    """<p>The supported MIME types for the data.</p>"""
    supported_compression_types: NotRequired[
        "aws_sdk_sagemaker.types.compression_types.CompressionTypes"
    ]
    """<p>The allowed compression types, if data compression is used.</p>"""
    supported_input_modes: NotRequired["aws_sdk_sagemaker.types.input_modes.InputModes"]
    """<p>The allowed input mode, either FILE or PIPE.</p> <p>In FILE mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode.</p> <p>In PIPE mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelSpecification) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "is_required" in value:
        out["IsRequired"] = value["is_required"]
    if "supported_content_types" in value:
        import aws_sdk_sagemaker.types.content_types

        out["SupportedContentTypes"] = (
            aws_sdk_sagemaker.types.content_types.serialize_aws_json_1_1(
                value["supported_content_types"]
            )
        )
    if "supported_compression_types" in value:
        import aws_sdk_sagemaker.types.compression_types

        out["SupportedCompressionTypes"] = (
            aws_sdk_sagemaker.types.compression_types.serialize_aws_json_1_1(
                value["supported_compression_types"]
            )
        )
    if "supported_input_modes" in value:
        import aws_sdk_sagemaker.types.input_modes

        out["SupportedInputModes"] = (
            aws_sdk_sagemaker.types.input_modes.serialize_aws_json_1_1(
                value["supported_input_modes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelSpecification:
    out: ChannelSpecification = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "IsRequired" in data:
        out["is_required"] = data["IsRequired"]
    if "SupportedContentTypes" in data:
        import aws_sdk_sagemaker.types.content_types

        out["supported_content_types"] = (
            aws_sdk_sagemaker.types.content_types.deserialize_aws_json_1_1(
                data["SupportedContentTypes"]
            )
        )
    if "SupportedCompressionTypes" in data:
        import aws_sdk_sagemaker.types.compression_types

        out["supported_compression_types"] = (
            aws_sdk_sagemaker.types.compression_types.deserialize_aws_json_1_1(
                data["SupportedCompressionTypes"]
            )
        )
    if "SupportedInputModes" in data:
        import aws_sdk_sagemaker.types.input_modes

        out["supported_input_modes"] = (
            aws_sdk_sagemaker.types.input_modes.deserialize_aws_json_1_1(
                data["SupportedInputModes"]
            )
        )
    return out
