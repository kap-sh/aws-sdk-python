"""Generated from Smithy shape ``com.amazonaws.workdocs#UserActivities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.activity

UserActivities: TypeAlias = list["aws_sdk_workdocs.types.activity.Activity"]


# --- restJson1 ser/de ---
def serialize_json(value: UserActivities) -> list:
    import aws_sdk_workdocs.types.activity

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.activity.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserActivities:
    import aws_sdk_workdocs.types.activity

    out: UserActivities = []
    for item in data:
        out.append(aws_sdk_workdocs.types.activity.deserialize_json(item))
    return out
