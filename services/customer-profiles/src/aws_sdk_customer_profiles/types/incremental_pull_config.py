"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IncrementalPullConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.datetime_type_field_name


class IncrementalPullConfig(TypedDict):
    datetime_type_field_name: NotRequired[
        "aws_sdk_customer_profiles.types.datetime_type_field_name.DatetimeTypeFieldName"
    ]
    """<p>A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalPullConfig) -> dict:
    out: dict = {}
    if "datetime_type_field_name" in value:
        out["DatetimeTypeFieldName"] = value["datetime_type_field_name"]
    return out


def deserialize_json(data: dict) -> IncrementalPullConfig:
    out: IncrementalPullConfig = {}  # type: ignore[typeddict-item]
    if "DatetimeTypeFieldName" in data:
        out["datetime_type_field_name"] = data["DatetimeTypeFieldName"]
    return out
