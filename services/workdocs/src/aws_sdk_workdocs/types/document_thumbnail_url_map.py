"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentThumbnailUrlMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.document_thumbnail_type
    import aws_sdk_workdocs.types.url_type

DocumentThumbnailUrlMap: TypeAlias = dict[
    "aws_sdk_workdocs.types.document_thumbnail_type.DocumentThumbnailType",
    "aws_sdk_workdocs.types.url_type.UrlType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DocumentThumbnailUrlMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_workdocs.types.document_thumbnail_type

        out[aws_sdk_workdocs.types.document_thumbnail_type.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> DocumentThumbnailUrlMap:
    out: DocumentThumbnailUrlMap = {}
    for key, value in data.items():
        import aws_sdk_workdocs.types.document_thumbnail_type

        out[aws_sdk_workdocs.types.document_thumbnail_type.deserialize_json(key)] = (
            value
        )
    return out
