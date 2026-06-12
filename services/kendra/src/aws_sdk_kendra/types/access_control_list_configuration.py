"""Generated from Smithy shape ``com.amazonaws.kendra#AccessControlListConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.s3_object_key


class AccessControlListConfiguration(TypedDict):
    key_path: NotRequired["aws_sdk_kendra.types.s3_object_key.S3ObjectKey"]
    """<p>Path to the Amazon S3 bucket that contains the ACL files.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlListConfiguration) -> dict:
    out: dict = {}
    if "key_path" in value:
        out["KeyPath"] = value["key_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessControlListConfiguration:
    out: AccessControlListConfiguration = {}  # type: ignore[typeddict-item]
    if "KeyPath" in data:
        out["key_path"] = data["KeyPath"]
    return out
