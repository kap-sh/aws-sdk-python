"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetFiles``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.file_information


class ReadSetFiles(TypedDict, closed=True):
    source1: NotRequired["capo_omics.types.file_information.FileInformation"]
    """<p>The location of the first file in Amazon S3.</p>"""
    source2: NotRequired["capo_omics.types.file_information.FileInformation"]
    """<p>The location of the second file in Amazon S3.</p>"""
    index: NotRequired["capo_omics.types.file_information.FileInformation"]
    """<p>The files' index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetFiles) -> dict:
    out: dict = {}
    if "source1" in value:
        import capo_omics.types.file_information

        out["source1"] = capo_omics.types.file_information.serialize_json(
            value["source1"]
        )
    if "source2" in value:
        import capo_omics.types.file_information

        out["source2"] = capo_omics.types.file_information.serialize_json(
            value["source2"]
        )
    if "index" in value:
        import capo_omics.types.file_information

        out["index"] = capo_omics.types.file_information.serialize_json(value["index"])
    return out


def deserialize_json(data: dict) -> ReadSetFiles:
    out: ReadSetFiles = {}  # type: ignore[typeddict-item]
    if "source1" in data:
        import capo_omics.types.file_information

        out["source1"] = capo_omics.types.file_information.deserialize_json(
            data["source1"]
        )
    if "source2" in data:
        import capo_omics.types.file_information

        out["source2"] = capo_omics.types.file_information.deserialize_json(
            data["source2"]
        )
    if "index" in data:
        import capo_omics.types.file_information

        out["index"] = capo_omics.types.file_information.deserialize_json(data["index"])
    return out
