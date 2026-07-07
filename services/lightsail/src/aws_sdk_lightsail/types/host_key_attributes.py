"""Generated from Smithy shape ``com.amazonaws.lightsail#HostKeyAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.string


class HostKeyAttributes(TypedDict, closed=True):
    algorithm: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The SSH host key algorithm or the RDP certificate format.</p> <p>For SSH host keys, the algorithm may be <code>ssh-rsa</code>, <code>ecdsa-sha2-nistp256</code>, <code>ssh-ed25519</code>, etc. For RDP certificates, the algorithm is always <code>x509-cert</code>.</p>"""
    public_key: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The public SSH host key or the RDP certificate.</p>"""
    witnessed_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The time that the SSH host key or RDP certificate was recorded by Lightsail.</p>"""
    fingerprint_sha1: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The SHA-1 fingerprint of the returned SSH host key or RDP certificate.</p> <ul> <li> <p>Example of an SHA-1 SSH fingerprint:</p> <p> <code>SHA1:1CHH6FaAaXjtFOsR/t83vf91SR0</code> </p> </li> <li> <p>Example of an SHA-1 RDP fingerprint:</p> <p> <code>af:34:51:fe:09:f0:e0:da:b8:4e:56:ca:60:c2:10:ff:38:06:db:45</code> </p> </li> </ul>"""
    fingerprint_sha256: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The SHA-256 fingerprint of the returned SSH host key or RDP certificate.</p> <ul> <li> <p>Example of an SHA-256 SSH fingerprint:</p> <p> <code>SHA256:KTsMnRBh1IhD17HpdfsbzeGA4jOijm5tyXsMjKVbB8o</code> </p> </li> <li> <p>Example of an SHA-256 RDP fingerprint:</p> <p> <code>03:9b:36:9f:4b:de:4e:61:70:fc:7c:c9:78:e7:d2:1a:1c:25:a8:0c:91:f6:7c:e4:d6:a0:85:c8:b4:53:99:68</code> </p> </li> </ul>"""
    not_valid_before: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The returned RDP certificate is valid after this point in time.</p> <p>This value is listed only for RDP certificates.</p>"""
    not_valid_after: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The returned RDP certificate is not valid after this point in time.</p> <p>This value is listed only for RDP certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostKeyAttributes) -> dict:
    out: dict = {}
    if "algorithm" in value:
        out["algorithm"] = value["algorithm"]
    if "public_key" in value:
        out["publicKey"] = value["public_key"]
    if "witnessed_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["witnessedAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["witnessed_at"]
        )
    if "fingerprint_sha1" in value:
        out["fingerprintSHA1"] = value["fingerprint_sha1"]
    if "fingerprint_sha256" in value:
        out["fingerprintSHA256"] = value["fingerprint_sha256"]
    if "not_valid_before" in value:
        import aws_sdk_lightsail.types.iso_date

        out["notValidBefore"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_valid_before"]
        )
    if "not_valid_after" in value:
        import aws_sdk_lightsail.types.iso_date

        out["notValidAfter"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_valid_after"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HostKeyAttributes:
    out: HostKeyAttributes = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        out["algorithm"] = data["algorithm"]
    if "publicKey" in data:
        out["public_key"] = data["publicKey"]
    if "witnessedAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["witnessed_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["witnessedAt"]
        )
    if "fingerprintSHA1" in data:
        out["fingerprint_sha1"] = data["fingerprintSHA1"]
    if "fingerprintSHA256" in data:
        out["fingerprint_sha256"] = data["fingerprintSHA256"]
    if "notValidBefore" in data:
        import aws_sdk_lightsail.types.iso_date

        out["not_valid_before"] = (
            aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
                data["notValidBefore"]
            )
        )
    if "notValidAfter" in data:
        import aws_sdk_lightsail.types.iso_date

        out["not_valid_after"] = (
            aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
                data["notValidAfter"]
            )
        )
    return out
