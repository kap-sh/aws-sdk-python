"""Generated from Smithy shape ``com.amazonaws.sagemaker#RetentionPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.retention_type


class RetentionPolicy(TypedDict, closed=True):
    home_efs_file_system: NotRequired[
        "aws_sdk_sagemaker.types.retention_type.RetentionType"
    ]
    """<p>The default is <code>Retain</code>, which specifies to keep the data stored on the Amazon EFS volume.</p> <p>Specify <code>Delete</code> to delete the data stored on the Amazon EFS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionPolicy) -> dict:
    out: dict = {}
    if "home_efs_file_system" in value:
        import aws_sdk_sagemaker.types.retention_type

        out["HomeEfsFileSystem"] = (
            aws_sdk_sagemaker.types.retention_type.serialize_aws_json_1_1(
                value["home_efs_file_system"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetentionPolicy:
    out: RetentionPolicy = {}  # type: ignore[typeddict-item]
    if "HomeEfsFileSystem" in data:
        import aws_sdk_sagemaker.types.retention_type

        out["home_efs_file_system"] = (
            aws_sdk_sagemaker.types.retention_type.deserialize_aws_json_1_1(
                data["HomeEfsFileSystem"]
            )
        )
    return out
