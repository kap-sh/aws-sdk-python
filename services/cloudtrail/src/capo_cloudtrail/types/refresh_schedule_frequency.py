"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RefreshScheduleFrequency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.refresh_schedule_frequency_unit
    import capo_cloudtrail.types.refresh_schedule_frequency_value


class RefreshScheduleFrequency(TypedDict, closed=True):
    unit: NotRequired[
        "capo_cloudtrail.types.refresh_schedule_frequency_unit.RefreshScheduleFrequencyUnit"
    ]
    """<p> The unit to use for the refresh. </p> <p>For custom dashboards, the unit can be <code>HOURS</code> or <code>DAYS</code>.</p> <p>For the Highlights dashboard, the <code>Unit</code> must be <code>HOURS</code>.</p>"""
    value: NotRequired[
        "capo_cloudtrail.types.refresh_schedule_frequency_value.RefreshScheduleFrequencyValue"
    ]
    """<p> The value for the refresh schedule. </p> <p> For custom dashboards, the following values are valid when the unit is <code>HOURS</code>: <code>1</code>, <code>6</code>, <code>12</code>, <code>24</code> </p> <p>For custom dashboards, the only valid value when the unit is <code>DAYS</code> is <code>1</code>.</p> <p>For the Highlights dashboard, the <code>Value</code> must be <code>6</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshScheduleFrequency) -> dict:
    out: dict = {}
    if "unit" in value:
        import capo_cloudtrail.types.refresh_schedule_frequency_unit

        out["Unit"] = (
            capo_cloudtrail.types.refresh_schedule_frequency_unit.serialize_aws_json_1_1(
                value["unit"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshScheduleFrequency:
    out: RefreshScheduleFrequency = {}  # type: ignore[typeddict-item]
    if "Unit" in data:
        import capo_cloudtrail.types.refresh_schedule_frequency_unit

        out["unit"] = (
            capo_cloudtrail.types.refresh_schedule_frequency_unit.deserialize_aws_json_1_1(
                data["Unit"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
