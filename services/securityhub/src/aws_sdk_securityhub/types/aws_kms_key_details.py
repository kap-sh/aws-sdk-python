"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsKmsKeyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.double
    import aws_sdk_securityhub.types.non_empty_string


class AwsKmsKeyDetails(TypedDict, closed=True):
    aws_account_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The twelve-digit account ID of the Amazon Web Services account that owns the KMS key.</p>"""
    creation_date: NotRequired["aws_sdk_securityhub.types.double.Double"]
    r"""<p>Indicates when the KMS key was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The globally unique identifier for the KMS key.</p>"""
    key_manager: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The manager of the KMS key. KMS keys in your Amazon Web Services account are either customer managed or Amazon Web Services managed.</p>"""
    key_state: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The state of the KMS key. Valid values are as follows:</p> <ul> <li> <p> <code>Disabled</code> </p> </li> <li> <p> <code>Enabled</code> </p> </li> <li> <p> <code>PendingDeletion</code> </p> </li> <li> <p> <code>PendingImport</code> </p> </li> <li> <p> <code>Unavailable</code> </p> </li> </ul>"""
    origin: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source of the KMS key material.</p> <p>When this value is <code>AWS_KMS</code>, KMS created the key material.</p> <p>When this value is <code>EXTERNAL</code>, the key material was imported from your existing key management infrastructure or the KMS key lacks key material.</p> <p>When this value is <code>AWS_CLOUDHSM</code>, the key material was created in the CloudHSM cluster associated with a custom key store.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the KMS key.</p>"""
    key_rotation_status: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the key has key rotation enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsKmsKeyDetails) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AWSAccountId"] = value["aws_account_id"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_manager" in value:
        out["KeyManager"] = value["key_manager"]
    if "key_state" in value:
        out["KeyState"] = value["key_state"]
    if "origin" in value:
        out["Origin"] = value["origin"]
    if "description" in value:
        out["Description"] = value["description"]
    if "key_rotation_status" in value:
        out["KeyRotationStatus"] = value["key_rotation_status"]
    return out


def deserialize_json(data: dict) -> AwsKmsKeyDetails:
    out: AwsKmsKeyDetails = {}  # type: ignore[typeddict-item]
    if "AWSAccountId" in data:
        out["aws_account_id"] = data["AWSAccountId"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "KeyManager" in data:
        out["key_manager"] = data["KeyManager"]
    if "KeyState" in data:
        out["key_state"] = data["KeyState"]
    if "Origin" in data:
        out["origin"] = data["Origin"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "KeyRotationStatus" in data:
        out["key_rotation_status"] = data["KeyRotationStatus"]
    return out
