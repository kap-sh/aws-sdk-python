"""Generated from Smithy shape ``com.amazonaws.appflow#IncrementalPullConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.datetime_type_field_name


class IncrementalPullConfig(TypedDict, closed=True):
    datetime_type_field_name: NotRequired[
        "capo_appflow.types.datetime_type_field_name.DatetimeTypeFieldName"
    ]
    """<p> A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalPullConfig) -> dict:
    out: dict = {}
    if "datetime_type_field_name" in value:
        out["datetimeTypeFieldName"] = value["datetime_type_field_name"]
    return out


def deserialize_json(data: dict) -> IncrementalPullConfig:
    out: IncrementalPullConfig = {}  # type: ignore[typeddict-item]
    if "datetimeTypeFieldName" in data:
        out["datetime_type_field_name"] = data["datetimeTypeFieldName"]
    return out
