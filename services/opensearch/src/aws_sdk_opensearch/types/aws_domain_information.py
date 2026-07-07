"""Generated from Smithy shape ``com.amazonaws.opensearch#AWSDomainInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.owner_id
    import aws_sdk_opensearch.types.region


class AWSDomainInformation(TypedDict, closed=True):
    owner_id: NotRequired["aws_sdk_opensearch.types.owner_id.OwnerId"]
    """<p>The Amazon Web Services account ID of the domain owner.</p>"""
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>Name of the domain.</p>"""
    region: NotRequired["aws_sdk_opensearch.types.region.Region"]
    """<p>The Amazon Web Services Region in which the domain is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSDomainInformation) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    out["DomainName"] = value["domain_name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> AWSDomainInformation:
    out: AWSDomainInformation = {}  # type: ignore[typeddict-item]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("AWSDomainInformation.domain_name required")
    if "Region" in data:
        out["region"] = data["Region"]
    return out
