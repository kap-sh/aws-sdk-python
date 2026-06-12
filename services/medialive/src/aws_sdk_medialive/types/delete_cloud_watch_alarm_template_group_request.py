"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteCloudWatchAlarmTemplateGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteCloudWatchAlarmTemplateGroupRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """A cloudwatch alarm template group's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCloudWatchAlarmTemplateGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCloudWatchAlarmTemplateGroupRequest:
    out: DeleteCloudWatchAlarmTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    return out
