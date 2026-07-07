"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
    ]
    """<p>The tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["Tags"] = (
            aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["tags"] = (
            aws_sdk_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.deserialize_json(
                data["Tags"]
            )
        )
    return out
