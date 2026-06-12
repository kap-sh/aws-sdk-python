"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateTestGridUrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_farm_arn
    import aws_sdk_device_farm.types.test_grid_url_expires_in_seconds_input


class CreateTestGridUrlRequest(TypedDict):
    project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>ARN (from <a>CreateTestGridProject</a> or <a>ListTestGridProjects</a>) to associate with the short-term URL. </p>"""
    expires_in_seconds: "aws_sdk_device_farm.types.test_grid_url_expires_in_seconds_input.TestGridUrlExpiresInSecondsInput"
    """<p>Lifetime, in seconds, of the URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTestGridUrlRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    out["expiresInSeconds"] = value["expires_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTestGridUrlRequest:
    out: CreateTestGridUrlRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("CreateTestGridUrlRequest.project_arn required")
    if "expiresInSeconds" in data:
        out["expires_in_seconds"] = data["expiresInSeconds"]
    else:
        raise DeserializationError(
            "CreateTestGridUrlRequest.expires_in_seconds required"
        )
    return out
