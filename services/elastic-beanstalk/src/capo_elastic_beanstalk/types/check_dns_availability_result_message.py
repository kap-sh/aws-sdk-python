"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CheckDNSAvailabilityResultMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.cname_availability
    import capo_elastic_beanstalk.types.dns_cname


class CheckDNSAvailabilityResultMessage(TypedDict, closed=True):
    available: NotRequired[
        "capo_elastic_beanstalk.types.cname_availability.CnameAvailability"
    ]
    """<p>Indicates if the specified CNAME is available:</p> <ul> <li> <p> <code>true</code> : The CNAME is available.</p> </li> <li> <p> <code>false</code> : The CNAME is not available.</p> </li> </ul>"""
    fully_qualified_cname: NotRequired[
        "capo_elastic_beanstalk.types.dns_cname.DNSCname"
    ]
    """<p>The fully qualified CNAME to reserve when <a>CreateEnvironment</a> is called with the provided prefix.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CheckDNSAvailabilityResultMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "available" in value:
        pairs.append(
            (f"{key_prefix}Available", "true" if value["available"] else "false")
        )
    if "fully_qualified_cname" in value:
        pairs.append(
            (f"{key_prefix}FullyQualifiedCNAME", str(value["fully_qualified_cname"]))
        )


def deserialize_query(el: Element) -> CheckDNSAvailabilityResultMessage:
    out: CheckDNSAvailabilityResultMessage = {}  # type: ignore[typeddict-item]
    child_available = el.find("Available")
    if child_available is not None:
        out["available"] = (child_available.text or "").lower() == "true"
    child_fully_qualified_cname = el.find("FullyQualifiedCNAME")
    if child_fully_qualified_cname is not None:
        out["fully_qualified_cname"] = str(child_fully_qualified_cname.text or "")
    return out
