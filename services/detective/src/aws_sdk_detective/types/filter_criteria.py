"""Generated from Smithy shape ``com.amazonaws.detective#FilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.date_filter
    import aws_sdk_detective.types.string_filter


class FilterCriteria(TypedDict):
    severity: NotRequired["aws_sdk_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the severity.</p>"""
    status: NotRequired["aws_sdk_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the status.</p>"""
    state: NotRequired["aws_sdk_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the state.</p>"""
    entity_arn: NotRequired["aws_sdk_detective.types.string_filter.StringFilter"]
    """<p>Filter the investigation results based on the Amazon Resource Name (ARN) of the entity.</p>"""
    created_time: NotRequired["aws_sdk_detective.types.date_filter.DateFilter"]
    """<p>Filter the investigation results based on when the investigation was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "severity" in value:
        import aws_sdk_detective.types.string_filter

        out["Severity"] = aws_sdk_detective.types.string_filter.serialize_json(
            value["severity"]
        )
    if "status" in value:
        import aws_sdk_detective.types.string_filter

        out["Status"] = aws_sdk_detective.types.string_filter.serialize_json(
            value["status"]
        )
    if "state" in value:
        import aws_sdk_detective.types.string_filter

        out["State"] = aws_sdk_detective.types.string_filter.serialize_json(
            value["state"]
        )
    if "entity_arn" in value:
        import aws_sdk_detective.types.string_filter

        out["EntityArn"] = aws_sdk_detective.types.string_filter.serialize_json(
            value["entity_arn"]
        )
    if "created_time" in value:
        import aws_sdk_detective.types.date_filter

        out["CreatedTime"] = aws_sdk_detective.types.date_filter.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if "Severity" in data:
        import aws_sdk_detective.types.string_filter

        out["severity"] = aws_sdk_detective.types.string_filter.deserialize_json(
            data["Severity"]
        )
    if "Status" in data:
        import aws_sdk_detective.types.string_filter

        out["status"] = aws_sdk_detective.types.string_filter.deserialize_json(
            data["Status"]
        )
    if "State" in data:
        import aws_sdk_detective.types.string_filter

        out["state"] = aws_sdk_detective.types.string_filter.deserialize_json(
            data["State"]
        )
    if "EntityArn" in data:
        import aws_sdk_detective.types.string_filter

        out["entity_arn"] = aws_sdk_detective.types.string_filter.deserialize_json(
            data["EntityArn"]
        )
    if "CreatedTime" in data:
        import aws_sdk_detective.types.date_filter

        out["created_time"] = aws_sdk_detective.types.date_filter.deserialize_json(
            data["CreatedTime"]
        )
    return out
