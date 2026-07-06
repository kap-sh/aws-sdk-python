"""Generated from Smithy shape ``com.amazonaws.omics#StartReferenceImportJobSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.reference_description
    import aws_sdk_omics.types.reference_name
    import aws_sdk_omics.types.s3_uri
    import aws_sdk_omics.types.tag_map


class StartReferenceImportJobSourceItem(TypedDict, closed=True):
    source_file: "aws_sdk_omics.types.s3_uri.S3Uri"
    """<p>The source file's location in Amazon S3.</p>"""
    name: "aws_sdk_omics.types.reference_name.ReferenceName"
    """<p>The source's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The source's description.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>The source's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReferenceImportJobSourceItem) -> dict:
    out: dict = {}
    out["sourceFile"] = value["source_file"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartReferenceImportJobSourceItem:
    out: StartReferenceImportJobSourceItem = {}  # type: ignore[typeddict-item]
    if "sourceFile" in data:
        out["source_file"] = data["sourceFile"]
    else:
        raise DeserializationError(
            "StartReferenceImportJobSourceItem.source_file required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartReferenceImportJobSourceItem.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    return out
