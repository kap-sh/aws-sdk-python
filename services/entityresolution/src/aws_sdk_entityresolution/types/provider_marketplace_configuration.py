"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderMarketplaceConfiguration``."""

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError


class ProviderMarketplaceConfiguration(TypedDict, closed=True):
    data_set_id: "str"
    """<p>The dataset ID on Data Exchange.</p>"""
    revision_id: "str"
    """<p>The revision ID on Data Exchange.</p>"""
    asset_id: "str"
    """<p>The asset ID on Data Exchange.</p>"""
    listing_id: "str"
    """<p>The listing ID on Data Exchange.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderMarketplaceConfiguration) -> dict:
    out: dict = {}
    out["dataSetId"] = value["data_set_id"]
    out["revisionId"] = value["revision_id"]
    out["assetId"] = value["asset_id"]
    out["listingId"] = value["listing_id"]
    return out


def deserialize_json(data: dict) -> ProviderMarketplaceConfiguration:
    out: ProviderMarketplaceConfiguration = {}  # type: ignore[typeddict-item]
    if "dataSetId" in data:
        out["data_set_id"] = data["dataSetId"]
    else:
        raise DeserializationError(
            "ProviderMarketplaceConfiguration.data_set_id required"
        )
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError(
            "ProviderMarketplaceConfiguration.revision_id required"
        )
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    else:
        raise DeserializationError("ProviderMarketplaceConfiguration.asset_id required")
    if "listingId" in data:
        out["listing_id"] = data["listingId"]
    else:
        raise DeserializationError(
            "ProviderMarketplaceConfiguration.listing_id required"
        )
    return out
