"""Generated from Smithy shape ``com.amazonaws.wafv2#CaptchaConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.immunity_time_property


class CaptchaConfig(TypedDict, closed=True):
    immunity_time_property: NotRequired[
        "capo_wafv2.types.immunity_time_property.ImmunityTimeProperty"
    ]
    """<p>Determines how long a <code>CAPTCHA</code> timestamp in the token remains valid after the client successfully solves a <code>CAPTCHA</code> puzzle. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptchaConfig) -> dict:
    out: dict = {}
    if "immunity_time_property" in value:
        import capo_wafv2.types.immunity_time_property

        out["ImmunityTimeProperty"] = (
            capo_wafv2.types.immunity_time_property.serialize_aws_json_1_1(
                value["immunity_time_property"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CaptchaConfig:
    out: CaptchaConfig = {}  # type: ignore[typeddict-item]
    if "ImmunityTimeProperty" in data:
        import capo_wafv2.types.immunity_time_property

        out["immunity_time_property"] = (
            capo_wafv2.types.immunity_time_property.deserialize_aws_json_1_1(
                data["ImmunityTimeProperty"]
            )
        )
    return out
