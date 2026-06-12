"""Generated from Smithy shape ``com.amazonaws.qbusiness#BasicAuthConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.secret_arn

class BasicAuthConfiguration(TypedDict):
    secret_arn: "aws_sdk_qbusiness.types.secret_arn.SecretArn"
    """<p>The ARN of the Secrets Manager secret that stores the basic authentication credentials used for plugin configuration..</p>"""
    role_arn: "aws_sdk_qbusiness.types.role_arn.RoleArn"
    """<p>The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BasicAuthConfiguration) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> BasicAuthConfiguration:
    out: BasicAuthConfiguration = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("BasicAuthConfiguration.secret_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("BasicAuthConfiguration.role_arn required")
    return out