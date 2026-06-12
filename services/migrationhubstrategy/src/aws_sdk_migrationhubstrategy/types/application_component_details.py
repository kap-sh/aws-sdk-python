"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationComponentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.application_component_detail

ApplicationComponentDetails: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.application_component_detail.ApplicationComponentDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationComponentDetails) -> list:
    import aws_sdk_migrationhubstrategy.types.application_component_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.application_component_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApplicationComponentDetails:
    import aws_sdk_migrationhubstrategy.types.application_component_detail

    out: ApplicationComponentDetails = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.application_component_detail.deserialize_json(
                item
            )
        )
    return out
