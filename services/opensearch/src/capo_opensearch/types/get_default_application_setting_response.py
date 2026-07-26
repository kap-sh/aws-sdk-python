"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDefaultApplicationSettingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn


class GetDefaultApplicationSettingResponse(TypedDict, closed=True):
    application_arn: NotRequired["capo_opensearch.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: GetDefaultApplicationSettingResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> GetDefaultApplicationSettingResponse:
    out: GetDefaultApplicationSettingResponse = {}  # type: ignore[typeddict-item]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    return out
