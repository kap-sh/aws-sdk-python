"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsSessionGroupByKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_group_by_key

AnalyticsSessionGroupByKeys: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.analytics_session_group_by_key.AnalyticsSessionGroupByKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsSessionGroupByKeys) -> list:
    import aws_sdk_lex_models_v2.types.analytics_session_group_by_key

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_group_by_key.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnalyticsSessionGroupByKeys:
    import aws_sdk_lex_models_v2.types.analytics_session_group_by_key

    out: AnalyticsSessionGroupByKeys = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.analytics_session_group_by_key.deserialize_json(
                item
            )
        )
    return out
