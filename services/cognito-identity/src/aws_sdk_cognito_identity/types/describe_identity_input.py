"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DescribeIdentityInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_id


class DescribeIdentityInput(TypedDict):
    identity_id: "aws_sdk_cognito_identity.types.identity_id.IdentityId"
    """<p>A unique identifier in the format REGION:GUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIdentityInput) -> dict:
    out: dict = {}
    out["IdentityId"] = value["identity_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIdentityInput:
    out: DescribeIdentityInput = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    else:
        raise DeserializationError("DescribeIdentityInput.identity_id required")
    return out
