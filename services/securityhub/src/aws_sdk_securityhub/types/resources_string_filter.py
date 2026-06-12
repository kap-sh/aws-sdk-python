"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesStringFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_string_field
    import aws_sdk_securityhub.types.string_filter


class ResourcesStringFilter(TypedDict):
    field_name: NotRequired[
        "aws_sdk_securityhub.types.resources_string_field.ResourcesStringField"
    ]
    """<p>The name of the field.</p>"""
    filter: NotRequired["aws_sdk_securityhub.types.string_filter.StringFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesStringFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_securityhub.types.resources_string_field

        out["FieldName"] = (
            aws_sdk_securityhub.types.resources_string_field.serialize_json(
                value["field_name"]
            )
        )
    if "filter" in value:
        import aws_sdk_securityhub.types.string_filter

        out["Filter"] = aws_sdk_securityhub.types.string_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesStringFilter:
    out: ResourcesStringFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_securityhub.types.resources_string_field

        out["field_name"] = (
            aws_sdk_securityhub.types.resources_string_field.deserialize_json(
                data["FieldName"]
            )
        )
    if "Filter" in data:
        import aws_sdk_securityhub.types.string_filter

        out["filter"] = aws_sdk_securityhub.types.string_filter.deserialize_json(
            data["Filter"]
        )
    return out
