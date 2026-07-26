"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.key_pair_id
    import capo_ec2.types.key_pair_name_with_resolver


class DeleteKeyPairRequest(TypedDict, closed=True):
    key_name: NotRequired[
        "capo_ec2.types.key_pair_name_with_resolver.KeyPairNameWithResolver"
    ]
    """<p>The name of the key pair.</p>"""
    key_pair_id: NotRequired["capo_ec2.types.key_pair_id.KeyPairId"]
    """<p>The ID of the key pair.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteKeyPairRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key_name" in value:
        pairs.append((f"{prefix}.KeyName", str(value["key_name"])))
    if "key_pair_id" in value:
        pairs.append((f"{prefix}.KeyPairId", str(value["key_pair_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteKeyPairRequest:
    out: DeleteKeyPairRequest = {}  # type: ignore[typeddict-item]
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_key_pair_id = el.find("KeyPairId")
    if child_key_pair_id is not None:
        out["key_pair_id"] = str(child_key_pair_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
