"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListRealtimeLogConfigsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.realtime_log_configs


class ListRealtimeLogConfigsResult(TypedDict, closed=True):
    realtime_log_configs: NotRequired[
        "capo_cloudfront.types.realtime_log_configs.RealtimeLogConfigs"
    ]
    """<p>A list of real-time log configurations.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListRealtimeLogConfigsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "realtime_log_configs" in value:
        import capo_cloudfront.types.realtime_log_configs

        capo_cloudfront.types.realtime_log_configs.serialize_xml(
            value["realtime_log_configs"], el, "RealtimeLogConfigs"
        )


def deserialize_xml(el: Element) -> ListRealtimeLogConfigsResult:
    out: ListRealtimeLogConfigsResult = {}  # type: ignore[typeddict-item]
    child_realtime_log_configs = el.find("RealtimeLogConfigs")
    if child_realtime_log_configs is not None:
        import capo_cloudfront.types.realtime_log_configs

        out["realtime_log_configs"] = (
            capo_cloudfront.types.realtime_log_configs.deserialize_xml(
                child_realtime_log_configs
            )
        )
    return out
