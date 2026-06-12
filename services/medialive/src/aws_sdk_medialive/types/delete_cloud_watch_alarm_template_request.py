"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteCloudWatchAlarmTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteCloudWatchAlarmTemplateRequest(TypedDict):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """A cloudwatch alarm template's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCloudWatchAlarmTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCloudWatchAlarmTemplateRequest:
    out: DeleteCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
