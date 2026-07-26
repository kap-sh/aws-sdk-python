"""Generated from Smithy shape ``com.amazonaws.b2bi#SampleDocumentKeys``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.s3_key


class SampleDocumentKeys(TypedDict, closed=True):
    input: NotRequired["capo_b2bi.types.s3_key.S3Key"]
    """<p>An array of keys for your input sample documents.</p>"""
    output: NotRequired["capo_b2bi.types.s3_key.S3Key"]
    """<p>An array of keys for your output sample documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SampleDocumentKeys) -> dict:
    out: dict = {}
    if "input" in value:
        out["input"] = value["input"]
    if "output" in value:
        out["output"] = value["output"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SampleDocumentKeys:
    out: SampleDocumentKeys = {}  # type: ignore[typeddict-item]
    if "input" in data:
        out["input"] = data["input"]
    if "output" in data:
        out["output"] = data["output"]
    return out
