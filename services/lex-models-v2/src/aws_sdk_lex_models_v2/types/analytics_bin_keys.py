"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsBinKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_bin_key

AnalyticsBinKeys: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_bin_key.AnalyticsBinKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsBinKeys) -> list:
    import aws_sdk_lex_models_v2.types.analytics_bin_key

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.analytics_bin_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalyticsBinKeys:
    import aws_sdk_lex_models_v2.types.analytics_bin_key

    out: AnalyticsBinKeys = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.analytics_bin_key.deserialize_json(item))
    return out
