"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SourceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.advanced_event_selectors
    import aws_sdk_cloudtrail.types.boolean


class SourceConfig(TypedDict):
    apply_to_all_regions: NotRequired["aws_sdk_cloudtrail.types.boolean.Boolean"]
    """<p> Specifies whether the channel applies to a single Region or to all Regions.</p>"""
    advanced_event_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p> The advanced event selectors that are configured for the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceConfig) -> dict:
    out: dict = {}
    if "apply_to_all_regions" in value:
        out["ApplyToAllRegions"] = value["apply_to_all_regions"]
    if "advanced_event_selectors" in value:
        import aws_sdk_cloudtrail.types.advanced_event_selectors

        out["AdvancedEventSelectors"] = (
            aws_sdk_cloudtrail.types.advanced_event_selectors.serialize_aws_json_1_1(
                value["advanced_event_selectors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceConfig:
    out: SourceConfig = {}  # type: ignore[typeddict-item]
    if "ApplyToAllRegions" in data:
        out["apply_to_all_regions"] = data["ApplyToAllRegions"]
    if "AdvancedEventSelectors" in data:
        import aws_sdk_cloudtrail.types.advanced_event_selectors

        out["advanced_event_selectors"] = (
            aws_sdk_cloudtrail.types.advanced_event_selectors.deserialize_aws_json_1_1(
                data["AdvancedEventSelectors"]
            )
        )
    return out
