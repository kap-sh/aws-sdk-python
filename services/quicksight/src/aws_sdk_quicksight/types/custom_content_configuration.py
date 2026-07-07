"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomContentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_content_image_scaling_configuration
    import aws_sdk_quicksight.types.custom_content_type
    import aws_sdk_quicksight.types.url_operation_template
    import aws_sdk_quicksight.types.visual_interaction_options


class CustomContentConfiguration(TypedDict, closed=True):
    content_url: NotRequired[
        "aws_sdk_quicksight.types.url_operation_template.URLOperationTemplate"
    ]
    """<p>The input URL that links to the custom content that you want in the custom visual.</p>"""
    content_type: NotRequired[
        "aws_sdk_quicksight.types.custom_content_type.CustomContentType"
    ]
    """<p>The content type of the custom content visual. You can use this to have the visual render as an image.</p>"""
    image_scaling: NotRequired[
        "aws_sdk_quicksight.types.custom_content_image_scaling_configuration.CustomContentImageScalingConfiguration"
    ]
    """<p>The sizing options for the size of the custom content visual. This structure is required when the <code>ContentType</code> of the visual is <code>'IMAGE'</code>.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomContentConfiguration) -> dict:
    out: dict = {}
    if "content_url" in value:
        out["ContentUrl"] = value["content_url"]
    if "content_type" in value:
        import aws_sdk_quicksight.types.custom_content_type

        out["ContentType"] = (
            aws_sdk_quicksight.types.custom_content_type.serialize_json(
                value["content_type"]
            )
        )
    if "image_scaling" in value:
        import aws_sdk_quicksight.types.custom_content_image_scaling_configuration

        out["ImageScaling"] = (
            aws_sdk_quicksight.types.custom_content_image_scaling_configuration.serialize_json(
                value["image_scaling"]
            )
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomContentConfiguration:
    out: CustomContentConfiguration = {}  # type: ignore[typeddict-item]
    if "ContentUrl" in data:
        out["content_url"] = data["ContentUrl"]
    if "ContentType" in data:
        import aws_sdk_quicksight.types.custom_content_type

        out["content_type"] = (
            aws_sdk_quicksight.types.custom_content_type.deserialize_json(
                data["ContentType"]
            )
        )
    if "ImageScaling" in data:
        import aws_sdk_quicksight.types.custom_content_image_scaling_configuration

        out["image_scaling"] = (
            aws_sdk_quicksight.types.custom_content_image_scaling_configuration.deserialize_json(
                data["ImageScaling"]
            )
        )
    if "Interactions" in data:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
