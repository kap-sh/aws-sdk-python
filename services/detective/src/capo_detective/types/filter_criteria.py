"""Generated from Smithy shape ``com.amazonaws.detective#FilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.date_filter
    import capo_detective.types.string_filter


class FilterCriteria(TypedDict, closed=True):
    severity: NotRequired["capo_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the severity.</p>"""
    status: NotRequired["capo_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the status.</p>"""
    state: NotRequired["capo_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the state.</p>"""
    entity_arn: NotRequired["capo_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the Amazon Resource Name (ARN) of the entity.</p>"""
    created_time: NotRequired["capo_detective.types.date_filter.DateFilter"]
    """<p>Filter the investigation results based on when the investigation was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "severity" in value:
        import capo_detective.types.string_filter

        out["Severity"] = capo_detective.types.string_filter.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import capo_detective.types.string_filter

        out["Status"] = capo_detective.types.string_filter.serialize_json(
            value["status"]
        )
    if "state" in value:
        import capo_detective.types.string_filter

        out["State"] = capo_detective.types.string_filter.serialize_json(value["state"])
    if "entity_arn" in value:
        import capo_detective.types.string_filter

        out["EntityArn"] = capo_detective.types.string_filter.serialize_json(
            value["entity_arn"]
        )
    if "created_time" in value:
        import capo_detective.types.date_filter

        out["CreatedTime"] = capo_detective.types.date_filter.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if "Severity" in data:
        import capo_detective.types.string_filter

        out["severity"] = capo_detective.types.string_filter.deserialize_json(
            data["Severity"]
        )
    if "Status" in data:
        import capo_detective.types.string_filter

        out["status"] = capo_detective.types.string_filter.deserialize_json(
            data["Status"]
        )
    if "State" in data:
        import capo_detective.types.string_filter

        out["state"] = capo_detective.types.string_filter.deserialize_json(
            data["State"]
        )
    if "EntityArn" in data:
        import capo_detective.types.string_filter

        out["entity_arn"] = capo_detective.types.string_filter.deserialize_json(
            data["EntityArn"]
        )
    if "CreatedTime" in data:
        import capo_detective.types.date_filter

        out["created_time"] = capo_detective.types.date_filter.deserialize_json(
            data["CreatedTime"]
        )
    return out
