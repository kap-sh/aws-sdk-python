"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DateTimeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.date_time_type
    import capo_bcm_dashboards.types.generic_string


class DateTimeValue(TypedDict, closed=True):
    type: "capo_bcm_dashboards.types.date_time_type.DateTimeType"
    """<p>The type of date/time value: <code>ABSOLUTE</code> for specific dates or <code>RELATIVE</code> for dynamic time periods.</p>"""
    value: "capo_bcm_dashboards.types.generic_string.GenericString"
    """<p>The actual date/time value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DateTimeValue) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.date_time_type

    out["type"] = capo_bcm_dashboards.types.date_time_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DateTimeValue:
    out: DateTimeValue = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bcm_dashboards.types.date_time_type

        out["type"] = capo_bcm_dashboards.types.date_time_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("DateTimeValue.type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("DateTimeValue.value required")
    return out
