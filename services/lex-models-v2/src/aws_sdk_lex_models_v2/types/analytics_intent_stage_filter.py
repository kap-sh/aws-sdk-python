"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentStageFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_filter_operator
    import aws_sdk_lex_models_v2.types.analytics_filter_values
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_filter_name


class AnalyticsIntentStageFilter(TypedDict):
    name: "aws_sdk_lex_models_v2.types.analytics_intent_stage_filter_name.AnalyticsIntentStageFilterName"
    """<p>The category by which to filter the intent stages. The descriptions for each option are as follows:</p> <ul> <li> <p> <code>BotAlias</code> – The name of the bot alias.</p> </li> <li> <p> <code>BotVersion</code> – The version of the bot.</p> </li> <li> <p> <code>LocaleId</code> – The locale of the bot.</p> </li> <li> <p> <code>Modality</code> – The modality of the session with the bot (audio, DTMF, or text).</p> </li> <li> <p> <code>Channel</code> – The channel that the bot is integrated with.</p> </li> <li> <p> <code>SessionId</code> – The identifier of the session with the bot.</p> </li> <li> <p> <code>OriginatingRequestId</code> – The identifier of the first request in a session.</p> </li> <li> <p> <code>IntentName</code> – The name of the intent.</p> </li> <li> <p> <code>IntentStageName</code> – The stage in the intent.</p> </li> </ul>"""
    operator: (
        "aws_sdk_lex_models_v2.types.analytics_filter_operator.AnalyticsFilterOperator"
    )
    """<p>The operation by which to filter the category. The following operations are possible:</p> <ul> <li> <p> <code>CO</code> – Contains</p> </li> <li> <p> <code>EQ</code> – Equals</p> </li> <li> <p> <code>GT</code> – Greater than</p> </li> <li> <p> <code>LT</code> – Less than</p> </li> </ul> <p>The operators that each filter supports are listed below:</p> <ul> <li> <p> <code>BotAlias</code> – <code>EQ</code>.</p> </li> <li> <p> <code>BotVersion</code> – <code>EQ</code>.</p> </li> <li> <p> <code>LocaleId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Modality</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Channel</code> – <code>EQ</code>.</p> </li> <li> <p> <code>SessionId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>OriginatingRequestId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>IntentName</code> – <code>EQ</code>, <code>CO</code>.</p> </li> <li> <p> <code>IntentStageName</code> – <code>EQ</code>, <code>CO</code>.</p> </li> </ul>"""
    values: "aws_sdk_lex_models_v2.types.analytics_filter_values.AnalyticsFilterValues"
    """<p>An array containing the values of the category by which to apply the operator to filter the results. You can provide multiple values if the operator is <code>EQ</code> or <code>CO</code>. If you provide multiple values, you filter for results that equal/contain any of the values. For example, if the <code>name</code>, <code>operator</code>, and <code>values</code> fields are <code>Modality</code>, <code>EQ</code>, and <code>[Speech, Text]</code>, the operation filters for results where the modality was either <code>Speech</code> or <code>Text</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentStageFilter) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_intent_stage_filter_name

    out["name"] = (
        aws_sdk_lex_models_v2.types.analytics_intent_stage_filter_name.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_lex_models_v2.types.analytics_filter_operator

    out["operator"] = (
        aws_sdk_lex_models_v2.types.analytics_filter_operator.serialize_json(
            value["operator"]
        )
    )
    import aws_sdk_lex_models_v2.types.analytics_filter_values

    out["values"] = aws_sdk_lex_models_v2.types.analytics_filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsIntentStageFilter:
    out: AnalyticsIntentStageFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_stage_filter_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_stage_filter_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("AnalyticsIntentStageFilter.name required")
    if "operator" in data:
        import aws_sdk_lex_models_v2.types.analytics_filter_operator

        out["operator"] = (
            aws_sdk_lex_models_v2.types.analytics_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("AnalyticsIntentStageFilter.operator required")
    if "values" in data:
        import aws_sdk_lex_models_v2.types.analytics_filter_values

        out["values"] = (
            aws_sdk_lex_models_v2.types.analytics_filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("AnalyticsIntentStageFilter.values required")
    return out
