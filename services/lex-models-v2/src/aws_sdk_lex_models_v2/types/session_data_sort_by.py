"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SessionDataSortBy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_session_sort_by_name
    import aws_sdk_lex_models_v2.types.analytics_sort_order


class SessionDataSortBy(TypedDict):
    name: "aws_sdk_lex_models_v2.types.analytics_session_sort_by_name.AnalyticsSessionSortByName"
    """<p>The measure by which to sort the session analytics data.</p> <ul> <li> <p> <code>conversationStartTime</code> – The date and time when the conversation began. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p> </li> <li> <p> <code>numberOfTurns</code> – The number of turns that the session took.</p> </li> <li> <p> <code>conversationDurationSeconds</code> – The duration of the conversation in seconds.</p> </li> </ul>"""
    order: "aws_sdk_lex_models_v2.types.analytics_sort_order.AnalyticsSortOrder"
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionDataSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.analytics_session_sort_by_name

    out["name"] = (
        aws_sdk_lex_models_v2.types.analytics_session_sort_by_name.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_lex_models_v2.types.analytics_sort_order

    out["order"] = aws_sdk_lex_models_v2.types.analytics_sort_order.serialize_json(
        value["order"]
    )
    return out


def deserialize_json(data: dict) -> SessionDataSortBy:
    out: SessionDataSortBy = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.analytics_session_sort_by_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.analytics_session_sort_by_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("SessionDataSortBy.name required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.analytics_sort_order

        out["order"] = (
            aws_sdk_lex_models_v2.types.analytics_sort_order.deserialize_json(
                data["order"]
            )
        )
    else:
        raise DeserializationError("SessionDataSortBy.order required")
    return out
