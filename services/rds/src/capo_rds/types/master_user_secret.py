"""Generated from Smithy shape ``com.amazonaws.rds#MasterUserSecret``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class MasterUserSecret(TypedDict, closed=True):
    secret_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secret.</p>"""
    secret_status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the secret.</p> <p>The possible status values include the following:</p> <ul> <li> <p> <code>creating</code> - The secret is being created.</p> </li> <li> <p> <code>active</code> - The secret is available for normal use and rotation.</p> </li> <li> <p> <code>rotating</code> - The secret is being rotated.</p> </li> <li> <p> <code>impaired</code> - The secret can be used to access database credentials, but it can't be rotated. A secret might have this status if, for example, permissions are changed so that RDS can no longer access either the secret or the KMS key for the secret.</p> <p>When a secret has this status, you can correct the condition that caused the status. Alternatively, modify the DB instance to turn off automatic management of database credentials, and then modify the DB instance again to turn on automatic management of database credentials.</p> </li> </ul>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier that is used to encrypt the secret.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MasterUserSecret, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "secret_arn" in value:
        pairs.append((f"{key_prefix}SecretArn", str(value["secret_arn"])))
    if "secret_status" in value:
        pairs.append((f"{key_prefix}SecretStatus", str(value["secret_status"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))


def deserialize_query(el: Element) -> MasterUserSecret:
    out: MasterUserSecret = {}  # type: ignore[typeddict-item]
    child_secret_arn = el.find("SecretArn")
    if child_secret_arn is not None:
        out["secret_arn"] = str(child_secret_arn.text or "")
    child_secret_status = el.find("SecretStatus")
    if child_secret_status is not None:
        out["secret_status"] = str(child_secret_status.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    return out
