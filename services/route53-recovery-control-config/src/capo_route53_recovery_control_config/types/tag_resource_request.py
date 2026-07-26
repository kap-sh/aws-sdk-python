"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s
    import capo_route53_recovery_control_config.types.__string


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) for the resource that's tagged.</p>"""
    tags: NotRequired[
        "capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
    ]
    """<p>The tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["Tags"] = (
            capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["tags"] = (
            capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.deserialize_json(
                data["Tags"]
            )
        )
    return out
