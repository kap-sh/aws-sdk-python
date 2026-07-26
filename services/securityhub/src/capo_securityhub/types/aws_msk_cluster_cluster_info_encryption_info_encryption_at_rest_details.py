"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails(
    TypedDict, closed=True
):
    data_volume_kms_key_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails,
) -> dict:
    out: dict = {}
    if "data_volume_kms_key_id" in value:
        out["DataVolumeKMSKeyId"] = value["data_volume_kms_key_id"]
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails:
    out: AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails = {}  # type: ignore[typeddict-item]
    if "DataVolumeKMSKeyId" in data:
        out["data_volume_kms_key_id"] = data["DataVolumeKMSKeyId"]
    return out
