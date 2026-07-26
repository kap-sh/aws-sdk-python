"""Generated from Smithy shape ``com.amazonaws.dataexchange#ApiGatewayApiAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.api_description
    import capo_dataexchange.types.protocol_type
    import capo_dataexchange.types.timestamp


class ApiGatewayApiAsset(TypedDict, closed=True):
    api_description: NotRequired[
        "capo_dataexchange.types.api_description.ApiDescription"
    ]
    """<p>The API description of the API asset.</p>"""
    api_endpoint: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The API endpoint of the API asset.</p>"""
    api_id: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The unique identifier of the API asset.</p>"""
    api_key: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The API key of the API asset.</p>"""
    api_name: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The API name of the API asset.</p>"""
    api_specification_download_url: NotRequired[
        "capo_dataexchange.types.__string.__string"
    ]
    """<p>The download URL of the API specification of the API asset.</p>"""
    api_specification_download_url_expires_at: NotRequired[
        "capo_dataexchange.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the upload URL expires, in ISO 8601 format.</p>"""
    protocol_type: NotRequired["capo_dataexchange.types.protocol_type.ProtocolType"]
    """<p>The protocol type of the API asset.</p>"""
    stage: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The stage of the API asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayApiAsset) -> dict:
    out: dict = {}
    if "api_description" in value:
        out["ApiDescription"] = value["api_description"]
    if "api_endpoint" in value:
        out["ApiEndpoint"] = value["api_endpoint"]
    if "api_id" in value:
        out["ApiId"] = value["api_id"]
    if "api_key" in value:
        out["ApiKey"] = value["api_key"]
    if "api_name" in value:
        out["ApiName"] = value["api_name"]
    if "api_specification_download_url" in value:
        out["ApiSpecificationDownloadUrl"] = value["api_specification_download_url"]
    if "api_specification_download_url_expires_at" in value:
        import capo_dataexchange.types.timestamp

        out["ApiSpecificationDownloadUrlExpiresAt"] = (
            capo_dataexchange.types.timestamp.serialize_json(
                value["api_specification_download_url_expires_at"]
            )
        )
    if "protocol_type" in value:
        out["ProtocolType"] = value["protocol_type"]
    if "stage" in value:
        out["Stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> ApiGatewayApiAsset:
    out: ApiGatewayApiAsset = {}  # type: ignore[typeddict-item]
    if "ApiDescription" in data:
        out["api_description"] = data["ApiDescription"]
    if "ApiEndpoint" in data:
        out["api_endpoint"] = data["ApiEndpoint"]
    if "ApiId" in data:
        out["api_id"] = data["ApiId"]
    if "ApiKey" in data:
        out["api_key"] = data["ApiKey"]
    if "ApiName" in data:
        out["api_name"] = data["ApiName"]
    if "ApiSpecificationDownloadUrl" in data:
        out["api_specification_download_url"] = data["ApiSpecificationDownloadUrl"]
    if "ApiSpecificationDownloadUrlExpiresAt" in data:
        import capo_dataexchange.types.timestamp

        out["api_specification_download_url_expires_at"] = (
            capo_dataexchange.types.timestamp.deserialize_json(
                data["ApiSpecificationDownloadUrlExpiresAt"]
            )
        )
    if "ProtocolType" in data:
        out["protocol_type"] = data["ProtocolType"]
    if "Stage" in data:
        out["stage"] = data["Stage"]
    return out
