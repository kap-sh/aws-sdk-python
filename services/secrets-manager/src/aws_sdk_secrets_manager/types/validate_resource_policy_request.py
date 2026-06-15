"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ValidateResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.non_empty_resource_policy_type
    import aws_sdk_secrets_manager.types.secret_id_type


class ValidateResourcePolicyRequest(TypedDict):
    secret_id: NotRequired["aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"]
    """<p>The ARN or name of the secret with the resource-based policy you want to validate.</p>"""
    resource_policy: "aws_sdk_secrets_manager.types.non_empty_resource_policy_type.NonEmptyResourcePolicyType"
    r"""<p>A JSON-formatted string that contains an Amazon Web Services resource-based policy. The policy in the string identifies who can access or manage this secret and its versions. For example policies, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html\">Permissions policy examples</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidateResourcePolicyRequest) -> dict:
    out: dict = {}
    if "secret_id" in value:
        out["SecretId"] = value["secret_id"]
    out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidateResourcePolicyRequest:
    out: ValidateResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    else:
        raise DeserializationError(
            "ValidateResourcePolicyRequest.resource_policy required"
        )
    return out
