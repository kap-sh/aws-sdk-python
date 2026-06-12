"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AssociatedApplications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.associated_application

AssociatedApplications: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.associated_application.AssociatedApplication"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedApplications) -> list:
    import aws_sdk_migrationhubstrategy.types.associated_application

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.associated_application.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssociatedApplications:
    import aws_sdk_migrationhubstrategy.types.associated_application

    out: AssociatedApplications = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.associated_application.deserialize_json(
                item
            )
        )
    return out
