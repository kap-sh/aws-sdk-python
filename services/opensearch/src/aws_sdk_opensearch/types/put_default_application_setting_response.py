"""Generated from Smithy shape ``com.amazonaws.opensearch#PutDefaultApplicationSettingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn


class PutDefaultApplicationSettingResponse(TypedDict):
    application_arn: NotRequired["aws_sdk_opensearch.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: PutDefaultApplicationSettingResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> PutDefaultApplicationSettingResponse:
    out: PutDefaultApplicationSettingResponse = {}  # type: ignore[typeddict-item]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    return out
