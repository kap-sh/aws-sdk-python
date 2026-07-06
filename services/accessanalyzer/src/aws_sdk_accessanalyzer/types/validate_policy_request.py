"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ValidatePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.locale
    import aws_sdk_accessanalyzer.types.policy_document
    import aws_sdk_accessanalyzer.types.policy_type
    import aws_sdk_accessanalyzer.types.token
    import aws_sdk_accessanalyzer.types.validate_policy_resource_type


class ValidatePolicyRequest(TypedDict, closed=True):
    locale: NotRequired["aws_sdk_accessanalyzer.types.locale.Locale"]
    """<p>The locale to use for localizing the findings.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    policy_document: "aws_sdk_accessanalyzer.types.policy_document.PolicyDocument"
    """<p>The JSON policy document to use as the content for the policy.</p>"""
    policy_type: "aws_sdk_accessanalyzer.types.policy_type.PolicyType"
    """<p>The type of policy to validate. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.</p> <p>Resource policies grant permissions on Amazon Web Services resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy. </p> <p>Service control policies (SCPs) are a type of organization policy attached to an Amazon Web Services organization, organizational unit (OU), or an account.</p>"""
    validate_policy_resource_type: NotRequired[
        "aws_sdk_accessanalyzer.types.validate_policy_resource_type.ValidatePolicyResourceType"
    ]
    """<p>The type of resource to attach to your resource policy. Specify a value for the policy validation resource type only if the policy type is <code>RESOURCE_POLICY</code>. For example, to validate a resource policy to attach to an Amazon S3 bucket, you can choose <code>AWS::S3::Bucket</code> for the policy validation resource type.</p> <p>For resource types not supported as valid values, IAM Access Analyzer runs policy checks that apply to all resource policies. For example, to validate a resource policy to attach to a KMS key, do not specify a value for the policy validation resource type and IAM Access Analyzer will run policy checks that apply to all resource policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidatePolicyRequest) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["policyDocument"] = value["policy_document"]
    out["policyType"] = value["policy_type"]
    if "validate_policy_resource_type" in value:
        out["validatePolicyResourceType"] = value["validate_policy_resource_type"]
    return out


def deserialize_json(data: dict) -> ValidatePolicyRequest:
    out: ValidatePolicyRequest = {}  # type: ignore[typeddict-item]
    if "locale" in data:
        out["locale"] = data["locale"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError("ValidatePolicyRequest.policy_document required")
    if "policyType" in data:
        out["policy_type"] = data["policyType"]
    else:
        raise DeserializationError("ValidatePolicyRequest.policy_type required")
    if "validatePolicyResourceType" in data:
        out["validate_policy_resource_type"] = data["validatePolicyResourceType"]
    return out
