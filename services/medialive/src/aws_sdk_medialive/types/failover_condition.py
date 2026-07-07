"""Generated from Smithy shape ``com.amazonaws.medialive#FailoverCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.failover_condition_settings


class FailoverCondition(TypedDict, closed=True):
    failover_condition_settings: NotRequired[
        "aws_sdk_medialive.types.failover_condition_settings.FailoverConditionSettings"
    ]
    """Failover condition type-specific settings."""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverCondition) -> dict:
    out: dict = {}
    if "failover_condition_settings" in value:
        import aws_sdk_medialive.types.failover_condition_settings

        out["failoverConditionSettings"] = (
            aws_sdk_medialive.types.failover_condition_settings.serialize_json(
                value["failover_condition_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FailoverCondition:
    out: FailoverCondition = {}  # type: ignore[typeddict-item]
    if "failoverConditionSettings" in data:
        import aws_sdk_medialive.types.failover_condition_settings

        out["failover_condition_settings"] = (
            aws_sdk_medialive.types.failover_condition_settings.deserialize_json(
                data["failoverConditionSettings"]
            )
        )
    return out
