"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.domain
    import aws_sdk_personalize.types.kms_key_arn
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.role_arn
    import aws_sdk_personalize.types.tags


class CreateDatasetGroupRequest(TypedDict):
    name: "aws_sdk_personalize.types.name.Name"
    """<p>The name for the new dataset group.</p>"""
    role_arn: NotRequired["aws_sdk_personalize.types.role_arn.RoleArn"]
    """<p>The ARN of the Identity and Access Management (IAM) role that has permissions to access the Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</p>"""
    kms_key_arn: NotRequired["aws_sdk_personalize.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of a Key Management Service (KMS) key used to encrypt the datasets.</p>"""
    domain: NotRequired["aws_sdk_personalize.types.domain.Domain"]
    """<p>The domain of the dataset group. Specify a domain to create a Domain dataset group. The domain you specify determines the default schemas for datasets and the use cases available for recommenders. If you don't specify a domain, you create a Custom dataset group with solution versions that you deploy with a campaign. </p>"""
    tags: NotRequired["aws_sdk_personalize.types.tags.Tags"]
    r"""<p>A list of <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html\">tags</a> to apply to the dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetGroupRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "domain" in value:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    if "tags" in value:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetGroupRequest:
    out: CreateDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDatasetGroupRequest.name required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "domain" in data:
        import aws_sdk_personalize.types.domain

        out["domain"] = aws_sdk_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    if "tags" in data:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
