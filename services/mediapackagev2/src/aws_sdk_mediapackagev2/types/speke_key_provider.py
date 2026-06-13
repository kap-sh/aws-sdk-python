"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#SpekeKeyProvider``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.drm_systems
    import aws_sdk_mediapackagev2.types.encryption_contract_configuration


class SpekeKeyProvider(TypedDict):
    encryption_contract_configuration: "aws_sdk_mediapackagev2.types.encryption_contract_configuration.EncryptionContractConfiguration"
    """<p>Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.</p>"""
    resource_id: "str"
    """<p>The unique identifier for the content. The service sends this to the key server to identify the current endpoint. How unique you make this depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.</p> <p>The following example shows a resource ID: <code>MovieNight20171126093045</code> </p>"""
    drm_systems: "aws_sdk_mediapackagev2.types.drm_systems.DrmSystems"
    """<p>The DRM solution provider you're using to protect your content during distribution.</p>"""
    role_arn: "str"
    """<p>The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.</p> <p>Valid format: <code>arn:aws:iam::{accountID}:role/{name}</code>. The following example shows a role ARN: <code>arn:aws:iam::444455556666:role/SpekeAccess</code> </p>"""
    url: "str"
    """<p>The URL of the API Gateway proxy that you set up to talk to your key server. The API Gateway proxy must reside in the same AWS Region as MediaPackage and must start with https://.</p> <p>The following example shows a URL: <code>https://1wm2dx1f33.execute-api.us-west-2.amazonaws.com/SpekeSample/copyProtection</code> </p>"""
    certificate_arn: NotRequired["str"]
    """<p>The ARN for the certificate that you imported to Amazon Web Services Certificate Manager to add content key encryption to this endpoint. For this feature to work, your DRM key provider must support content key encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpekeKeyProvider) -> dict:
    out: dict = {}
    import aws_sdk_mediapackagev2.types.encryption_contract_configuration

    out["EncryptionContractConfiguration"] = (
        aws_sdk_mediapackagev2.types.encryption_contract_configuration.serialize_json(
            value["encryption_contract_configuration"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_mediapackagev2.types.drm_systems

    out["DrmSystems"] = aws_sdk_mediapackagev2.types.drm_systems.serialize_json(
        value["drm_systems"]
    )
    out["RoleArn"] = value["role_arn"]
    out["Url"] = value["url"]
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_json(data: dict) -> SpekeKeyProvider:
    out: SpekeKeyProvider = {}  # type: ignore[typeddict-item]
    if "EncryptionContractConfiguration" in data:
        import aws_sdk_mediapackagev2.types.encryption_contract_configuration

        out["encryption_contract_configuration"] = (
            aws_sdk_mediapackagev2.types.encryption_contract_configuration.deserialize_json(
                data["EncryptionContractConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SpekeKeyProvider.encryption_contract_configuration required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("SpekeKeyProvider.resource_id required")
    if "DrmSystems" in data:
        import aws_sdk_mediapackagev2.types.drm_systems

        out["drm_systems"] = aws_sdk_mediapackagev2.types.drm_systems.deserialize_json(
            data["DrmSystems"]
        )
    else:
        raise DeserializationError("SpekeKeyProvider.drm_systems required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("SpekeKeyProvider.role_arn required")
    if "Url" in data:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("SpekeKeyProvider.url required")
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    return out
