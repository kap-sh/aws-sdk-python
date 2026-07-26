"""Generated from Smithy shape ``com.amazonaws.ec2#ResetEbsDefaultKmsKeyIdResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ResetEbsDefaultKmsKeyIdResult(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the default KMS key for EBS encryption by default.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResetEbsDefaultKmsKeyIdResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))


def deserialize_ec2_query(el: Element) -> ResetEbsDefaultKmsKeyIdResult:
    out: ResetEbsDefaultKmsKeyIdResult = {}  # type: ignore[typeddict-item]
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    return out
