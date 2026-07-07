"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.app_registry_arn
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.ssm_sap_arn


class GetApplicationInput(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    application_arn: NotRequired["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the application. </p>"""
    app_registry_arn: NotRequired[
        "aws_sdk_ssm_sap.types.app_registry_arn.AppRegistryArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the application registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationInput) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "app_registry_arn" in value:
        out["AppRegistryArn"] = value["app_registry_arn"]
    return out


def deserialize_json(data: dict) -> GetApplicationInput:
    out: GetApplicationInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    if "AppRegistryArn" in data:
        out["app_registry_arn"] = data["AppRegistryArn"]
    return out
