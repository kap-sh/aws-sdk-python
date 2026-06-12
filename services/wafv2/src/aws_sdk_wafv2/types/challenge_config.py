"""Generated from Smithy shape ``com.amazonaws.wafv2#ChallengeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.immunity_time_property


class ChallengeConfig(TypedDict):
    immunity_time_property: NotRequired[
        "aws_sdk_wafv2.types.immunity_time_property.ImmunityTimeProperty"
    ]
    """<p>Determines how long a challenge timestamp in the token remains valid after the client successfully responds to a challenge. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeConfig) -> dict:
    out: dict = {}
    if "immunity_time_property" in value:
        import aws_sdk_wafv2.types.immunity_time_property

        out["ImmunityTimeProperty"] = (
            aws_sdk_wafv2.types.immunity_time_property.serialize_aws_json_1_1(
                value["immunity_time_property"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChallengeConfig:
    out: ChallengeConfig = {}  # type: ignore[typeddict-item]
    if "ImmunityTimeProperty" in data:
        import aws_sdk_wafv2.types.immunity_time_property

        out["immunity_time_property"] = (
            aws_sdk_wafv2.types.immunity_time_property.deserialize_aws_json_1_1(
                data["ImmunityTimeProperty"]
            )
        )
    return out
