"""Generated from Smithy shape ``com.amazonaws.medialive#GetCloudWatchAlarmTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class GetCloudWatchAlarmTemplateRequest(TypedDict, closed=True):
    identifier: "aws_sdk_medialive.types.__string.__string"
    """A cloudwatch alarm template's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudWatchAlarmTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCloudWatchAlarmTemplateRequest:
    out: GetCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
