"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.certificate_authority_arn
    import aws_sdk_pca_connector_ad.types.client_token
    import aws_sdk_pca_connector_ad.types.directory_id
    import aws_sdk_pca_connector_ad.types.tags
    import aws_sdk_pca_connector_ad.types.vpc_information


class CreateConnectorRequest(TypedDict):
    directory_id: "aws_sdk_pca_connector_ad.types.directory_id.DirectoryId"
    """<p>The identifier of the Active Directory.</p>"""
    certificate_authority_arn: "aws_sdk_pca_connector_ad.types.certificate_authority_arn.CertificateAuthorityArn"
    """<p> The Amazon Resource Name (ARN) of the certificate authority being used.</p>"""
    vpc_information: "aws_sdk_pca_connector_ad.types.vpc_information.VpcInformation"
    """<p>Information about your VPC and security groups used with the connector.</p>"""
    client_token: NotRequired["aws_sdk_pca_connector_ad.types.client_token.ClientToken"]
    """<p>Idempotency token.</p>"""
    tags: NotRequired["aws_sdk_pca_connector_ad.types.tags.Tags"]
    """<p>Metadata assigned to a connector consisting of a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    import aws_sdk_pca_connector_ad.types.vpc_information

    out["VpcInformation"] = (
        aws_sdk_pca_connector_ad.types.vpc_information.serialize_json(
            value["vpc_information"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_pca_connector_ad.types.tags

        out["Tags"] = aws_sdk_pca_connector_ad.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("CreateConnectorRequest.directory_id required")
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "CreateConnectorRequest.certificate_authority_arn required"
        )
    if "VpcInformation" in data:
        import aws_sdk_pca_connector_ad.types.vpc_information

        out["vpc_information"] = (
            aws_sdk_pca_connector_ad.types.vpc_information.deserialize_json(
                data["VpcInformation"]
            )
        )
    else:
        raise DeserializationError("CreateConnectorRequest.vpc_information required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_pca_connector_ad.types.tags

        out["tags"] = aws_sdk_pca_connector_ad.types.tags.deserialize_json(data["Tags"])
    return out
