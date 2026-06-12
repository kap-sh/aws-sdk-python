"""Generated from Smithy shape ``com.amazonaws.acmpca#GetPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.arn


class GetPolicyRequest(TypedDict):
    resource_arn: "aws_sdk_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Number (ARN) of the private CA that will have its policy retrieved. You can find the CA's ARN by calling the ListCertificateAuthorities action. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPolicyRequest:
    out: GetPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetPolicyRequest.resource_arn required")
    return out
