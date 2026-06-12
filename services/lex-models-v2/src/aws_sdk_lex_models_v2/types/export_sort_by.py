"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportSortBy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.export_sort_attribute
    import aws_sdk_lex_models_v2.types.sort_order


class ExportSortBy(TypedDict):
    attribute: "aws_sdk_lex_models_v2.types.export_sort_attribute.ExportSortAttribute"
    """<p>The export field to use for sorting.</p>"""
    order: "aws_sdk_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order to sort the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.export_sort_attribute

    out["attribute"] = aws_sdk_lex_models_v2.types.export_sort_attribute.serialize_json(
        value["attribute"]
    )
    import aws_sdk_lex_models_v2.types.sort_order

    out["order"] = aws_sdk_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> ExportSortBy:
    out: ExportSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_lex_models_v2.types.export_sort_attribute

        out["attribute"] = (
            aws_sdk_lex_models_v2.types.export_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("ExportSortBy.attribute required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.sort_order

        out["order"] = aws_sdk_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("ExportSortBy.order required")
    return out
