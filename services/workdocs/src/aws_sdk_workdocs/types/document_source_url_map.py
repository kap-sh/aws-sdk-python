"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentSourceUrlMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.document_source_type
    import aws_sdk_workdocs.types.url_type

DocumentSourceUrlMap: TypeAlias = dict[
    "aws_sdk_workdocs.types.document_source_type.DocumentSourceType",
    "aws_sdk_workdocs.types.url_type.UrlType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DocumentSourceUrlMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_workdocs.types.document_source_type

        out[aws_sdk_workdocs.types.document_source_type.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> DocumentSourceUrlMap:
    out: DocumentSourceUrlMap = {}
    for key, value in data.items():
        import aws_sdk_workdocs.types.document_source_type

        out[aws_sdk_workdocs.types.document_source_type.deserialize_json(key)] = value
    return out
