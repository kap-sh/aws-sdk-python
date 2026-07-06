"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.date_filter
    import aws_sdk_securityhub.types.ocsf_date_field


class OcsfDateFilter(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_securityhub.types.ocsf_date_field.OcsfDateField"]
    """<p>The name of the field.</p>"""
    filter: NotRequired["aws_sdk_securityhub.types.date_filter.DateFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfDateFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_securityhub.types.ocsf_date_field

        out["FieldName"] = aws_sdk_securityhub.types.ocsf_date_field.serialize_json(
            value["field_name"]
        )
    if "filter" in value:
        import aws_sdk_securityhub.types.date_filter

        out["Filter"] = aws_sdk_securityhub.types.date_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> OcsfDateFilter:
    out: OcsfDateFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_securityhub.types.ocsf_date_field

        out["field_name"] = aws_sdk_securityhub.types.ocsf_date_field.deserialize_json(
            data["FieldName"]
        )
    if "Filter" in data:
        import aws_sdk_securityhub.types.date_filter

        out["filter"] = aws_sdk_securityhub.types.date_filter.deserialize_json(
            data["Filter"]
        )
    return out
