"""Generated from Smithy shape ``com.amazonaws.deadline#SearchFilterExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_deadline.types.date_time_filter_expression
    import capo_deadline.types.parameter_filter_expression
    import capo_deadline.types.search_grouped_filter_expressions
    import capo_deadline.types.search_term_filter_expression
    import capo_deadline.types.string_filter_expression
    import capo_deadline.types.string_list_filter_expression


class _SearchFilterExpression_dateTimeFilter(TypedDict, closed=True):
    dateTimeFilter: (
        "capo_deadline.types.date_time_filter_expression.DateTimeFilterExpression"
    )


class _SearchFilterExpression_parameterFilter(TypedDict, closed=True):
    parameterFilter: (
        "capo_deadline.types.parameter_filter_expression.ParameterFilterExpression"
    )


class _SearchFilterExpression_searchTermFilter(TypedDict, closed=True):
    searchTermFilter: (
        "capo_deadline.types.search_term_filter_expression.SearchTermFilterExpression"
    )


class _SearchFilterExpression_stringFilter(TypedDict, closed=True):
    stringFilter: "capo_deadline.types.string_filter_expression.StringFilterExpression"


class _SearchFilterExpression_stringListFilter(TypedDict, closed=True):
    stringListFilter: (
        "capo_deadline.types.string_list_filter_expression.StringListFilterExpression"
    )


class _SearchFilterExpression_groupFilter(TypedDict, closed=True):
    groupFilter: "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"


SearchFilterExpression: TypeAlias = (
    _SearchFilterExpression_dateTimeFilter
    | _SearchFilterExpression_parameterFilter
    | _SearchFilterExpression_searchTermFilter
    | _SearchFilterExpression_stringFilter
    | _SearchFilterExpression_stringListFilter
    | _SearchFilterExpression_groupFilter
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilterExpression) -> dict:
    if "dateTimeFilter" in value:
        import capo_deadline.types.date_time_filter_expression

        return {
            "dateTimeFilter": capo_deadline.types.date_time_filter_expression.serialize_json(
                value["dateTimeFilter"]
            )
        }
    elif "parameterFilter" in value:
        import capo_deadline.types.parameter_filter_expression

        return {
            "parameterFilter": capo_deadline.types.parameter_filter_expression.serialize_json(
                value["parameterFilter"]
            )
        }
    elif "searchTermFilter" in value:
        import capo_deadline.types.search_term_filter_expression

        return {
            "searchTermFilter": capo_deadline.types.search_term_filter_expression.serialize_json(
                value["searchTermFilter"]
            )
        }
    elif "stringFilter" in value:
        import capo_deadline.types.string_filter_expression

        return {
            "stringFilter": capo_deadline.types.string_filter_expression.serialize_json(
                value["stringFilter"]
            )
        }
    elif "stringListFilter" in value:
        import capo_deadline.types.string_list_filter_expression

        return {
            "stringListFilter": capo_deadline.types.string_list_filter_expression.serialize_json(
                value["stringListFilter"]
            )
        }
    elif "groupFilter" in value:
        import capo_deadline.types.search_grouped_filter_expressions

        return {
            "groupFilter": capo_deadline.types.search_grouped_filter_expressions.serialize_json(
                value["groupFilter"]
            )
        }
    else:
        raise SerializationError("SearchFilterExpression: no variant present")


def deserialize_json(data: dict) -> SearchFilterExpression:
    if "dateTimeFilter" in data:
        import capo_deadline.types.date_time_filter_expression

        return {
            "dateTimeFilter": capo_deadline.types.date_time_filter_expression.deserialize_json(
                data["dateTimeFilter"]
            )
        }
    elif "parameterFilter" in data:
        import capo_deadline.types.parameter_filter_expression

        return {
            "parameterFilter": capo_deadline.types.parameter_filter_expression.deserialize_json(
                data["parameterFilter"]
            )
        }
    elif "searchTermFilter" in data:
        import capo_deadline.types.search_term_filter_expression

        return {
            "searchTermFilter": capo_deadline.types.search_term_filter_expression.deserialize_json(
                data["searchTermFilter"]
            )
        }
    elif "stringFilter" in data:
        import capo_deadline.types.string_filter_expression

        return {
            "stringFilter": capo_deadline.types.string_filter_expression.deserialize_json(
                data["stringFilter"]
            )
        }
    elif "stringListFilter" in data:
        import capo_deadline.types.string_list_filter_expression

        return {
            "stringListFilter": capo_deadline.types.string_list_filter_expression.deserialize_json(
                data["stringListFilter"]
            )
        }
    elif "groupFilter" in data:
        import capo_deadline.types.search_grouped_filter_expressions

        return {
            "groupFilter": capo_deadline.types.search_grouped_filter_expressions.deserialize_json(
                data["groupFilter"]
            )
        }
    else:
        raise DeserializationError("SearchFilterExpression: no recognized variant key")
