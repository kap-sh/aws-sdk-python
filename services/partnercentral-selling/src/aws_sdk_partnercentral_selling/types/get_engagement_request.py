"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetEngagementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier


class GetEngagementRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the engagement request. Valid values are <code>AWS</code> and <code>Sandbox</code>.</p>"""
    identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier"
    """<p>Specifies the identifier of the Engagement record to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEngagementRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEngagementRequest:
    out: GetEngagementRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetEngagementRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetEngagementRequest.identifier required")
    return out
