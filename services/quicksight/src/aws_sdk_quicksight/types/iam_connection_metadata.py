"""Generated from Smithy shape ``com.amazonaws.quicksight#IAMConnectionMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.role_arn


class IAMConnectionMetadata(TypedDict):
    role_arn: "aws_sdk_quicksight.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to assume for authentication with Amazon Web Services services. This IAM role should be in the same account as Quick Sight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMConnectionMetadata) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IAMConnectionMetadata:
    out: IAMConnectionMetadata = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("IAMConnectionMetadata.role_arn required")
    return out
