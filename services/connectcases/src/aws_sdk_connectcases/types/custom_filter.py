"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.custom_fields_filter


class CustomFilter(TypedDict, closed=True):
    fields: NotRequired[
        "aws_sdk_connectcases.types.custom_fields_filter.CustomFieldsFilter"
    ]
    """<p>Filter conditions for custom fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomFilter) -> dict:
    out: dict = {}
    if "fields" in value:
        import aws_sdk_connectcases.types.custom_fields_filter

        out["fields"] = aws_sdk_connectcases.types.custom_fields_filter.serialize_json(
            value["fields"]
        )
    return out


def deserialize_json(data: dict) -> CustomFilter:
    out: CustomFilter = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_connectcases.types.custom_fields_filter

        out["fields"] = (
            aws_sdk_connectcases.types.custom_fields_filter.deserialize_json(
                data["fields"]
            )
        )
    return out
