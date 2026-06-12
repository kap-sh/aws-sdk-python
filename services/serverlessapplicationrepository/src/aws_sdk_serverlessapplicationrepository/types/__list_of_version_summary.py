"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfVersionSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.version_summary

__listOfVersionSummary: TypeAlias = list[
    "aws_sdk_serverlessapplicationrepository.types.version_summary.VersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVersionSummary) -> list:
    import aws_sdk_serverlessapplicationrepository.types.version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfVersionSummary:
    import aws_sdk_serverlessapplicationrepository.types.version_summary

    out: __listOfVersionSummary = []
    for item in data:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.version_summary.deserialize_json(
                item
            )
        )
    return out
