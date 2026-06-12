"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportPreferences``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_application_discovery_service.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.ec2_recommendations_export_preferences


class _ExportPreferences_ec2RecommendationsPreferences(TypedDict):
    ec2RecommendationsPreferences: "aws_sdk_application_discovery_service.types.ec2_recommendations_export_preferences.Ec2RecommendationsExportPreferences"


ExportPreferences: TypeAlias = _ExportPreferences_ec2RecommendationsPreferences


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportPreferences) -> dict:
    if "ec2RecommendationsPreferences" in value:
        import aws_sdk_application_discovery_service.types.ec2_recommendations_export_preferences

        return {
            "ec2RecommendationsPreferences": aws_sdk_application_discovery_service.types.ec2_recommendations_export_preferences.serialize_aws_json_1_1(
                value["ec2RecommendationsPreferences"]
            )
        }
    else:
        raise SerializationError("ExportPreferences: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ExportPreferences:
    if "ec2RecommendationsPreferences" in data:
        import aws_sdk_application_discovery_service.types.ec2_recommendations_export_preferences

        return {
            "ec2RecommendationsPreferences": aws_sdk_application_discovery_service.types.ec2_recommendations_export_preferences.deserialize_aws_json_1_1(
                data["ec2RecommendationsPreferences"]
            )
        }
    else:
        raise DeserializationError("ExportPreferences: no recognized variant key")
