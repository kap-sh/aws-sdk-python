"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#MskMonitoringParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.msk_enhanced_monitoring_level


class MskMonitoringParameters(TypedDict, closed=True):
    enhanced_monitoring: NotRequired[
        "aws_sdk_observabilityadmin.types.msk_enhanced_monitoring_level.MskEnhancedMonitoringLevel"
    ]
    """<p> The level of enhanced monitoring for the MSK cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MskMonitoringParameters) -> dict:
    out: dict = {}
    if "enhanced_monitoring" in value:
        import aws_sdk_observabilityadmin.types.msk_enhanced_monitoring_level

        out["EnhancedMonitoring"] = (
            aws_sdk_observabilityadmin.types.msk_enhanced_monitoring_level.serialize_json(
                value["enhanced_monitoring"]
            )
        )
    return out


def deserialize_json(data: dict) -> MskMonitoringParameters:
    out: MskMonitoringParameters = {}  # type: ignore[typeddict-item]
    if "EnhancedMonitoring" in data:
        import aws_sdk_observabilityadmin.types.msk_enhanced_monitoring_level

        out["enhanced_monitoring"] = (
            aws_sdk_observabilityadmin.types.msk_enhanced_monitoring_level.deserialize_json(
                data["EnhancedMonitoring"]
            )
        )
    return out
