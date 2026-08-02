"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyEbsDefaultKmsKeyIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.kms_key_id


class ModifyEbsDefaultKmsKeyIdRequest(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Amazon EBS is used. If <code>KmsKeyId</code> is specified, the encrypted state must be <code>true</code>.</p> <p>You can specify the KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyEbsDefaultKmsKeyIdRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyEbsDefaultKmsKeyIdRequest:
    out: ModifyEbsDefaultKmsKeyIdRequest = {}  # type: ignore[typeddict-item]
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
