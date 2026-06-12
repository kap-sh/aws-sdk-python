"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateRealtimeLogConfigResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.realtime_log_config


class UpdateRealtimeLogConfigResult(TypedDict):
    realtime_log_config: NotRequired[
        "aws_sdk_cloudfront.types.realtime_log_config.RealtimeLogConfig"
    ]
    """<p>A real-time log configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateRealtimeLogConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "realtime_log_config" in value:
        import aws_sdk_cloudfront.types.realtime_log_config

        aws_sdk_cloudfront.types.realtime_log_config.serialize_xml(
            value["realtime_log_config"], el, "RealtimeLogConfig"
        )


def deserialize_xml(el: Element) -> UpdateRealtimeLogConfigResult:
    out: UpdateRealtimeLogConfigResult = {}  # type: ignore[typeddict-item]
    child_realtime_log_config = el.find("RealtimeLogConfig")
    if child_realtime_log_config is not None:
        import aws_sdk_cloudfront.types.realtime_log_config

        out["realtime_log_config"] = (
            aws_sdk_cloudfront.types.realtime_log_config.deserialize_xml(
                child_realtime_log_config
            )
        )
    return out
