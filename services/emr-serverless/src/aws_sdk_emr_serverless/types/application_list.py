"""Generated from Smithy shape ``com.amazonaws.emrserverless#ApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_summary

ApplicationList: TypeAlias = list[
    "aws_sdk_emr_serverless.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationList) -> list:
    import aws_sdk_emr_serverless.types.application_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr_serverless.types.application_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ApplicationList:
    import aws_sdk_emr_serverless.types.application_summary

    out: ApplicationList = []
    for item in data:
        out.append(
            aws_sdk_emr_serverless.types.application_summary.deserialize_json(item)
        )
    return out
