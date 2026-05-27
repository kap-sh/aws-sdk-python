"""Generated from Smithy shape ``com.amazonaws.ec2#ImportKeyPairResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ImportKeyPairResult(TypedDict):
    key_fingerprint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<ul> <li> <p>For RSA key pairs, the key fingerprint is the MD5 public key fingerprint as specified in section 4 of RFC 4716.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with <a href=\"http://www.openssh.com/txt/release-6.8\">OpenSSH 6.8</a>.</p> </li> </ul>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key pair name that you provided.</p>"""
    key_pair_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resulting key pair.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags applied to the imported key pair.</p>"""
