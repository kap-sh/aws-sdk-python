"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadIamConnectionMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.resource_arn
    import aws_sdk_quicksight.types.role_arn


class ReadIamConnectionMetadata(TypedDict):
    role_arn: "aws_sdk_quicksight.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to assume for authentication.</p>"""
    source_arn: "aws_sdk_quicksight.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the source resource for IAM authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadIamConnectionMetadata) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    out["SourceArn"] = value["source_arn"]
    return out


def deserialize_json(data: dict) -> ReadIamConnectionMetadata:
    out: ReadIamConnectionMetadata = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("ReadIamConnectionMetadata.role_arn required")
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    else:
        raise DeserializationError("ReadIamConnectionMetadata.source_arn required")
    return out
