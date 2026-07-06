"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleLastTestReverted``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string


class LifeCycleLastTestReverted(TypedDict, closed=True):
    api_call_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Lifecycle last Test reverted API call date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastTestReverted) -> dict:
    out: dict = {}
    if "api_call_date_time" in value:
        out["apiCallDateTime"] = value["api_call_date_time"]
    return out


def deserialize_json(data: dict) -> LifeCycleLastTestReverted:
    out: LifeCycleLastTestReverted = {}  # type: ignore[typeddict-item]
    if "apiCallDateTime" in data:
        out["api_call_date_time"] = data["apiCallDateTime"]
    return out
