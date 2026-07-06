"""Generated from Smithy shape ``com.amazonaws.textract#UndetectedSignature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.u_integer


class UndetectedSignature(TypedDict, closed=True):
    page: NotRequired["aws_sdk_textract.types.u_integer.UInteger"]
    """<p>The page where a signature was expected but not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UndetectedSignature) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UndetectedSignature:
    out: UndetectedSignature = {}  # type: ignore[typeddict-item]
    if "Page" in data:
        out["page"] = data["Page"]
    return out
