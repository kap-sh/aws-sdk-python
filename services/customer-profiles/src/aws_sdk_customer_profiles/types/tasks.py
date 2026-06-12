"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Tasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.task

Tasks: TypeAlias = list["aws_sdk_customer_profiles.types.task.Task"]


# --- restJson1 ser/de ---
def serialize_json(value: Tasks) -> list:
    import aws_sdk_customer_profiles.types.task

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.task.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tasks:
    import aws_sdk_customer_profiles.types.task

    out: Tasks = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.task.deserialize_json(item))
    return out
