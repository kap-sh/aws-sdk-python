"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionGroupByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_group_by_specification

AnalyticsSessionGroupByList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_session_group_by_specification.AnalyticsSessionGroupBySpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionGroupByList) -> list:
    import aws_sdk_lex_models_v2.types.analytics_session_group_by_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_group_by_specification.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionGroupByList:
    import aws_sdk_lex_models_v2.types.analytics_session_group_by_specification

    out: AnalyticsSessionGroupByList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_group_by_specification.deserialize_json(
                item
            )
        )
    return out
