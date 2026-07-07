"""Generated from Smithy shape ``com.amazonaws.acm#ExtendedKeyUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.extended_key_usage_name
    import aws_sdk_acm.types.string


class ExtendedKeyUsage(TypedDict, closed=True):
    name: NotRequired["aws_sdk_acm.types.extended_key_usage_name.ExtendedKeyUsageName"]
    """<p>The name of an Extended Key Usage value.</p>"""
    oid: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>An object identifier (OID) for the extension value. OIDs are strings of numbers separated by periods. The following OIDs are defined in RFC 3280 and RFC 5280. </p> <ul> <li> <p> <code>1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.3 (CODE_SIGNING)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.8 (TIME_STAMPING)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)</code> </p> </li> <li> <p> <code>1.3.6.1.5.5.7.3.7 (IPSEC_USER)</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedKeyUsage) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_acm.types.extended_key_usage_name

        out["Name"] = aws_sdk_acm.types.extended_key_usage_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "oid" in value:
        out["OID"] = value["oid"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendedKeyUsage:
    out: ExtendedKeyUsage = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_acm.types.extended_key_usage_name

        out["name"] = (
            aws_sdk_acm.types.extended_key_usage_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "OID" in data:
        out["oid"] = data["OID"]
    return out
