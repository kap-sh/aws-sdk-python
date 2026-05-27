"""Generated from Smithy shape ``com.amazonaws.ec2#KeyPairInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.key_type
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class KeyPairInfo(TypedDict):
    key_pair_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the key pair.</p>"""
    key_type: NotRequired["aws_sdk_ec2.types.key_type.KeyType"]
    """<p>The type of key pair.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the key pair.</p>"""
    public_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public key material.</p>"""
    create_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>If you used Amazon EC2 to create the key pair, this is the date and time when the key was created, in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601 date-time format</a>, in the UTC time zone.</p> <p>If you imported an existing key pair to Amazon EC2, this is the date and time the key was imported, in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601 date-time format</a>, in the UTC time zone.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    key_fingerprint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If you used <a>CreateKeyPair</a> to create the key pair:</p> <ul> <li> <p>For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with <a href=\"http://www.openssh.com/txt/release-6.8\">OpenSSH 6.8</a>.</p> </li> </ul> <p>If you used <a>ImportKeyPair</a> to provide Amazon Web Services the public key:</p> <ul> <li> <p>For RSA key pairs, the key fingerprint is the MD5 public key fingerprint as specified in section 4 of RFC4716.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with <a href=\"http://www.openssh.com/txt/release-6.8\">OpenSSH 6.8</a>.</p> </li> </ul>"""
