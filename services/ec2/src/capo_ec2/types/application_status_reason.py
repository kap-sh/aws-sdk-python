"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class ApplicationStatusReason(TypedDict, closed=True):
    code: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason code for the application status check result. Possible values:</p> <ul> <li> <p> <code>ResponseCodeMatched</code> – The HTTP status code returned by the health check matched the configured <code>StatusCodeMatcher</code>.</p> </li> <li> <p> <code>ResponseCodeMismatch</code> – The HTTP status code returned by the health check did not match the configured <code>StatusCodeMatcher</code>.</p> </li> <li> <p> <code>ConnectionTimeout</code> – The connection to the target timed out.</p> </li> <li> <p> <code>ResponseTimeout</code> – The health check timed out while waiting for a response from the target.</p> </li> <li> <p> <code>ConnectionRefused</code> – The target refused the health check connection.</p> </li> <li> <p> <code>ConnectionReset</code> – The target reset the health check connection before returning a response.</p> </li> </ul> <p>Current health check results use the values in the preceding list. Legacy results that do not contain structured reason metadata can instead contain a producer error type, such as <code>Http Status Code</code> or <code>HttpConnectTimeoutException</code>.</p> <p>For <code>ResponseCodeMatched</code> and <code>ResponseCodeMismatch</code>, the <code>statusCode</code> field contains the returned HTTP status code. The <code>protocol</code> field contains the protocol used for the health check.</p>"""
    status_code: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The HTTP status code returned by the health check.</p>"""
    protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The protocol used for the health check. Possible values: <code>HTTP</code> and <code>HTTPS</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplicationStatusReason, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        pairs.append((f"{key_prefix}Code", str(value["code"])))
    if "status_code" in value:
        pairs.append((f"{key_prefix}StatusCode", str(value["status_code"])))
    if "protocol" in value:
        pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))


def deserialize_ec2_query(el: Element) -> ApplicationStatusReason:
    out: ApplicationStatusReason = {}  # type: ignore[typeddict-item]
    child_code = el.find("code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_status_code = el.find("statusCode")
    if child_status_code is not None:
        out["status_code"] = int(child_status_code.text or "")
    child_protocol = el.find("protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    return out
