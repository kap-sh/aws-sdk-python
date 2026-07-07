"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeDomainEndpointOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.boolean
    import aws_sdk_cloudsearch.types.domain_name


class DescribeDomainEndpointOptionsRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    """<p>A string that represents the name of a domain.</p>"""
    deployed: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>Whether to retrieve the latest configuration (which might be in a Processing state) or the current, active configuration. Defaults to <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDomainEndpointOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    if "deployed" in value:
        pairs.append((f"{prefix}.Deployed", "true" if value["deployed"] else "false"))


def deserialize_query(el: Element) -> DescribeDomainEndpointOptionsRequest:
    out: DescribeDomainEndpointOptionsRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError(
            "DescribeDomainEndpointOptionsRequest.domain_name required"
        )
    child_deployed = el.find("Deployed")
    if child_deployed is not None:
        out["deployed"] = (child_deployed.text or "").lower() == "true"
    return out
