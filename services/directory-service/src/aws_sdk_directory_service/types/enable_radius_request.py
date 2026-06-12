"""Generated from Smithy shape ``com.amazonaws.directoryservice#EnableRadiusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.radius_settings


class EnableRadiusRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to enable MFA.</p>"""
    radius_settings: "aws_sdk_directory_service.types.radius_settings.RadiusSettings"
    """<p>A <a>RadiusSettings</a> object that contains information about the RADIUS server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableRadiusRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import aws_sdk_directory_service.types.radius_settings

    out["RadiusSettings"] = (
        aws_sdk_directory_service.types.radius_settings.serialize_aws_json_1_1(
            value["radius_settings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableRadiusRequest:
    out: EnableRadiusRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("EnableRadiusRequest.directory_id required")
    if "RadiusSettings" in data:
        import aws_sdk_directory_service.types.radius_settings

        out["radius_settings"] = (
            aws_sdk_directory_service.types.radius_settings.deserialize_aws_json_1_1(
                data["RadiusSettings"]
            )
        )
    else:
        raise DeserializationError("EnableRadiusRequest.radius_settings required")
    return out
