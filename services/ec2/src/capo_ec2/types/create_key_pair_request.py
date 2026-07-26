"""Generated from Smithy shape ``com.amazonaws.ec2#CreateKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.key_format
    import capo_ec2.types.key_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateKeyPairRequest(TypedDict, closed=True):
    key_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique name for the key pair.</p> <p>Constraints: Up to 255 ASCII characters</p>"""
    key_type: NotRequired["capo_ec2.types.key_type.KeyType"]
    """<p>The type of key pair. Note that ED25519 keys are not supported for Windows instances.</p> <p>Default: <code>rsa</code> </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new key pair.</p>"""
    key_format: NotRequired["capo_ec2.types.key_format.KeyFormat"]
    """<p>The format of the key pair.</p> <p>Default: <code>pem</code> </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateKeyPairRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key_name" in value:
        pairs.append((f"{prefix}.KeyName", str(value["key_name"])))
    if "key_type" in value:
        import capo_ec2.types.key_type

        capo_ec2.types.key_type.serialize_ec2_query(
            value["key_type"], pairs, f"{prefix}.KeyType"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "key_format" in value:
        import capo_ec2.types.key_format

        capo_ec2.types.key_format.serialize_ec2_query(
            value["key_format"], pairs, f"{prefix}.KeyFormat"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateKeyPairRequest:
    out: CreateKeyPairRequest = {}  # type: ignore[typeddict-item]
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_key_type = el.find("KeyType")
    if child_key_type is not None:
        import capo_ec2.types.key_type

        out["key_type"] = capo_ec2.types.key_type.deserialize_ec2_query(child_key_type)
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_key_format = el.find("KeyFormat")
    if child_key_format is not None:
        import capo_ec2.types.key_format

        out["key_format"] = capo_ec2.types.key_format.deserialize_ec2_query(
            child_key_format
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
