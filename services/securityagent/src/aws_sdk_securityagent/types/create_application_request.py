"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.default_kms_key_id
    import aws_sdk_securityagent.types.id_c_instance_arn
    import aws_sdk_securityagent.types.role_arn
    import aws_sdk_securityagent.types.tag_map


class CreateApplicationRequest(TypedDict, closed=True):
    idc_instance_arn: NotRequired[
        "aws_sdk_securityagent.types.id_c_instance_arn.IdCInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center instance to associate with the application.</p>"""
    role_arn: NotRequired["aws_sdk_securityagent.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the application.</p>"""
    default_kms_key_id: NotRequired[
        "aws_sdk_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
    ]
    """<p>The identifier of the default AWS KMS key to use for encrypting data in the application.</p>"""
    tags: NotRequired["aws_sdk_securityagent.types.tag_map.TagMap"]
    """<p>The tags to associate with the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "idc_instance_arn" in value:
        out["idcInstanceArn"] = value["idc_instance_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "default_kms_key_id" in value:
        out["defaultKmsKeyId"] = value["default_kms_key_id"]
    if "tags" in value:
        import aws_sdk_securityagent.types.tag_map

        out["tags"] = aws_sdk_securityagent.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "idcInstanceArn" in data:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "defaultKmsKeyId" in data:
        out["default_kms_key_id"] = data["defaultKmsKeyId"]
    if "tags" in data:
        import aws_sdk_securityagent.types.tag_map

        out["tags"] = aws_sdk_securityagent.types.tag_map.deserialize_json(data["tags"])
    return out
