"""Generated from Smithy shape ``com.amazonaws.omics#ETag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.e_tag_algorithm


class ETag(TypedDict, closed=True):
    algorithm: NotRequired["aws_sdk_omics.types.e_tag_algorithm.ETagAlgorithm"]
    """<p>The algorithm used to calculate the read set’s ETag(s).</p>"""
    source1: NotRequired["str"]
    """<p>The ETag hash calculated on Source1 of the read set.</p>"""
    source2: NotRequired["str"]
    """<p>The ETag hash calculated on Source2 of the read set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ETag) -> dict:
    out: dict = {}
    if "algorithm" in value:
        out["algorithm"] = value["algorithm"]
    if "source1" in value:
        out["source1"] = value["source1"]
    if "source2" in value:
        out["source2"] = value["source2"]
    return out


def deserialize_json(data: dict) -> ETag:
    out: ETag = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        out["algorithm"] = data["algorithm"]
    if "source1" in data:
        out["source1"] = data["source1"]
    if "source2" in data:
        out["source2"] = data["source2"]
    return out
