"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizedTargetsByServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.authorized_targets_by_service

AuthorizedTargetsByServices: TypeAlias = list[
    "aws_sdk_quicksight.types.authorized_targets_by_service.AuthorizedTargetsByService"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedTargetsByServices) -> list:
    import aws_sdk_quicksight.types.authorized_targets_by_service

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.authorized_targets_by_service.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AuthorizedTargetsByServices:
    import aws_sdk_quicksight.types.authorized_targets_by_service

    out: AuthorizedTargetsByServices = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.authorized_targets_by_service.deserialize_json(
                item
            )
        )
    return out
