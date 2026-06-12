"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDefaultApplicationSettingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn


class GetDefaultApplicationSettingResponse(TypedDict):
    application_arn: NotRequired["aws_sdk_opensearch.types.arn.ARN"]


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
