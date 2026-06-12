"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExportFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.export_filter_name
    import aws_sdk_lex_models_v2.types.export_filter_operator
    import aws_sdk_lex_models_v2.types.filter_values


class ExportFilter(TypedDict):
    name: "aws_sdk_lex_models_v2.types.export_filter_name.ExportFilterName"
    """<p>The name of the field to use for filtering.</p>"""
    values: "aws_sdk_lex_models_v2.types.filter_values.FilterValues"
    """<p>The values to use to filter the response. The values must be <code>Bot</code>, <code>BotLocale</code>, or <code>CustomVocabulary</code>.</p>"""
    operator: "aws_sdk_lex_models_v2.types.export_filter_operator.ExportFilterOperator"
    """<p>The operator to use for the filter. Specify EQ when the <code>ListExports</code> operation should return only resource types that equal the specified value. Specify CO when the <code>ListExports</code> operation should return resource types that contain the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFilter) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.export_filter_name

    out["name"] = aws_sdk_lex_models_v2.types.export_filter_name.serialize_json(
        value["name"]
    )
    import aws_sdk_lex_models_v2.types.filter_values

    out["values"] = aws_sdk_lex_models_v2.types.filter_values.serialize_json(
        value["values"]
    )
    import aws_sdk_lex_models_v2.types.export_filter_operator

    out["operator"] = aws_sdk_lex_models_v2.types.export_filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> ExportFilter:
    out: ExportFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.export_filter_name

        out["name"] = aws_sdk_lex_models_v2.types.export_filter_name.deserialize_json(
            data["name"]
        )
    else:
        raise DeserializationError("ExportFilter.name required")
    if "values" in data:
        import aws_sdk_lex_models_v2.types.filter_values

        out["values"] = aws_sdk_lex_models_v2.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("ExportFilter.values required")
    if "operator" in data:
        import aws_sdk_lex_models_v2.types.export_filter_operator

        out["operator"] = (
            aws_sdk_lex_models_v2.types.export_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("ExportFilter.operator required")
    return out
