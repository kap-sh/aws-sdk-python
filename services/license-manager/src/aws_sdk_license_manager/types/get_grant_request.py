"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.string


class GetGrantRequest(TypedDict, closed=True):
    grant_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the grant.</p>"""
    version: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Grant version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGrantRequest) -> dict:
    out: dict = {}
    out["GrantArn"] = value["grant_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGrantRequest:
    out: GetGrantRequest = {}  # type: ignore[typeddict-item]
    if "GrantArn" in data:
        out["grant_arn"] = data["GrantArn"]
    else:
        raise DeserializationError("GetGrantRequest.grant_arn required")
    if "Version" in data:
        out["version"] = data["Version"]
    return out
