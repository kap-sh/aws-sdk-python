"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfApplicationDependencySummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.application_dependency_summary

__listOfApplicationDependencySummary: TypeAlias = list[
    "aws_sdk_serverlessapplicationrepository.types.application_dependency_summary.ApplicationDependencySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfApplicationDependencySummary) -> list:
    import aws_sdk_serverlessapplicationrepository.types.application_dependency_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.application_dependency_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfApplicationDependencySummary:
    import aws_sdk_serverlessapplicationrepository.types.application_dependency_summary

    out: __listOfApplicationDependencySummary = []
    for item in data:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.application_dependency_summary.deserialize_json(
                item
            )
        )
    return out
