"""Generated from Smithy shape ``com.amazonaws.b2bi#X12Delimiters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_component_separator
    import aws_sdk_b2bi.types.x12_data_element_separator
    import aws_sdk_b2bi.types.x12_segment_terminator


class X12Delimiters(TypedDict):
    component_separator: NotRequired[
        "aws_sdk_b2bi.types.x12_component_separator.X12ComponentSeparator"
    ]
    """<p>The component, or sub-element, separator. The default value is <code>:</code> (colon).</p>"""
    data_element_separator: NotRequired[
        "aws_sdk_b2bi.types.x12_data_element_separator.X12DataElementSeparator"
    ]
    """<p>The data element separator. The default value is <code>*</code> (asterisk).</p>"""
    segment_terminator: NotRequired[
        "aws_sdk_b2bi.types.x12_segment_terminator.X12SegmentTerminator"
    ]
    """<p>The segment terminator. The default value is <code>~</code> (tilde).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12Delimiters) -> dict:
    out: dict = {}
    if "component_separator" in value:
        out["componentSeparator"] = value["component_separator"]
    if "data_element_separator" in value:
        out["dataElementSeparator"] = value["data_element_separator"]
    if "segment_terminator" in value:
        out["segmentTerminator"] = value["segment_terminator"]
    return out


def deserialize_aws_json_1_0(data: dict) -> X12Delimiters:
    out: X12Delimiters = {}  # type: ignore[typeddict-item]
    if "componentSeparator" in data:
        out["component_separator"] = data["componentSeparator"]
    if "dataElementSeparator" in data:
        out["data_element_separator"] = data["dataElementSeparator"]
    if "segmentTerminator" in data:
        out["segment_terminator"] = data["segmentTerminator"]
    return out
