"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateDomainNameAccessAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.access_association_source_type
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class CreateDomainNameAccessAssociationRequest(TypedDict):
    domain_name_arn: "aws_sdk_api_gateway.types.string.String"
    """<p> The ARN of the domain name. </p>"""
    access_association_source_type: "aws_sdk_api_gateway.types.access_association_source_type.AccessAssociationSourceType"
    """<p> The type of the domain name access association source. </p>"""
    access_association_source: "aws_sdk_api_gateway.types.string.String"
    """<p> The identifier of the domain name access association source. For a VPCE, the value is the VPC endpoint ID. </p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainNameAccessAssociationRequest) -> dict:
    out: dict = {}
    out["domainNameArn"] = value["domain_name_arn"]
    import aws_sdk_api_gateway.types.access_association_source_type

    out["accessAssociationSourceType"] = (
        aws_sdk_api_gateway.types.access_association_source_type.serialize_json(
            value["access_association_source_type"]
        )
    )
    out["accessAssociationSource"] = value["access_association_source"]
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDomainNameAccessAssociationRequest:
    out: CreateDomainNameAccessAssociationRequest = {}  # type: ignore[typeddict-item]
    if "domainNameArn" in data:
        out["domain_name_arn"] = data["domainNameArn"]
    else:
        raise DeserializationError(
            "CreateDomainNameAccessAssociationRequest.domain_name_arn required"
        )
    if "accessAssociationSourceType" in data:
        import aws_sdk_api_gateway.types.access_association_source_type

        out["access_association_source_type"] = (
            aws_sdk_api_gateway.types.access_association_source_type.deserialize_json(
                data["accessAssociationSourceType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDomainNameAccessAssociationRequest.access_association_source_type required"
        )
    if "accessAssociationSource" in data:
        out["access_association_source"] = data["accessAssociationSource"]
    else:
        raise DeserializationError(
            "CreateDomainNameAccessAssociationRequest.access_association_source required"
        )
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
