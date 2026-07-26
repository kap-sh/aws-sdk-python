"""Generated from Smithy shape ``com.amazonaws.mq#SanitizationWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__string
    import capo_mq.types.sanitization_warning_reason


class SanitizationWarning(TypedDict, closed=True):
    attribute_name: NotRequired["capo_mq.types.__string.__string"]
    """<p>The name of the configuration attribute that has been sanitized.</p>"""
    element_name: NotRequired["capo_mq.types.__string.__string"]
    """<p>The name of the configuration element that has been sanitized.</p>"""
    reason: NotRequired[
        "capo_mq.types.sanitization_warning_reason.SanitizationWarningReason"
    ]
    """<p>The reason for which the configuration elements or attributes were sanitized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SanitizationWarning) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["attributeName"] = value["attribute_name"]
    if "element_name" in value:
        out["elementName"] = value["element_name"]
    if "reason" in value:
        import capo_mq.types.sanitization_warning_reason

        out["reason"] = capo_mq.types.sanitization_warning_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> SanitizationWarning:
    out: SanitizationWarning = {}  # type: ignore[typeddict-item]
    if "attributeName" in data:
        out["attribute_name"] = data["attributeName"]
    if "elementName" in data:
        out["element_name"] = data["elementName"]
    if "reason" in data:
        import capo_mq.types.sanitization_warning_reason

        out["reason"] = capo_mq.types.sanitization_warning_reason.deserialize_json(
            data["reason"]
        )
    return out
