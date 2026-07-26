"""Generated from Smithy shape ``com.amazonaws.dlm#FastRestoreRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.availability_zone_id_list
    import capo_dlm.types.availability_zone_list
    import capo_dlm.types.count
    import capo_dlm.types.interval
    import capo_dlm.types.retention_interval_unit_values


class FastRestoreRule(TypedDict, closed=True):
    count: NotRequired["capo_dlm.types.count.Count"]
    """<p>The number of snapshots to be enabled with fast snapshot restore.</p>"""
    interval: NotRequired["capo_dlm.types.interval.Interval"]
    """<p>The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.</p>"""
    interval_unit: NotRequired[
        "capo_dlm.types.retention_interval_unit_values.RetentionIntervalUnitValues"
    ]
    """<p>The unit of time for enabling fast snapshot restore.</p>"""
    availability_zones: NotRequired[
        "capo_dlm.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The Availability Zones in which to enable fast snapshot restore.</p>"""
    availability_zone_ids: NotRequired[
        "capo_dlm.types.availability_zone_id_list.AvailabilityZoneIdList"
    ]
    """<p>The Availability Zone Ids in which to enable fast snapshot restore.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FastRestoreRule) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    if "interval" in value:
        out["Interval"] = value["interval"]
    if "interval_unit" in value:
        import capo_dlm.types.retention_interval_unit_values

        out["IntervalUnit"] = (
            capo_dlm.types.retention_interval_unit_values.serialize_json(
                value["interval_unit"]
            )
        )
    if "availability_zones" in value:
        import capo_dlm.types.availability_zone_list

        out["AvailabilityZones"] = capo_dlm.types.availability_zone_list.serialize_json(
            value["availability_zones"]
        )
    if "availability_zone_ids" in value:
        import capo_dlm.types.availability_zone_id_list

        out["AvailabilityZoneIds"] = (
            capo_dlm.types.availability_zone_id_list.serialize_json(
                value["availability_zone_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> FastRestoreRule:
    out: FastRestoreRule = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    if "Interval" in data:
        out["interval"] = data["Interval"]
    if "IntervalUnit" in data:
        import capo_dlm.types.retention_interval_unit_values

        out["interval_unit"] = (
            capo_dlm.types.retention_interval_unit_values.deserialize_json(
                data["IntervalUnit"]
            )
        )
    if "AvailabilityZones" in data:
        import capo_dlm.types.availability_zone_list

        out["availability_zones"] = (
            capo_dlm.types.availability_zone_list.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if "AvailabilityZoneIds" in data:
        import capo_dlm.types.availability_zone_id_list

        out["availability_zone_ids"] = (
            capo_dlm.types.availability_zone_id_list.deserialize_json(
                data["AvailabilityZoneIds"]
            )
        )
    return out
