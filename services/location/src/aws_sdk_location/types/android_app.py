"""Generated from Smithy shape ``com.amazonaws.location#AndroidApp``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.android_package_name
    import aws_sdk_location.types.sha1_certificate_fingerprint


class AndroidApp(TypedDict):
    package: "aws_sdk_location.types.android_package_name.AndroidPackageName"
    """<p>Unique package name identifier for an Android app.</p> <p>Example: <code>com.mydomain.appname</code> </p>"""
    certificate_fingerprint: (
        "aws_sdk_location.types.sha1_certificate_fingerprint.Sha1CertificateFingerprint"
    )
    """<p>20 byte SHA-1 certificate fingerprint associated with the Android app signing certificate.</p> <p>Example: <code>BB:0D:AC:74:D3:21:E1:43:67:71:9B:62:91:AF:A1:66:6E:44:5D:75</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AndroidApp) -> dict:
    out: dict = {}
    out["Package"] = value["package"]
    out["CertificateFingerprint"] = value["certificate_fingerprint"]
    return out


def deserialize_json(data: dict) -> AndroidApp:
    out: AndroidApp = {}  # type: ignore[typeddict-item]
    if "Package" in data:
        out["package"] = data["Package"]
    else:
        raise DeserializationError("AndroidApp.package required")
    if "CertificateFingerprint" in data:
        out["certificate_fingerprint"] = data["CertificateFingerprint"]
    else:
        raise DeserializationError("AndroidApp.certificate_fingerprint required")
    return out
