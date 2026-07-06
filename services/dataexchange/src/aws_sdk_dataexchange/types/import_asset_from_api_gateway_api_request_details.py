"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetFromApiGatewayApiRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093
    import aws_sdk_dataexchange.types.api_description
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.protocol_type


class ImportAssetFromApiGatewayApiRequestDetails(TypedDict, closed=True):
    api_description: NotRequired[
        "aws_sdk_dataexchange.types.api_description.ApiDescription"
    ]
    """<p>The API description. Markdown supported.</p>"""
    api_id: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The API Gateway API ID.</p>"""
    api_key: NotRequired["aws_sdk_dataexchange.types.__string.__string"]
    """<p>The API Gateway API key.</p>"""
    api_name: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The API name.</p>"""
    api_specification_md5_hash: "aws_sdk_dataexchange.types.__string_min24_max24_pattern_a_za_z094_a_za_z092_a_za_z093.__stringMin24Max24PatternAZaZ094AZaZ092AZaZ093"
    """<p>The Base64-encoded MD5 hash of the OpenAPI 3.0 JSON API specification file. It is used to ensure the integrity of the file.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The data set ID.</p>"""
    protocol_type: "aws_sdk_dataexchange.types.protocol_type.ProtocolType"
    """<p>The protocol type.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The revision ID.</p>"""
    stage: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The API stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetFromApiGatewayApiRequestDetails) -> dict:
    out: dict = {}
    if "api_description" in value:
        out["ApiDescription"] = value["api_description"]
    out["ApiId"] = value["api_id"]
    if "api_key" in value:
        out["ApiKey"] = value["api_key"]
    out["ApiName"] = value["api_name"]
    out["ApiSpecificationMd5Hash"] = value["api_specification_md5_hash"]
    out["DataSetId"] = value["data_set_id"]
    out["ProtocolType"] = value["protocol_type"]
    out["RevisionId"] = value["revision_id"]
    out["Stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> ImportAssetFromApiGatewayApiRequestDetails:
    out: ImportAssetFromApiGatewayApiRequestDetails = {}  # type: ignore[typeddict-item]
    if "ApiDescription" in data:
        out["api_description"] = data["ApiDescription"]
    if "ApiId" in data:
        out["api_id"] = data["ApiId"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiRequestDetails.api_id required"
        )
    if "ApiKey" in data:
        out["api_key"] = data["ApiKey"]
    if "ApiName" in data:
        out["api_name"] = data["ApiName"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiRequestDetails.api_name required"
        )
    if "ApiSpecificationMd5Hash" in data:
        out["api_specification_md5_hash"] = data["ApiSpecificationMd5Hash"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiRequestDetails.api_specification_md5_hash required"
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiRequestDetails.data_set_id required"
        )
    if "ProtocolType" in data:
        out["protocol_type"] = data["ProtocolType"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiRequestDetails.protocol_type required"
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiRequestDetails.revision_id required"
        )
    if "Stage" in data:
        out["stage"] = data["Stage"]
    else:
        raise DeserializationError(
            "ImportAssetFromApiGatewayApiRequestDetails.stage required"
        )
    return out
