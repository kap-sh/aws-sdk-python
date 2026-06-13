"""Generated from Smithy shape ``com.amazonaws.mgn#LifeCycleLastCutoverReverted``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.iso8601_datetime_string


class LifeCycleLastCutoverReverted(TypedDict):
    api_call_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Lifecycle last Cutover reverted API call date time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastCutoverReverted) -> dict:
    out: dict = {}
    if "api_call_date_time" in value:
        out["apiCallDateTime"] = value["api_call_date_time"]
    return out


def deserialize_json(data: dict) -> LifeCycleLastCutoverReverted:
    out: LifeCycleLastCutoverReverted = {}  # type: ignore[typeddict-item]
    if "apiCallDateTime" in data:
        out["api_call_date_time"] = data["apiCallDateTime"]
    return out
