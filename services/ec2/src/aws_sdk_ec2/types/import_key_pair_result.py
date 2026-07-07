"""Generated from Smithy shape ``com.amazonaws.ec2#ImportKeyPairResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ImportKeyPairResult(TypedDict, closed=True):
    key_fingerprint: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<ul> <li> <p>For RSA key pairs, the key fingerprint is the MD5 public key fingerprint as specified in section 4 of RFC 4716.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with <a href=\"http://www.openssh.com/txt/release-6.8\">OpenSSH 6.8</a>.</p> </li> </ul>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key pair name that you provided.</p>"""
    key_pair_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resulting key pair.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags applied to the imported key pair.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportKeyPairResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "key_fingerprint" in value:
        pairs.append((f"{prefix}.KeyFingerprint", str(value["key_fingerprint"])))
    if "key_name" in value:
        pairs.append((f"{prefix}.KeyName", str(value["key_name"])))
    if "key_pair_id" in value:
        pairs.append((f"{prefix}.KeyPairId", str(value["key_pair_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> ImportKeyPairResult:
    out: ImportKeyPairResult = {}  # type: ignore[typeddict-item]
    child_key_fingerprint = el.find("KeyFingerprint")
    if child_key_fingerprint is not None:
        out["key_fingerprint"] = str(child_key_fingerprint.text or "")
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_key_pair_id = el.find("KeyPairId")
    if child_key_pair_id is not None:
        out["key_pair_id"] = str(child_key_pair_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
