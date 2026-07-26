"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteCloudWatchAlarmTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteCloudWatchAlarmTemplateRequest(TypedDict, closed=True):
    identifier: "capo_medialive.types.__string.__string"
    """A cloudwatch alarm template's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCloudWatchAlarmTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCloudWatchAlarmTemplateRequest:
    out: DeleteCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
