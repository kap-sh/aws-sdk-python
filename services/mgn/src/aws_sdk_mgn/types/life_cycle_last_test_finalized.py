"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleLastTestFinalized``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string


class LifeCycleLastTestFinalized(TypedDict):
    api_call_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Lifecycle Test failed API call date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastTestFinalized) -> dict:
    out: dict = {}
    if "api_call_date_time" in value:
        out["apiCallDateTime"] = value["api_call_date_time"]
    return out


def deserialize_json(data: dict) -> LifeCycleLastTestFinalized:
    out: LifeCycleLastTestFinalized = {}  # type: ignore[typeddict-item]
    if "apiCallDateTime" in data:
        out["api_call_date_time"] = data["apiCallDateTime"]
    return out
