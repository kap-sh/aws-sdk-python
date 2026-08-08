"""Generated from Smithy shape ``com.amazonaws.ec2#ImportKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.blob
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class ImportKeyPairRequest(TypedDict, closed=True):
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the imported key pair.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    key_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique name for the key pair.</p>"""
    public_key_material: NotRequired["capo_ec2.types.blob.Blob"]
    """<p>The public key.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportKeyPairRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "public_key_material" in value:
        import capo_ec2.types.blob

        capo_ec2.types.blob.serialize_ec2_query(
            value["public_key_material"], pairs, f"{key_prefix}PublicKeyMaterial"
        )


def deserialize_ec2_query(el: Element) -> ImportKeyPairRequest:
    out: ImportKeyPairRequest = {}  # type: ignore[typeddict-item]
    if el.find("TagSpecification") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecification"
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_key_name = el.find("keyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_public_key_material = el.find("publicKeyMaterial")
    if child_public_key_material is not None:
        import capo_ec2.types.blob

        out["public_key_material"] = capo_ec2.types.blob.deserialize_ec2_query(
            child_public_key_material
        )
    return out
