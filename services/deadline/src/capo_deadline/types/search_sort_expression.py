"""Generated from Smithy shape ``com.amazonaws.deadline#SearchSortExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_deadline.types.field_sort_expression
    import capo_deadline.types.parameter_sort_expression
    import capo_deadline.types.user_jobs_first


class _SearchSortExpression_userJobsFirst(TypedDict, closed=True):
    userJobsFirst: "capo_deadline.types.user_jobs_first.UserJobsFirst"


class _SearchSortExpression_fieldSort(TypedDict, closed=True):
    fieldSort: "capo_deadline.types.field_sort_expression.FieldSortExpression"


class _SearchSortExpression_parameterSort(TypedDict, closed=True):
    parameterSort: (
        "capo_deadline.types.parameter_sort_expression.ParameterSortExpression"
    )


SearchSortExpression: TypeAlias = (
    _SearchSortExpression_userJobsFirst
    | _SearchSortExpression_fieldSort
    | _SearchSortExpression_parameterSort
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchSortExpression) -> dict:
    if "userJobsFirst" in value:
        import capo_deadline.types.user_jobs_first

        return {
            "userJobsFirst": capo_deadline.types.user_jobs_first.serialize_json(
                value["userJobsFirst"]
            )
        }
    elif "fieldSort" in value:
        import capo_deadline.types.field_sort_expression

        return {
            "fieldSort": capo_deadline.types.field_sort_expression.serialize_json(
                value["fieldSort"]
            )
        }
    elif "parameterSort" in value:
        import capo_deadline.types.parameter_sort_expression

        return {
            "parameterSort": capo_deadline.types.parameter_sort_expression.serialize_json(
                value["parameterSort"]
            )
        }
    else:
        raise SerializationError("SearchSortExpression: no variant present")


def deserialize_json(data: dict) -> SearchSortExpression:
    if "userJobsFirst" in data:
        import capo_deadline.types.user_jobs_first

        return {
            "userJobsFirst": capo_deadline.types.user_jobs_first.deserialize_json(
                data["userJobsFirst"]
            )
        }
    elif "fieldSort" in data:
        import capo_deadline.types.field_sort_expression

        return {
            "fieldSort": capo_deadline.types.field_sort_expression.deserialize_json(
                data["fieldSort"]
            )
        }
    elif "parameterSort" in data:
        import capo_deadline.types.parameter_sort_expression

        return {
            "parameterSort": capo_deadline.types.parameter_sort_expression.deserialize_json(
                data["parameterSort"]
            )
        }
    else:
        raise DeserializationError("SearchSortExpression: no recognized variant key")
