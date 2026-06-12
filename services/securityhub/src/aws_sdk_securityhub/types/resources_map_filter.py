"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesMapFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.map_filter
    import aws_sdk_securityhub.types.resources_map_field


class ResourcesMapFilter(TypedDict):
    field_name: NotRequired[
        "aws_sdk_securityhub.types.resources_map_field.ResourcesMapField"
    ]
    """<p>The name of the field.</p>"""
    filter: NotRequired["aws_sdk_securityhub.types.map_filter.MapFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesMapFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_securityhub.types.resources_map_field

        out["FieldName"] = aws_sdk_securityhub.types.resources_map_field.serialize_json(
            value["field_name"]
        )
    if "filter" in value:
        import aws_sdk_securityhub.types.map_filter

        out["Filter"] = aws_sdk_securityhub.types.map_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesMapFilter:
    out: ResourcesMapFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_securityhub.types.resources_map_field

        out["field_name"] = (
            aws_sdk_securityhub.types.resources_map_field.deserialize_json(
                data["FieldName"]
            )
        )
    if "Filter" in data:
        import aws_sdk_securityhub.types.map_filter

        out["filter"] = aws_sdk_securityhub.types.map_filter.deserialize_json(
            data["Filter"]
        )
    return out
