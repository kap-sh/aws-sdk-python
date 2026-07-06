"""Generated from Smithy shape ``com.amazonaws.securityagent#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.application_domain
    import aws_sdk_securityagent.types.application_id
    import aws_sdk_securityagent.types.default_kms_key_id
    import aws_sdk_securityagent.types.id_c_configuration
    import aws_sdk_securityagent.types.role_arn


class GetApplicationResponse(TypedDict, closed=True):
    application_id: "aws_sdk_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application.</p>"""
    domain: "aws_sdk_securityagent.types.application_domain.ApplicationDomain"
    """<p>The domain associated with the application.</p>"""
    application_name: NotRequired["str"]
    """<p>The name of the application.</p>"""
    idc_configuration: NotRequired[
        "aws_sdk_securityagent.types.id_c_configuration.IdCConfiguration"
    ]
    """<p>The IAM Identity Center configuration for the application.</p>"""
    role_arn: NotRequired["aws_sdk_securityagent.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the application.</p>"""
    default_kms_key_id: NotRequired[
        "aws_sdk_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
    ]
    """<p>The identifier of the default AWS KMS key used to encrypt data for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["domain"] = value["domain"]
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "idc_configuration" in value:
        import aws_sdk_securityagent.types.id_c_configuration

        out["idcConfiguration"] = (
            aws_sdk_securityagent.types.id_c_configuration.serialize_json(
                value["idc_configuration"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "default_kms_key_id" in value:
        out["defaultKmsKeyId"] = value["default_kms_key_id"]
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("GetApplicationResponse.application_id required")
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("GetApplicationResponse.domain required")
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "idcConfiguration" in data:
        import aws_sdk_securityagent.types.id_c_configuration

        out["idc_configuration"] = (
            aws_sdk_securityagent.types.id_c_configuration.deserialize_json(
                data["idcConfiguration"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "defaultKmsKeyId" in data:
        out["default_kms_key_id"] = data["defaultKmsKeyId"]
    return out
