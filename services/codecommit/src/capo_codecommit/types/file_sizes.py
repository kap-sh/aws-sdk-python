"""Generated from Smithy shape ``com.amazonaws.codecommit#FileSizes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_size


class FileSizes(TypedDict, closed=True):
    source: "capo_codecommit.types.file_size.FileSize"
    """<p>The size of a file in the source of a merge or pull request.</p>"""
    destination: "capo_codecommit.types.file_size.FileSize"
    """<p>The size of a file in the destination of a merge or pull request.</p>"""
    base: "capo_codecommit.types.file_size.FileSize"
    """<p>The size of a file in the base of a merge or pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSizes) -> dict:
    out: dict = {}
    out["source"] = value.get("source", 0)
    out["destination"] = value.get("destination", 0)
    out["base"] = value.get("base", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSizes:
    out: FileSizes = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        out["source"] = 0
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        out["destination"] = 0
    if "base" in data:
        out["base"] = data["base"]
    else:
        out["base"] = 0
    return out
