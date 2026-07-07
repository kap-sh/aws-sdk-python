"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIndexCapacityFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.capacity_bytes_range_filter
    import aws_sdk_quicksight.types.user_name_or_email_filter


class _UserIndexCapacityFilter_userNameOrEmail(TypedDict, closed=True):
    userNameOrEmail: (
        "aws_sdk_quicksight.types.user_name_or_email_filter.UserNameOrEmailFilter"
    )


class _UserIndexCapacityFilter_totalCapacityBytes(TypedDict, closed=True):
    totalCapacityBytes: (
        "aws_sdk_quicksight.types.capacity_bytes_range_filter.CapacityBytesRangeFilter"
    )


UserIndexCapacityFilter: TypeAlias = (
    _UserIndexCapacityFilter_userNameOrEmail
    | _UserIndexCapacityFilter_totalCapacityBytes
)


# --- restJson1 ser/de ---
def serialize_json(value: UserIndexCapacityFilter) -> dict:
    if "userNameOrEmail" in value:
        import aws_sdk_quicksight.types.user_name_or_email_filter

        return {
            "userNameOrEmail": aws_sdk_quicksight.types.user_name_or_email_filter.serialize_json(
                value["userNameOrEmail"]
            )
        }
    elif "totalCapacityBytes" in value:
        import aws_sdk_quicksight.types.capacity_bytes_range_filter

        return {
            "totalCapacityBytes": aws_sdk_quicksight.types.capacity_bytes_range_filter.serialize_json(
                value["totalCapacityBytes"]
            )
        }
    else:
        raise SerializationError("UserIndexCapacityFilter: no variant present")


def deserialize_json(data: dict) -> UserIndexCapacityFilter:
    if "userNameOrEmail" in data:
        import aws_sdk_quicksight.types.user_name_or_email_filter

        return {
            "userNameOrEmail": aws_sdk_quicksight.types.user_name_or_email_filter.deserialize_json(
                data["userNameOrEmail"]
            )
        }
    elif "totalCapacityBytes" in data:
        import aws_sdk_quicksight.types.capacity_bytes_range_filter

        return {
            "totalCapacityBytes": aws_sdk_quicksight.types.capacity_bytes_range_filter.deserialize_json(
                data["totalCapacityBytes"]
            )
        }
    else:
        raise DeserializationError("UserIndexCapacityFilter: no recognized variant key")
