"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTpmEkPubResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ek_pub_key_format
    import capo_ec2.types.ek_pub_key_type
    import capo_ec2.types.ek_pub_key_value
    import capo_ec2.types.instance_id


class GetInstanceTpmEkPubResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    key_type: NotRequired["capo_ec2.types.ek_pub_key_type.EkPubKeyType"]
    """<p>The public endorsement key type.</p>"""
    key_format: NotRequired["capo_ec2.types.ek_pub_key_format.EkPubKeyFormat"]
    """<p>The public endorsement key format.</p>"""
    key_value: NotRequired["capo_ec2.types.ek_pub_key_value.EkPubKeyValue"]
    """<p>The public endorsement key material.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetInstanceTpmEkPubResult, pairs: list[tuple[str, str]], prefix: str
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
    if "key_value" in value:
        pairs.append((f"{prefix}.KeyValue", str(value["key_value"])))


def deserialize_ec2_query(el: Element) -> GetInstanceTpmEkPubResult:
    out: GetInstanceTpmEkPubResult = {}  # type: ignore[typeddict-item]
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
    child_key_value = el.find("KeyValue")
    if child_key_value is not None:
        out["key_value"] = str(child_key_value.text or "")
    return out
