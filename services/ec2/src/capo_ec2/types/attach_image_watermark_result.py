"""Generated from Smithy shape ``com.amazonaws.ec2#AttachImageWatermarkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AttachImageWatermarkResult(TypedDict, closed=True):
    watermark_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The watermark identifier, in <code>accountId:watermarkName</code> format (for example, <code>123456789012:approvedAmi</code>).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachImageWatermarkResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "watermark_key" in value:
        pairs.append((f"{key_prefix}WatermarkKey", str(value["watermark_key"])))


def deserialize_ec2_query(el: Element) -> AttachImageWatermarkResult:
    out: AttachImageWatermarkResult = {}  # type: ignore[typeddict-item]
    child_watermark_key = el.find("watermarkKey")
    if child_watermark_key is not None:
        out["watermark_key"] = str(child_watermark_key.text or "")
    return out
