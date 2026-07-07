"""Generated from Smithy shape ``com.amazonaws.omics#TsvVersionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.annotation_type
    import aws_sdk_omics.types.format_to_header
    import aws_sdk_omics.types.schema


class TsvVersionOptions(TypedDict, closed=True):
    annotation_type: NotRequired["aws_sdk_omics.types.annotation_type.AnnotationType"]
    """<p> The store version's annotation type. </p>"""
    format_to_header: NotRequired["aws_sdk_omics.types.format_to_header.FormatToHeader"]
    """<p> The annotation store version's header key to column name mapping. </p>"""
    schema: NotRequired["aws_sdk_omics.types.schema.Schema"]
    """<p> The TSV schema for an annotation store version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TsvVersionOptions) -> dict:
    out: dict = {}
    if "annotation_type" in value:
        out["annotationType"] = value["annotation_type"]
    if "format_to_header" in value:
        import aws_sdk_omics.types.format_to_header

        out["formatToHeader"] = aws_sdk_omics.types.format_to_header.serialize_json(
            value["format_to_header"]
        )
    if "schema" in value:
        import aws_sdk_omics.types.schema

        out["schema"] = aws_sdk_omics.types.schema.serialize_json(value["schema"])
    return out


def deserialize_json(data: dict) -> TsvVersionOptions:
    out: TsvVersionOptions = {}  # type: ignore[typeddict-item]
    if "annotationType" in data:
        out["annotation_type"] = data["annotationType"]
    if "formatToHeader" in data:
        import aws_sdk_omics.types.format_to_header

        out["format_to_header"] = aws_sdk_omics.types.format_to_header.deserialize_json(
            data["formatToHeader"]
        )
    if "schema" in data:
        import aws_sdk_omics.types.schema

        out["schema"] = aws_sdk_omics.types.schema.deserialize_json(data["schema"])
    return out
