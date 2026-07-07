"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DkimAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.dkim_status
    import aws_sdk_pinpoint_email.types.dns_token_list
    import aws_sdk_pinpoint_email.types.enabled


class DkimAttributes(TypedDict, closed=True):
    signing_enabled: "aws_sdk_pinpoint_email.types.enabled.Enabled"
    """<p>If the value is <code>true</code>, then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. If the value is <code>false</code>, then the messages that Amazon Pinpoint sends from the identity aren't DKIM-signed.</p>"""
    status: NotRequired["aws_sdk_pinpoint_email.types.dkim_status.DkimStatus"]
    """<p>Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:</p> <ul> <li> <p> <code>PENDING</code> – Amazon Pinpoint hasn't yet located the DKIM records in the DNS configuration for the domain, but will continue to attempt to locate them.</p> </li> <li> <p> <code>SUCCESS</code> – Amazon Pinpoint located the DKIM records in the DNS configuration for the domain and determined that they're correct. Amazon Pinpoint can now send DKIM-signed email from the identity.</p> </li> <li> <p> <code>FAILED</code> – Amazon Pinpoint was unable to locate the DKIM records in the DNS settings for the domain, and won't continue to search for them.</p> </li> <li> <p> <code>TEMPORARY_FAILURE</code> – A temporary issue occurred, which prevented Amazon Pinpoint from determining the DKIM status for the domain.</p> </li> <li> <p> <code>NOT_STARTED</code> – Amazon Pinpoint hasn't yet started searching for the DKIM records in the DKIM records for the domain.</p> </li> </ul>"""
    tokens: NotRequired["aws_sdk_pinpoint_email.types.dns_token_list.DnsTokenList"]
    """<p>A set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint usually detects these records within about 72 hours of adding them to the DNS configuration for your domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DkimAttributes) -> dict:
    out: dict = {}
    out["SigningEnabled"] = value.get("signing_enabled", False)
    if "status" in value:
        import aws_sdk_pinpoint_email.types.dkim_status

        out["Status"] = aws_sdk_pinpoint_email.types.dkim_status.serialize_json(
            value["status"]
        )
    if "tokens" in value:
        import aws_sdk_pinpoint_email.types.dns_token_list

        out["Tokens"] = aws_sdk_pinpoint_email.types.dns_token_list.serialize_json(
            value["tokens"]
        )
    return out


def deserialize_json(data: dict) -> DkimAttributes:
    out: DkimAttributes = {}  # type: ignore[typeddict-item]
    if "SigningEnabled" in data:
        out["signing_enabled"] = data["SigningEnabled"]
    else:
        out["signing_enabled"] = False
    if "Status" in data:
        import aws_sdk_pinpoint_email.types.dkim_status

        out["status"] = aws_sdk_pinpoint_email.types.dkim_status.deserialize_json(
            data["Status"]
        )
    if "Tokens" in data:
        import aws_sdk_pinpoint_email.types.dns_token_list

        out["tokens"] = aws_sdk_pinpoint_email.types.dns_token_list.deserialize_json(
            data["Tokens"]
        )
    return out
