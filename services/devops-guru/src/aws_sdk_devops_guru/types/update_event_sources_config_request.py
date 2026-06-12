"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateEventSourcesConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.event_sources_config


class UpdateEventSourcesConfigRequest(TypedDict):
    event_sources: NotRequired[
        "aws_sdk_devops_guru.types.event_sources_config.EventSourcesConfig"
    ]
    """<p>Configuration information about the integration of DevOps Guru as the Consumer via EventBridge with another AWS Service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventSourcesConfigRequest) -> dict:
    out: dict = {}
    if "event_sources" in value:
        import aws_sdk_devops_guru.types.event_sources_config

        out["EventSources"] = (
            aws_sdk_devops_guru.types.event_sources_config.serialize_json(
                value["event_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEventSourcesConfigRequest:
    out: UpdateEventSourcesConfigRequest = {}  # type: ignore[typeddict-item]
    if "EventSources" in data:
        import aws_sdk_devops_guru.types.event_sources_config

        out["event_sources"] = (
            aws_sdk_devops_guru.types.event_sources_config.deserialize_json(
                data["EventSources"]
            )
        )
    return out
