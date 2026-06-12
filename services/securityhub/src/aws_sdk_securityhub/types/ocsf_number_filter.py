"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfNumberFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.number_filter
    import aws_sdk_securityhub.types.ocsf_number_field


class OcsfNumberFilter(TypedDict):
    field_name: NotRequired[
        "aws_sdk_securityhub.types.ocsf_number_field.OcsfNumberField"
    ]
    """<p>The name of the field.</p>"""
    filter: NotRequired["aws_sdk_securityhub.types.number_filter.NumberFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfNumberFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_securityhub.types.ocsf_number_field

        out["FieldName"] = aws_sdk_securityhub.types.ocsf_number_field.serialize_json(
            value["field_name"]
        )
    if "filter" in value:
        import aws_sdk_securityhub.types.number_filter

        out["Filter"] = aws_sdk_securityhub.types.number_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> OcsfNumberFilter:
    out: OcsfNumberFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_securityhub.types.ocsf_number_field

        out["field_name"] = (
            aws_sdk_securityhub.types.ocsf_number_field.deserialize_json(
                data["FieldName"]
            )
        )
    if "Filter" in data:
        import aws_sdk_securityhub.types.number_filter

        out["filter"] = aws_sdk_securityhub.types.number_filter.deserialize_json(
            data["Filter"]
        )
    return out
