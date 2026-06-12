"""Generated from Smithy shape ``com.amazonaws.apigateway#DomainNameAccessAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.access_association_source_type
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.string


class DomainNameAccessAssociation(TypedDict):
    domain_name_access_association_arn: NotRequired[
        "aws_sdk_api_gateway.types.string.String"
    ]
    """<p>The ARN of the domain name access association resource. </p>"""
    domain_name_arn: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The ARN of the domain name. </p>"""
    access_association_source_type: NotRequired[
        "aws_sdk_api_gateway.types.access_association_source_type.AccessAssociationSourceType"
    ]
    """<p> The type of the domain name access association source. </p>"""
    access_association_source: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p> The ARN of the domain name access association source. For a VPCE, the ARN must be a VPC endpoint. </p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p> The collection of tags. Each tag element is associated with a given resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameAccessAssociation) -> dict:
    out: dict = {}
    if "domain_name_access_association_arn" in value:
        out["domainNameAccessAssociationArn"] = value[
            "domain_name_access_association_arn"
        ]
    if "domain_name_arn" in value:
        out["domainNameArn"] = value["domain_name_arn"]
    if "access_association_source_type" in value:
        import aws_sdk_api_gateway.types.access_association_source_type

        out["accessAssociationSourceType"] = (
            aws_sdk_api_gateway.types.access_association_source_type.serialize_json(
                value["access_association_source_type"]
            )
        )
    if "access_association_source" in value:
        out["accessAssociationSource"] = value["access_association_source"]
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DomainNameAccessAssociation:
    out: DomainNameAccessAssociation = {}  # type: ignore[typeddict-item]
    if "domainNameAccessAssociationArn" in data:
        out["domain_name_access_association_arn"] = data[
            "domainNameAccessAssociationArn"
        ]
    if "domainNameArn" in data:
        out["domain_name_arn"] = data["domainNameArn"]
    if "accessAssociationSourceType" in data:
        import aws_sdk_api_gateway.types.access_association_source_type

        out["access_association_source_type"] = (
            aws_sdk_api_gateway.types.access_association_source_type.deserialize_json(
                data["accessAssociationSourceType"]
            )
        )
    if "accessAssociationSource" in data:
        out["access_association_source"] = data["accessAssociationSource"]
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    return out
