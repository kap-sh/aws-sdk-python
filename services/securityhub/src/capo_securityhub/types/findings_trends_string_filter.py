"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsTrendsStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.findings_trends_string_field
    import capo_securityhub.types.string_filter


class FindingsTrendsStringFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.findings_trends_string_field.FindingsTrendsStringField"
    ]
    """<p>The name of the findings field to filter on.</p>"""
    filter: NotRequired["capo_securityhub.types.string_filter.StringFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsTrendsStringFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.findings_trends_string_field

        out["FieldName"] = (
            capo_securityhub.types.findings_trends_string_field.serialize_json(
                value["field_name"]
            )
        )
    if "filter" in value:
        import capo_securityhub.types.string_filter

        out["Filter"] = capo_securityhub.types.string_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> FindingsTrendsStringFilter:
    out: FindingsTrendsStringFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import capo_securityhub.types.findings_trends_string_field

        out["field_name"] = (
            capo_securityhub.types.findings_trends_string_field.deserialize_json(
                data["FieldName"]
            )
        )
    if "Filter" in data:
        import capo_securityhub.types.string_filter

        out["filter"] = capo_securityhub.types.string_filter.deserialize_json(
            data["Filter"]
        )
    return out
