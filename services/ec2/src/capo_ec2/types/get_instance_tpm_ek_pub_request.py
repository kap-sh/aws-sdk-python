"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTpmEkPubRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ek_pub_key_format
    import capo_ec2.types.ek_pub_key_type
    import capo_ec2.types.instance_id


class GetInstanceTpmEkPubRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance for which to get the public endorsement key.</p>"""
    key_type: NotRequired["capo_ec2.types.ek_pub_key_type.EkPubKeyType"]
    """<p>The required public endorsement key type.</p>"""
    key_format: NotRequired["capo_ec2.types.ek_pub_key_format.EkPubKeyFormat"]
    """<p>The required public endorsement key format. Specify <code>der</code> for a DER-encoded public key that is compatible with OpenSSL. Specify <code>tpmt</code> for a TPM 2.0 format that is compatible with tpm2-tools. The returned key is base64 encoded.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specify this parameter to verify whether the request will succeed, without actually making the request. If the request will succeed, the response is <code>DryRunOperation</code>. Otherwise, the response is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetInstanceTpmEkPubRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "key_type" in value:
        import capo_ec2.types.ek_pub_key_type

        capo_ec2.types.ek_pub_key_type.serialize_ec2_query(
            value["key_type"], pairs, f"{prefix}.KeyType"
        )
    if "key_format" in value:
        import capo_ec2.types.ek_pub_key_format

        capo_ec2.types.ek_pub_key_format.serialize_ec2_query(
            value["key_format"], pairs, f"{prefix}.KeyFormat"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetInstanceTpmEkPubRequest:
    out: GetInstanceTpmEkPubRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_key_type = el.find("KeyType")
    if child_key_type is not None:
        import capo_ec2.types.ek_pub_key_type

        out["key_type"] = capo_ec2.types.ek_pub_key_type.deserialize_ec2_query(
            child_key_type
        )
    child_key_format = el.find("KeyFormat")
    if child_key_format is not None:
        import capo_ec2.types.ek_pub_key_format

        out["key_format"] = capo_ec2.types.ek_pub_key_format.deserialize_ec2_query(
            child_key_format
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
