"""Generated from Smithy shape ``com.amazonaws.ec2#KeyPair``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.sensitive_user_data
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class KeyPair(TypedDict):
    key_pair_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the key pair.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the key pair.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    key_fingerprint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<ul> <li> <p>For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with OpenSSH 6.8.</p> </li> </ul>"""
    key_material: NotRequired["aws_sdk_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>An unencrypted PEM encoded RSA or ED25519 private key.</p>"""
