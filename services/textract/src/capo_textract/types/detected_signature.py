"""Generated from Smithy shape ``com.amazonaws.textract#DetectedSignature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.u_integer


class DetectedSignature(TypedDict, closed=True):
    page: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The page a detected signature was found on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectedSignature) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectedSignature:
    out: DetectedSignature = {}  # type: ignore[typeddict-item]
    if "Page" in data:
        out["page"] = data["Page"]
    return out
