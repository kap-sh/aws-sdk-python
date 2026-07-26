"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__mapOf__stringMin0Max256PatternS``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string
    import capo_route53_recovery_control_config.types.__string_min0_max256_pattern_s

__mapOf__stringMin0Max256PatternS: TypeAlias = dict[
    "capo_route53_recovery_control_config.types.__string.__string",
    "capo_route53_recovery_control_config.types.__string_min0_max256_pattern_s.__stringMin0Max256PatternS",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: __mapOf__stringMin0Max256PatternS) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> __mapOf__stringMin0Max256PatternS:
    out: __mapOf__stringMin0Max256PatternS = {}
    for key, value in data.items():
        out[key] = value
    return out
