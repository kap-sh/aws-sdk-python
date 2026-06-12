"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_value
    import aws_sdk_connectcases.types.field_value
    import aws_sdk_connectcases.types.field_value
    import aws_sdk_connectcases.types.field_value
    import aws_sdk_connectcases.types.field_value
    import aws_sdk_connectcases.types.field_value


class _FieldFilter_equalTo(TypedDict):
    equalTo: "aws_sdk_connectcases.types.field_value.FieldValue"


class _FieldFilter_contains(TypedDict):
    contains: "aws_sdk_connectcases.types.field_value.FieldValue"


class _FieldFilter_greaterThan(TypedDict):
    greaterThan: "aws_sdk_connectcases.types.field_value.FieldValue"


class _FieldFilter_greaterThanOrEqualTo(TypedDict):
    greaterThanOrEqualTo: "aws_sdk_connectcases.types.field_value.FieldValue"


class _FieldFilter_lessThan(TypedDict):
    lessThan: "aws_sdk_connectcases.types.field_value.FieldValue"


class _FieldFilter_lessThanOrEqualTo(TypedDict):
    lessThanOrEqualTo: "aws_sdk_connectcases.types.field_value.FieldValue"


FieldFilter: TypeAlias = (
    _FieldFilter_equalTo
    | _FieldFilter_contains
    | _FieldFilter_greaterThan
    | _FieldFilter_greaterThanOrEqualTo
    | _FieldFilter_lessThan
    | _FieldFilter_lessThanOrEqualTo
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldFilter) -> dict:
    if "equalTo" in value:
        import aws_sdk_connectcases.types.field_value

        return {
            "equalTo": aws_sdk_connectcases.types.field_value.serialize_json(
                value["equalTo"]
            )
        }
    elif "contains" in value:
        import aws_sdk_connectcases.types.field_value

        return {
            "contains": aws_sdk_connectcases.types.field_value.serialize_json(
                value["contains"]
            )
        }
    elif "greaterThan" in value:
        import aws_sdk_connectcases.types.field_value

        return {
            "greaterThan": aws_sdk_connectcases.types.field_value.serialize_json(
                value["greaterThan"]
            )
        }
    elif "greaterThanOrEqualTo" in value:
        import aws_sdk_connectcases.types.field_value

        return {
            "greaterThanOrEqualTo": aws_sdk_connectcases.types.field_value.serialize_json(
                value["greaterThanOrEqualTo"]
            )
        }
    elif "lessThan" in value:
        import aws_sdk_connectcases.types.field_value

        return {
            "lessThan": aws_sdk_connectcases.types.field_value.serialize_json(
                value["lessThan"]
            )
        }
    elif "lessThanOrEqualTo" in value:
        import aws_sdk_connectcases.types.field_value

        return {
            "lessThanOrEqualTo": aws_sdk_connectcases.types.field_value.serialize_json(
                value["lessThanOrEqualTo"]
            )
        }
    else:
        raise SerializationError("FieldFilter: no variant present")


def deserialize_json(data: dict) -> FieldFilter:
    if "equalTo" in data:
        import aws_sdk_connectcases.types.field_value

        return {
            "equalTo": aws_sdk_connectcases.types.field_value.deserialize_json(
                data["equalTo"]
            )
        }
    elif "contains" in data:
        import aws_sdk_connectcases.types.field_value

        return {
            "contains": aws_sdk_connectcases.types.field_value.deserialize_json(
                data["contains"]
            )
        }
    elif "greaterThan" in data:
        import aws_sdk_connectcases.types.field_value

        return {
            "greaterThan": aws_sdk_connectcases.types.field_value.deserialize_json(
                data["greaterThan"]
            )
        }
    elif "greaterThanOrEqualTo" in data:
        import aws_sdk_connectcases.types.field_value

        return {
            "greaterThanOrEqualTo": aws_sdk_connectcases.types.field_value.deserialize_json(
                data["greaterThanOrEqualTo"]
            )
        }
    elif "lessThan" in data:
        import aws_sdk_connectcases.types.field_value

        return {
            "lessThan": aws_sdk_connectcases.types.field_value.deserialize_json(
                data["lessThan"]
            )
        }
    elif "lessThanOrEqualTo" in data:
        import aws_sdk_connectcases.types.field_value

        return {
            "lessThanOrEqualTo": aws_sdk_connectcases.types.field_value.deserialize_json(
                data["lessThanOrEqualTo"]
            )
        }
    else:
        raise DeserializationError("FieldFilter: no recognized variant key")
