"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceFiles``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.file_information


class ReferenceFiles(TypedDict):
    source: NotRequired["aws_sdk_omics.types.file_information.FileInformation"]
    """<p>The source file's location in Amazon S3.</p>"""
    index: NotRequired["aws_sdk_omics.types.file_information.FileInformation"]
    """<p>The files' index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceFiles) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_omics.types.file_information

        out["source"] = aws_sdk_omics.types.file_information.serialize_json(
            value["source"]
        )
    if "index" in value:
        import aws_sdk_omics.types.file_information

        out["index"] = aws_sdk_omics.types.file_information.serialize_json(
            value["index"]
        )
    return out


def deserialize_json(data: dict) -> ReferenceFiles:
    out: ReferenceFiles = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_omics.types.file_information

        out["source"] = aws_sdk_omics.types.file_information.deserialize_json(
            data["source"]
        )
    if "index" in data:
        import aws_sdk_omics.types.file_information

        out["index"] = aws_sdk_omics.types.file_information.deserialize_json(
            data["index"]
        )
    return out
