"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.add_tags
    import aws_sdk_service_catalog.types.idempotency_token
    import aws_sdk_service_catalog.types.product_type
    import aws_sdk_service_catalog.types.product_view_name
    import aws_sdk_service_catalog.types.product_view_owner
    import aws_sdk_service_catalog.types.product_view_short_description
    import aws_sdk_service_catalog.types.provisioning_artifact_properties
    import aws_sdk_service_catalog.types.source_connection
    import aws_sdk_service_catalog.types.support_description
    import aws_sdk_service_catalog.types.support_email
    import aws_sdk_service_catalog.types.support_url


class CreateProductInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    name: "aws_sdk_service_catalog.types.product_view_name.ProductViewName"
    """<p>The name of the product.</p>"""
    owner: "aws_sdk_service_catalog.types.product_view_owner.ProductViewOwner"
    """<p>The owner of the product.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.product_view_short_description.ProductViewShortDescription"
    ]
    """<p>The description of the product.</p>"""
    distributor: NotRequired[
        "aws_sdk_service_catalog.types.product_view_owner.ProductViewOwner"
    ]
    """<p>The distributor of the product.</p>"""
    support_description: NotRequired[
        "aws_sdk_service_catalog.types.support_description.SupportDescription"
    ]
    """<p>The support information about the product.</p>"""
    support_email: NotRequired[
        "aws_sdk_service_catalog.types.support_email.SupportEmail"
    ]
    """<p>The contact email for product support.</p>"""
    support_url: NotRequired["aws_sdk_service_catalog.types.support_url.SupportUrl"]
    r"""<p>The contact URL for product support.</p> <p> <code>^https?:\/\// </code>/ is the pattern used to validate SupportUrl.</p>"""
    product_type: "aws_sdk_service_catalog.types.product_type.ProductType"
    """<p>The type of product.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.add_tags.AddTags"]
    """<p>One or more tags.</p>"""
    provisioning_artifact_parameters: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_properties.ProvisioningArtifactProperties"
    ]
    """<p>The configuration of the provisioning artifact. </p>"""
    idempotency_token: (
        "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""
    source_connection: NotRequired[
        "aws_sdk_service_catalog.types.source_connection.SourceConnection"
    ]
    """<p>Specifies connection details for the created product and syncs the product to the connection source artifact. This automatically manages the product's artifacts based on changes to the source. The <code>SourceConnection</code> parameter consists of the following sub-fields.</p> <ul> <li> <p> <code>Type</code> </p> </li> <li> <p> <code>ConnectionParamters</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["Name"] = value["name"]
    out["Owner"] = value["owner"]
    if "description" in value:
        out["Description"] = value["description"]
    if "distributor" in value:
        out["Distributor"] = value["distributor"]
    if "support_description" in value:
        out["SupportDescription"] = value["support_description"]
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_url" in value:
        out["SupportUrl"] = value["support_url"]
    import aws_sdk_service_catalog.types.product_type

    out["ProductType"] = (
        aws_sdk_service_catalog.types.product_type.serialize_aws_json_1_1(
            value["product_type"]
        )
    )
    if "tags" in value:
        import aws_sdk_service_catalog.types.add_tags

        out["Tags"] = aws_sdk_service_catalog.types.add_tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "provisioning_artifact_parameters" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_properties

        out["ProvisioningArtifactParameters"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_properties.serialize_aws_json_1_1(
                value["provisioning_artifact_parameters"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    if "source_connection" in value:
        import aws_sdk_service_catalog.types.source_connection

        out["SourceConnection"] = (
            aws_sdk_service_catalog.types.source_connection.serialize_aws_json_1_1(
                value["source_connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProductInput:
    out: CreateProductInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateProductInput.name required")
    if "Owner" in data:
        out["owner"] = data["Owner"]
    else:
        raise DeserializationError("CreateProductInput.owner required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Distributor" in data:
        out["distributor"] = data["Distributor"]
    if "SupportDescription" in data:
        out["support_description"] = data["SupportDescription"]
    if "SupportEmail" in data:
        out["support_email"] = data["SupportEmail"]
    if "SupportUrl" in data:
        out["support_url"] = data["SupportUrl"]
    if "ProductType" in data:
        import aws_sdk_service_catalog.types.product_type

        out["product_type"] = (
            aws_sdk_service_catalog.types.product_type.deserialize_aws_json_1_1(
                data["ProductType"]
            )
        )
    else:
        raise DeserializationError("CreateProductInput.product_type required")
    if "Tags" in data:
        import aws_sdk_service_catalog.types.add_tags

        out["tags"] = aws_sdk_service_catalog.types.add_tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ProvisioningArtifactParameters" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_properties

        out["provisioning_artifact_parameters"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_properties.deserialize_aws_json_1_1(
                data["ProvisioningArtifactParameters"]
            )
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError("CreateProductInput.idempotency_token required")
    if "SourceConnection" in data:
        import aws_sdk_service_catalog.types.source_connection

        out["source_connection"] = (
            aws_sdk_service_catalog.types.source_connection.deserialize_aws_json_1_1(
                data["SourceConnection"]
            )
        )
    return out
