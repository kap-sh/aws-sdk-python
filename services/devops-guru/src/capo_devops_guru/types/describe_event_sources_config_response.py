"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeEventSourcesConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.event_sources_config


class DescribeEventSourcesConfigResponse(TypedDict, closed=True):
    event_sources: NotRequired[
        "capo_devops_guru.types.event_sources_config.EventSourcesConfig"
    ]
    """<p>Lists the event sources in the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEventSourcesConfigResponse) -> dict:
    out: dict = {}
    if "event_sources" in value:
        import capo_devops_guru.types.event_sources_config

        out["EventSources"] = (
            capo_devops_guru.types.event_sources_config.serialize_json(
                value["event_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeEventSourcesConfigResponse:
    out: DescribeEventSourcesConfigResponse = {}  # type: ignore[typeddict-item]
    if "EventSources" in data:
        import capo_devops_guru.types.event_sources_config

        out["event_sources"] = (
            capo_devops_guru.types.event_sources_config.deserialize_json(
                data["EventSources"]
            )
        )
    return out
