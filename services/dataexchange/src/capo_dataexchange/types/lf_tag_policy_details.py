"""Generated from Smithy shape ``com.amazonaws.dataexchange#LFTagPolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.aws_account_id
    import capo_dataexchange.types.lf_resource_details
    import capo_dataexchange.types.lf_resource_type


class LFTagPolicyDetails(TypedDict, closed=True):
    catalog_id: "capo_dataexchange.types.aws_account_id.AwsAccountId"
    """<p>The identifier for the AWS Glue Data Catalog.</p>"""
    resource_type: "capo_dataexchange.types.lf_resource_type.LFResourceType"
    """<p>The resource type for which the LF-tag policy applies.</p>"""
    resource_details: "capo_dataexchange.types.lf_resource_details.LFResourceDetails"
    """<p>Details for the Lake Formation Resources included in the LF-tag policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagPolicyDetails) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["ResourceType"] = value["resource_type"]
    import capo_dataexchange.types.lf_resource_details

    out["ResourceDetails"] = capo_dataexchange.types.lf_resource_details.serialize_json(
        value["resource_details"]
    )
    return out


def deserialize_json(data: dict) -> LFTagPolicyDetails:
    out: LFTagPolicyDetails = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError("LFTagPolicyDetails.catalog_id required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("LFTagPolicyDetails.resource_type required")
    if "ResourceDetails" in data:
        import capo_dataexchange.types.lf_resource_details

        out["resource_details"] = (
            capo_dataexchange.types.lf_resource_details.deserialize_json(
                data["ResourceDetails"]
            )
        )
    else:
        raise DeserializationError("LFTagPolicyDetails.resource_details required")
    return out
