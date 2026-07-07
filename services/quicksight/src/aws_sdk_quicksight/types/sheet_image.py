"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.image_custom_action_list
    import aws_sdk_quicksight.types.image_interaction_options
    import aws_sdk_quicksight.types.long_plain_text
    import aws_sdk_quicksight.types.sheet_image_scaling_configuration
    import aws_sdk_quicksight.types.sheet_image_source
    import aws_sdk_quicksight.types.sheet_image_tooltip_configuration
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class SheetImage(TypedDict, closed=True):
    sheet_image_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the sheet image.</p>"""
    source: "aws_sdk_quicksight.types.sheet_image_source.SheetImageSource"
    """<p>The source of the image.</p>"""
    scaling: NotRequired[
        "aws_sdk_quicksight.types.sheet_image_scaling_configuration.SheetImageScalingConfiguration"
    ]
    """<p>Determines how the image is scaled.</p>"""
    tooltip: NotRequired[
        "aws_sdk_quicksight.types.sheet_image_tooltip_configuration.SheetImageTooltipConfiguration"
    ]
    """<p>The tooltip to be shown when hovering over the image.</p>"""
    image_content_alt_text: NotRequired[
        "aws_sdk_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the image.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.image_interaction_options.ImageInteractionOptions"
    ]
    """<p>The general image interactions setup for an image.</p>"""
    actions: NotRequired[
        "aws_sdk_quicksight.types.image_custom_action_list.ImageCustomActionList"
    ]
    """<p>A list of custom actions that are configured for an image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImage) -> dict:
    out: dict = {}
    out["SheetImageId"] = value["sheet_image_id"]
    import aws_sdk_quicksight.types.sheet_image_source

    out["Source"] = aws_sdk_quicksight.types.sheet_image_source.serialize_json(
        value["source"]
    )
    if "scaling" in value:
        import aws_sdk_quicksight.types.sheet_image_scaling_configuration

        out["Scaling"] = (
            aws_sdk_quicksight.types.sheet_image_scaling_configuration.serialize_json(
                value["scaling"]
            )
        )
    if "tooltip" in value:
        import aws_sdk_quicksight.types.sheet_image_tooltip_configuration

        out["Tooltip"] = (
            aws_sdk_quicksight.types.sheet_image_tooltip_configuration.serialize_json(
                value["tooltip"]
            )
        )
    if "image_content_alt_text" in value:
        out["ImageContentAltText"] = value["image_content_alt_text"]
    if "interactions" in value:
        import aws_sdk_quicksight.types.image_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.image_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    if "actions" in value:
        import aws_sdk_quicksight.types.image_custom_action_list

        out["Actions"] = (
            aws_sdk_quicksight.types.image_custom_action_list.serialize_json(
                value["actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetImage:
    out: SheetImage = {}  # type: ignore[typeddict-item]
    if "SheetImageId" in data:
        out["sheet_image_id"] = data["SheetImageId"]
    else:
        raise DeserializationError("SheetImage.sheet_image_id required")
    if "Source" in data:
        import aws_sdk_quicksight.types.sheet_image_source

        out["source"] = aws_sdk_quicksight.types.sheet_image_source.deserialize_json(
            data["Source"]
        )
    else:
        raise DeserializationError("SheetImage.source required")
    if "Scaling" in data:
        import aws_sdk_quicksight.types.sheet_image_scaling_configuration

        out["scaling"] = (
            aws_sdk_quicksight.types.sheet_image_scaling_configuration.deserialize_json(
                data["Scaling"]
            )
        )
    if "Tooltip" in data:
        import aws_sdk_quicksight.types.sheet_image_tooltip_configuration

        out["tooltip"] = (
            aws_sdk_quicksight.types.sheet_image_tooltip_configuration.deserialize_json(
                data["Tooltip"]
            )
        )
    if "ImageContentAltText" in data:
        out["image_content_alt_text"] = data["ImageContentAltText"]
    if "Interactions" in data:
        import aws_sdk_quicksight.types.image_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.image_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    if "Actions" in data:
        import aws_sdk_quicksight.types.image_custom_action_list

        out["actions"] = (
            aws_sdk_quicksight.types.image_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    return out
