"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AutomatedAbrRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_allowed_rendition_size
    import aws_sdk_mediaconvert.types.__list_of_force_include_rendition_size
    import aws_sdk_mediaconvert.types.min_bottom_rendition_size
    import aws_sdk_mediaconvert.types.min_top_rendition_size
    import aws_sdk_mediaconvert.types.rule_type


class AutomatedAbrRule(TypedDict, closed=True):
    allowed_renditions: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_allowed_rendition_size.__listOfAllowedRenditionSize"
    ]
    """When customer adds the allowed renditions rule for auto ABR ladder, they are required to add at leat one rendition to allowedRenditions list"""
    force_include_renditions: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_force_include_rendition_size.__listOfForceIncludeRenditionSize"
    ]
    """When customer adds the force include renditions rule for auto ABR ladder, they are required to add at leat one rendition to forceIncludeRenditions list"""
    min_bottom_rendition_size: NotRequired[
        "aws_sdk_mediaconvert.types.min_bottom_rendition_size.MinBottomRenditionSize"
    ]
    """Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. * The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. * If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size."""
    min_top_rendition_size: NotRequired[
        "aws_sdk_mediaconvert.types.min_top_rendition_size.MinTopRenditionSize"
    ]
    """Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. * The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. * If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution."""
    type: NotRequired["aws_sdk_mediaconvert.types.rule_type.RuleType"]
    """Use Min top rendition size to specify a minimum size for the highest resolution in your ABR stack. * The highest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 1280x720 the highest resolution in your ABR stack will be equal to or greater than 1280x720. * If you specify a value for Max resolution, the value that you specify for Min top rendition size must be less than, or equal to, Max resolution. Use Min bottom rendition size to specify a minimum size for the lowest resolution in your ABR stack. * The lowest resolution in your ABR stack will be equal to or greater than the value that you enter. For example: If you specify 640x360 the lowest resolution in your ABR stack will be equal to or greater than to 640x360. * If you specify a Min top rendition size rule, the value that you specify for Min bottom rendition size must be less than, or equal to, Min top rendition size. Use Force include renditions to specify one or more resolutions to include your ABR stack. * (Recommended) To optimize automated ABR, specify as few resolutions as possible. * (Required) The number of resolutions that you specify must be equal to, or less than, the Max renditions setting. * If you specify a Min top rendition size rule, specify at least one resolution that is equal to, or greater than, Min top rendition size. * If you specify a Min bottom rendition size rule, only specify resolutions that are equal to, or greater than, Min bottom rendition size. * If you specify a Force include renditions rule, do not specify a separate rule for Allowed renditions. * Note: The ABR stack may include other resolutions that you do not specify here, depending on the Max renditions setting. Use Allowed renditions to specify a list of possible resolutions in your ABR stack. * (Required) The number of resolutions that you specify must be equal to, or greater than, the Max renditions setting. * MediaConvert will create an ABR stack exclusively from the list of resolutions that you specify. * Some resolutions in the Allowed renditions list may not be included, however you can force a resolution to be included by setting Required to ENABLED. * You must specify at least one resolution that is greater than or equal to any resolutions that you specify in Min top rendition size or Min bottom rendition size. * If you specify Allowed renditions, you must not specify a separate rule for Force include renditions."""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedAbrRule) -> dict:
    out: dict = {}
    if "allowed_renditions" in value:
        import aws_sdk_mediaconvert.types.__list_of_allowed_rendition_size

        out["allowedRenditions"] = (
            aws_sdk_mediaconvert.types.__list_of_allowed_rendition_size.serialize_json(
                value["allowed_renditions"]
            )
        )
    if "force_include_renditions" in value:
        import aws_sdk_mediaconvert.types.__list_of_force_include_rendition_size

        out["forceIncludeRenditions"] = (
            aws_sdk_mediaconvert.types.__list_of_force_include_rendition_size.serialize_json(
                value["force_include_renditions"]
            )
        )
    if "min_bottom_rendition_size" in value:
        import aws_sdk_mediaconvert.types.min_bottom_rendition_size

        out["minBottomRenditionSize"] = (
            aws_sdk_mediaconvert.types.min_bottom_rendition_size.serialize_json(
                value["min_bottom_rendition_size"]
            )
        )
    if "min_top_rendition_size" in value:
        import aws_sdk_mediaconvert.types.min_top_rendition_size

        out["minTopRenditionSize"] = (
            aws_sdk_mediaconvert.types.min_top_rendition_size.serialize_json(
                value["min_top_rendition_size"]
            )
        )
    if "type" in value:
        import aws_sdk_mediaconvert.types.rule_type

        out["type"] = aws_sdk_mediaconvert.types.rule_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> AutomatedAbrRule:
    out: AutomatedAbrRule = {}  # type: ignore[typeddict-item]
    if "allowedRenditions" in data:
        import aws_sdk_mediaconvert.types.__list_of_allowed_rendition_size

        out["allowed_renditions"] = (
            aws_sdk_mediaconvert.types.__list_of_allowed_rendition_size.deserialize_json(
                data["allowedRenditions"]
            )
        )
    if "forceIncludeRenditions" in data:
        import aws_sdk_mediaconvert.types.__list_of_force_include_rendition_size

        out["force_include_renditions"] = (
            aws_sdk_mediaconvert.types.__list_of_force_include_rendition_size.deserialize_json(
                data["forceIncludeRenditions"]
            )
        )
    if "minBottomRenditionSize" in data:
        import aws_sdk_mediaconvert.types.min_bottom_rendition_size

        out["min_bottom_rendition_size"] = (
            aws_sdk_mediaconvert.types.min_bottom_rendition_size.deserialize_json(
                data["minBottomRenditionSize"]
            )
        )
    if "minTopRenditionSize" in data:
        import aws_sdk_mediaconvert.types.min_top_rendition_size

        out["min_top_rendition_size"] = (
            aws_sdk_mediaconvert.types.min_top_rendition_size.deserialize_json(
                data["minTopRenditionSize"]
            )
        )
    if "type" in data:
        import aws_sdk_mediaconvert.types.rule_type

        out["type"] = aws_sdk_mediaconvert.types.rule_type.deserialize_json(
            data["type"]
        )
    return out
