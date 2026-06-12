"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.owner_id
    import aws_sdk_elasticsearch_service.types.region


class DomainInformation(TypedDict):
    owner_id: NotRequired["aws_sdk_elasticsearch_service.types.owner_id.OwnerId"]
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    region: NotRequired["aws_sdk_elasticsearch_service.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: DomainInformation) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    out["DomainName"] = value["domain_name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> DomainInformation:
    out: DomainInformation = {}  # type: ignore[typeddict-item]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("DomainInformation.domain_name required")
    if "Region" in data:
        out["region"] = data["Region"]
    return out
