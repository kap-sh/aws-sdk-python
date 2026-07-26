"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteCloudWatchAlarmTemplateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteCloudWatchAlarmTemplateGroupRequest(TypedDict, closed=True):
    identifier: "capo_medialive.types.__string.__string"
    """A cloudwatch alarm template group's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCloudWatchAlarmTemplateGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCloudWatchAlarmTemplateGroupRequest:
    out: DeleteCloudWatchAlarmTemplateGroupRequest = {}  # type: ignore[typeddict-item]
    return out
