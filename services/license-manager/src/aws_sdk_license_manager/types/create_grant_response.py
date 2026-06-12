"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateGrantResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn
    import aws_sdk_license_manager.types.grant_status
    import aws_sdk_license_manager.types.string


class CreateGrantResponse(TypedDict):
    grant_arn: NotRequired["aws_sdk_license_manager.types.arn.Arn"]
    """<p>Grant ARN.</p>"""
    status: NotRequired["aws_sdk_license_manager.types.grant_status.GrantStatus"]
    """<p>Grant status.</p>"""
    version: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Grant version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGrantResponse) -> dict:
    out: dict = {}
    if "grant_arn" in value:
        out["GrantArn"] = value["grant_arn"]
    if "status" in value:
        import aws_sdk_license_manager.types.grant_status

        out["Status"] = (
            aws_sdk_license_manager.types.grant_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrantResponse:
    out: CreateGrantResponse = {}  # type: ignore[typeddict-item]
    if "GrantArn" in data:
        out["grant_arn"] = data["GrantArn"]
    if "Status" in data:
        import aws_sdk_license_manager.types.grant_status

        out["status"] = (
            aws_sdk_license_manager.types.grant_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    return out
