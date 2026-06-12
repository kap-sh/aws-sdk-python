"""Generated from Smithy shape ``com.amazonaws.medialive#GetCloudWatchAlarmTemplateGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class GetCloudWatchAlarmTemplateGroupRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """A cloudwatch alarm template group's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudWatchAlarmTemplateGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCloudWatchAlarmTemplateGroupRequest:
    out: GetCloudWatchAlarmTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    return out
