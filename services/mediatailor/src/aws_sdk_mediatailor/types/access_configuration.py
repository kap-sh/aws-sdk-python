"""Generated from Smithy shape ``com.amazonaws.mediatailor#AccessConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.access_type
    import aws_sdk_mediatailor.types.secrets_manager_access_token_configuration


class AccessConfiguration(TypedDict):
    access_type: NotRequired["aws_sdk_mediatailor.types.access_type.AccessType"]
    r"""<p>The type of authentication used to access content from <code>HttpConfiguration::BaseUrl</code> on your source location.</p> <p> <code>S3_SIGV4</code> - AWS Signature Version 4 authentication for Amazon S3 hosted virtual-style access. If your source location base URL is an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the bucket where your source content is stored. Your MediaTailor source location baseURL must follow the S3 virtual hosted-style request URL format. For example, https://bucket-name.s3.Region.amazonaws.com/key-name.</p> <p>Before you can use <code>S3_SIGV4</code>, you must meet these requirements:</p> <p>• You must allow MediaTailor to access your S3 bucket by granting mediatailor.amazonaws.com principal access in IAM. For information about configuring access in IAM, see Access management in the IAM User Guide.</p> <p>• The mediatailor.amazonaws.com service principal must have permissions to read all top level manifests referenced by the VodSource packaging configurations.</p> <p>• The caller of the API must have s3:GetObject IAM permissions to read all top level manifests referenced by your MediaTailor VodSource packaging configurations.</p> <p> <code>AUTODETECT_SIGV4</code> - AWS Signature Version 4 authentication for a set of supported services: MediaPackage Version 2 and Amazon S3 hosted virtual-style access. If your source location base URL is a MediaPackage Version 2 endpoint or an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the resource where your source content is stored.</p> <p>Before you can use <code>AUTODETECT_SIGV4</code> with a MediaPackage Version 2 endpoint, you must meet these requirements:</p> <p>• You must grant MediaTailor access to your MediaPackage endpoint by granting <code>mediatailor.amazonaws.com</code> principal access in an Origin Access policy on the endpoint.</p> <p>• Your MediaTailor source location base URL must be a MediaPackage V2 endpoint.</p> <p>• The caller of the API must have <code>mediapackagev2:GetObject</code> IAM permissions to read all top level manifests referenced by the MediaTailor source packaging configurations.</p> <p>Before you can use <code>AUTODETECT_SIGV4</code> with an Amazon S3 bucket, you must meet these requirements:</p> <p>• You must grant MediaTailor access to your S3 bucket by granting <code>mediatailor.amazonaws.com</code> principal access in IAM. For more information about configuring access in IAM, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html\">Access management</a> in the <i>IAM User Guide.</i>.</p> <p>• The <code>mediatailor.amazonaws.com</code> service principal must have permissions to read all top-level manifests referenced by the <code>VodSource</code> packaging configurations.</p> <p>• The caller of the API must have <code>s3:GetObject</code> IAM permissions to read all top level manifests referenced by your MediaTailor <code>VodSource</code> packaging configurations.</p>"""
    secrets_manager_access_token_configuration: NotRequired[
        "aws_sdk_mediatailor.types.secrets_manager_access_token_configuration.SecretsManagerAccessTokenConfiguration"
    ]
    """<p>AWS Secrets Manager access token configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessConfiguration) -> dict:
    out: dict = {}
    if "access_type" in value:
        import aws_sdk_mediatailor.types.access_type

        out["AccessType"] = aws_sdk_mediatailor.types.access_type.serialize_json(
            value["access_type"]
        )
    if "secrets_manager_access_token_configuration" in value:
        import aws_sdk_mediatailor.types.secrets_manager_access_token_configuration

        out["SecretsManagerAccessTokenConfiguration"] = (
            aws_sdk_mediatailor.types.secrets_manager_access_token_configuration.serialize_json(
                value["secrets_manager_access_token_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessConfiguration:
    out: AccessConfiguration = {}  # type: ignore[typeddict-item]
    if "AccessType" in data:
        import aws_sdk_mediatailor.types.access_type

        out["access_type"] = aws_sdk_mediatailor.types.access_type.deserialize_json(
            data["AccessType"]
        )
    if "SecretsManagerAccessTokenConfiguration" in data:
        import aws_sdk_mediatailor.types.secrets_manager_access_token_configuration

        out["secrets_manager_access_token_configuration"] = (
            aws_sdk_mediatailor.types.secrets_manager_access_token_configuration.deserialize_json(
                data["SecretsManagerAccessTokenConfiguration"]
            )
        )
    return out
