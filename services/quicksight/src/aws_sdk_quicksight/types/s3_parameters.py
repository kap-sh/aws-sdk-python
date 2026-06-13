"""Generated from Smithy shape ``com.amazonaws.quicksight#S3Parameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.manifest_file_location
    import aws_sdk_quicksight.types.role_arn


class S3Parameters(TypedDict):
    manifest_file_location: (
        "aws_sdk_quicksight.types.manifest_file_location.ManifestFileLocation"
    )
    """<p>Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded into Quick Sight.</p>"""
    role_arn: NotRequired["aws_sdk_quicksight.types.role_arn.RoleArn"]
    """<p>Use the <code>RoleArn</code> structure to override an account-wide role for a specific S3 data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use <code>RoleArn</code> to bypass the account-wide role and allow S3 access for the single S3 data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Parameters) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.manifest_file_location

    out["ManifestFileLocation"] = (
        aws_sdk_quicksight.types.manifest_file_location.serialize_json(
            value["manifest_file_location"]
        )
    )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> S3Parameters:
    out: S3Parameters = {}  # type: ignore[typeddict-item]
    if "ManifestFileLocation" in data:
        import aws_sdk_quicksight.types.manifest_file_location

        out["manifest_file_location"] = (
            aws_sdk_quicksight.types.manifest_file_location.deserialize_json(
                data["ManifestFileLocation"]
            )
        )
    else:
        raise DeserializationError("S3Parameters.manifest_file_location required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
