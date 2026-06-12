"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationVersionChangeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_version_id


class ApplicationVersionChangeDetails(TypedDict):
    application_version_updated_from: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The new version that the application was updated to.</p>"""
    application_version_updated_to: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The version that the operation execution applied to the applicartion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationVersionChangeDetails) -> dict:
    out: dict = {}
    out["ApplicationVersionUpdatedFrom"] = value["application_version_updated_from"]
    out["ApplicationVersionUpdatedTo"] = value["application_version_updated_to"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationVersionChangeDetails:
    out: ApplicationVersionChangeDetails = {}  # type: ignore[typeddict-item]
    if "ApplicationVersionUpdatedFrom" in data:
        out["application_version_updated_from"] = data["ApplicationVersionUpdatedFrom"]
    else:
        raise DeserializationError(
            "ApplicationVersionChangeDetails.application_version_updated_from required"
        )
    if "ApplicationVersionUpdatedTo" in data:
        out["application_version_updated_to"] = data["ApplicationVersionUpdatedTo"]
    else:
        raise DeserializationError(
            "ApplicationVersionChangeDetails.application_version_updated_to required"
        )
    return out
