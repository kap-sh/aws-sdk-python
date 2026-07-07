"""Generated from Smithy shape ``com.amazonaws.glue#SourceProcessingProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.string128


class SourceProcessingProperties(TypedDict, closed=True):
    role_arn: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>The IAM role to access the Glue connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceProcessingProperties) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceProcessingProperties:
    out: SourceProcessingProperties = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
