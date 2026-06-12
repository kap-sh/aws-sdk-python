"""Generated from Smithy shape ``com.amazonaws.deadline#SearchSortExpression``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.field_sort_expression
    import aws_sdk_deadline.types.parameter_sort_expression
    import aws_sdk_deadline.types.user_jobs_first


class _SearchSortExpression_userJobsFirst(TypedDict):
    userJobsFirst: "aws_sdk_deadline.types.user_jobs_first.UserJobsFirst"


class _SearchSortExpression_fieldSort(TypedDict):
    fieldSort: "aws_sdk_deadline.types.field_sort_expression.FieldSortExpression"


class _SearchSortExpression_parameterSort(TypedDict):
    parameterSort: (
        "aws_sdk_deadline.types.parameter_sort_expression.ParameterSortExpression"
    )


SearchSortExpression: TypeAlias = (
    _SearchSortExpression_userJobsFirst
    | _SearchSortExpression_fieldSort
    | _SearchSortExpression_parameterSort
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchSortExpression) -> dict:
    if "userJobsFirst" in value:
        import aws_sdk_deadline.types.user_jobs_first

        return {
            "userJobsFirst": aws_sdk_deadline.types.user_jobs_first.serialize_json(
                value["userJobsFirst"]
            )
        }
    elif "fieldSort" in value:
        import aws_sdk_deadline.types.field_sort_expression

        return {
            "fieldSort": aws_sdk_deadline.types.field_sort_expression.serialize_json(
                value["fieldSort"]
            )
        }
    elif "parameterSort" in value:
        import aws_sdk_deadline.types.parameter_sort_expression

        return {
            "parameterSort": aws_sdk_deadline.types.parameter_sort_expression.serialize_json(
                value["parameterSort"]
            )
        }
    else:
        raise SerializationError("SearchSortExpression: no variant present")


def deserialize_json(data: dict) -> SearchSortExpression:
    if "userJobsFirst" in data:
        import aws_sdk_deadline.types.user_jobs_first

        return {
            "userJobsFirst": aws_sdk_deadline.types.user_jobs_first.deserialize_json(
                data["userJobsFirst"]
            )
        }
    elif "fieldSort" in data:
        import aws_sdk_deadline.types.field_sort_expression

        return {
            "fieldSort": aws_sdk_deadline.types.field_sort_expression.deserialize_json(
                data["fieldSort"]
            )
        }
    elif "parameterSort" in data:
        import aws_sdk_deadline.types.parameter_sort_expression

        return {
            "parameterSort": aws_sdk_deadline.types.parameter_sort_expression.deserialize_json(
                data["parameterSort"]
            )
        }
    else:
        raise DeserializationError("SearchSortExpression: no recognized variant key")
