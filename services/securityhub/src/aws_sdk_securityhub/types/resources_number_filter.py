"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesNumberFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.number_filter
    import aws_sdk_securityhub.types.resources_number_field


class ResourcesNumberFilter(TypedDict):
    field_name: NotRequired[
        "aws_sdk_securityhub.types.resources_number_field.ResourcesNumberField"
    ]
    """<p>The name of the field.</p>"""
    filter: NotRequired["aws_sdk_securityhub.types.number_filter.NumberFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesNumberFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_securityhub.types.resources_number_field

        out["FieldName"] = (
            aws_sdk_securityhub.types.resources_number_field.serialize_json(
                value["field_name"]
            )
        )
    if "filter" in value:
        import aws_sdk_securityhub.types.number_filter

        out["Filter"] = aws_sdk_securityhub.types.number_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesNumberFilter:
    out: ResourcesNumberFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_securityhub.types.resources_number_field

        out["field_name"] = (
            aws_sdk_securityhub.types.resources_number_field.deserialize_json(
                data["FieldName"]
            )
        )
    if "Filter" in data:
        import aws_sdk_securityhub.types.number_filter

        out["filter"] = aws_sdk_securityhub.types.number_filter.deserialize_json(
            data["Filter"]
        )
    return out
