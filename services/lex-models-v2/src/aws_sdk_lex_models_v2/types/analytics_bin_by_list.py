"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsBinByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_bin_by_specification

AnalyticsBinByList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_bin_by_specification.AnalyticsBinBySpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsBinByList) -> list:
    import aws_sdk_lex_models_v2.types.analytics_bin_by_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_bin_by_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsBinByList:
    import aws_sdk_lex_models_v2.types.analytics_bin_by_specification

    out: AnalyticsBinByList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_bin_by_specification.deserialize_json(
                item
            )
        )
    return out
