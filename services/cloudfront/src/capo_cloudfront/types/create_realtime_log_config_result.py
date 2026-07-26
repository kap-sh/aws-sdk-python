"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateRealtimeLogConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.realtime_log_config


class CreateRealtimeLogConfigResult(TypedDict, closed=True):
    realtime_log_config: NotRequired[
        "capo_cloudfront.types.realtime_log_config.RealtimeLogConfig"
    ]
    """<p>A real-time log configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateRealtimeLogConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "realtime_log_config" in value:
        import capo_cloudfront.types.realtime_log_config

        capo_cloudfront.types.realtime_log_config.serialize_xml(
            value["realtime_log_config"], el, "RealtimeLogConfig"
        )


def deserialize_xml(el: Element) -> CreateRealtimeLogConfigResult:
    out: CreateRealtimeLogConfigResult = {}  # type: ignore[typeddict-item]
    child_realtime_log_config = el.find("RealtimeLogConfig")
    if child_realtime_log_config is not None:
        import capo_cloudfront.types.realtime_log_config

        out["realtime_log_config"] = (
            capo_cloudfront.types.realtime_log_config.deserialize_xml(
                child_realtime_log_config
            )
        )
    return out
