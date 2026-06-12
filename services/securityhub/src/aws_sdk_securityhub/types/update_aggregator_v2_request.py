"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateAggregatorV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class UpdateAggregatorV2Request(TypedDict):
    aggregator_v2_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the Aggregator V2.</p>"""
    region_linking_mode: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Determines how Amazon Web Services Regions should be linked to the Aggregator V2.</p>"""
    linked_regions: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>A list of Amazon Web Services Regions linked to the aggegation Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAggregatorV2Request) -> dict:
    out: dict = {}
    if "region_linking_mode" in value:
        out["RegionLinkingMode"] = value["region_linking_mode"]
    if "linked_regions" in value:
        import aws_sdk_securityhub.types.string_list

        out["LinkedRegions"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["linked_regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAggregatorV2Request:
    out: UpdateAggregatorV2Request = {}  # type: ignore[typeddict-item]
    if "RegionLinkingMode" in data:
        out["region_linking_mode"] = data["RegionLinkingMode"]
    if "LinkedRegions" in data:
        import aws_sdk_securityhub.types.string_list

        out["linked_regions"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["LinkedRegions"]
        )
    return out
