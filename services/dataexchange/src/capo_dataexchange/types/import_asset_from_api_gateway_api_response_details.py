"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromApiGatewayApiResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093
    import capo_dataexchange.types.api_description
    import capo_dataexchange.types.id
    import capo_dataexchange.types.protocol_type
    import capo_dataexchange.types.timestamp


class ImportAssetFromApiGatewayApiResponseDetails(TypedDict, closed=True):
    api_description: NotRequired[
        "capo_dataexchange.types.api_description.ApiDescription"
    ]
    """<p>The API description.</p>"""
    api_id: "capo_dataexchange.types.__string.__string"
    """<p>The API ID.</p>"""
    api_key: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The API key.</p>"""
    api_name: "capo_dataexchange.types.__string.__string"
    """<p>The API name.</p>"""
    api_specification_md5_hash: "capo_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093.__stringMin24Max24PatternAZaZ094AZaZ092AZaZ093"
    """<p>The Base64-encoded Md5 hash for the API asset, used to ensure the integrity of the API at that location.</p>"""
    api_specification_upload_url: "capo_dataexchange.types.__string.__string"
    """<p>The upload URL of the API specification.</p>"""
    api_specification_upload_url_expires_at: (
        "capo_dataexchange.types.timestamp.Timestamp"
    )
    """<p>The date and time that the upload URL expires, in ISO 8601 format.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The data set ID.</p>"""
    protocol_type: "capo_dataexchange.types.protocol_type.ProtocolType"
    """<p>The protocol type.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The revision ID.</p>"""
    stage: "capo_dataexchange.types.__string.__string"
    """<p>The API stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromApiGatewayApiResponseDetails) -> dict:
    out: dict = {}
    if "api_description" in value:
        out["ApiDescription"] = value["api_description"]
    out["ApiId"] = value["api_id"]
    if "api_key" in value:
        out["ApiKey"] = value["api_key"]
    out["ApiName"] = value["api_name"]
    out["ApiSpecificationMd5Hash"] = value["api_specification_md5_hash"]
    out["ApiSpecificationUploadUrl"] = value["api_specification_upload_url"]
    import capo_dataexchange.types.timestamp

    out["ApiSpecificationUploadUrlExpiresAt"] = (
        capo_dataexchange.types.timestamp.serialize_json(
            value["api_specification_upload_url_expires_at"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    out["ProtocolType"] = value["protocol_type"]
    out["RevisionId"] = value["revision_id"]
    out["Stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> ImportAssetFromApiGatewayApiResponseDetails:
    out: ImportAssetFromApiGatewayApiResponseDetails = {}  # type: ignore[typeddict-item]
    if "ApiDescription" in data:
        out["api_description"] = data["ApiDescription"]
    if "ApiId" in data:
        out["api_id"] = data["ApiId"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.api_id required"
        )
    if "ApiKey" in data:
        out["api_key"] = data["ApiKey"]
    if "ApiName" in data:
        out["api_name"] = data["ApiName"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.api_name required"
        )
    if "ApiSpecificationMd5Hash" in data:
        out["api_specification_md5_hash"] = data["ApiSpecificationMd5Hash"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.api_specification_md5_hash required"
        )
    if "ApiSpecificationUploadUrl" in data:
        out["api_specification_upload_url"] = data["ApiSpecificationUploadUrl"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.api_specification_upload_url required"
        )
    if "ApiSpecificationUploadUrlExpiresAt" in data:
        import capo_dataexchange.types.timestamp

        out["api_specification_upload_url_expires_at"] = (
            capo_dataexchange.types.timestamp.deserialize_json(
                data["ApiSpecificationUploadUrlExpiresAt"]
            )
        )
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.api_specification_upload_url_expires_at required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.data_set_id required"
        )
    if "ProtocolType" in data:
        out["protocol_type"] = data["ProtocolType"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.protocol_type required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.revision_id required"
        )
    if "Stage" in data:
        out["stage"] = data["Stage"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiResponseDetails.stage required"
        )
    return out
