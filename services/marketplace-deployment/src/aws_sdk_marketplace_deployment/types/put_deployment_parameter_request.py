"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#PutDeploymentParameterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_deployment.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_marketplace_deployment.types.catalog
    import aws_sdk_marketplace_deployment.types.client_token
    import aws_sdk_marketplace_deployment.types.deployment_parameter_input
    import aws_sdk_marketplace_deployment.types.resource_id
    import aws_sdk_marketplace_deployment.types.tags_map


class PutDeploymentParameterRequest(TypedDict, closed=True):
    catalog: "aws_sdk_marketplace_deployment.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    product_id: "aws_sdk_marketplace_deployment.types.resource_id.ResourceId"
    """<p>The product for which AWS Marketplace will save secrets for the buyer’s account.</p>"""
    agreement_id: "aws_sdk_marketplace_deployment.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""
    deployment_parameter: "aws_sdk_marketplace_deployment.types.deployment_parameter_input.DeploymentParameterInput"
    """<p>The deployment parameter targeted to the acceptor of an agreement for which to create the AWS Secret Manager resource.</p>"""
    tags: NotRequired["aws_sdk_marketplace_deployment.types.tags_map.TagsMap"]
    """<p>A map of key-value pairs, where each pair represents a tag saved to the resource. Tags will only be applied for create operations, and they'll be ignored if the resource already exists.</p>"""
    expiration_date: NotRequired["datetime.datetime"]
    """<p>The date when deployment parameters expire and are scheduled for deletion.</p>"""
    client_token: NotRequired[
        "aws_sdk_marketplace_deployment.types.client_token.ClientToken"
    ]
    """<p>The idempotency token for deployment parameters. A unique identifier for the new version.</p> <note> <p>This field is not required if you're calling using an AWS SDK. Otherwise, a <code>clientToken</code> must be provided with the request.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDeploymentParameterRequest) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    import aws_sdk_marketplace_deployment.types.deployment_parameter_input

    out["deploymentParameter"] = (
        aws_sdk_marketplace_deployment.types.deployment_parameter_input.serialize_json(
            value["deployment_parameter"]
        )
    )
    if "tags" in value:
        import aws_sdk_marketplace_deployment.types.tags_map

        out["tags"] = aws_sdk_marketplace_deployment.types.tags_map.serialize_json(
            value["tags"]
        )
    if "expiration_date" in value:
        import aws_sdk_marketplace_deployment.types._prelude.timestamp

        out["expirationDate"] = (
            aws_sdk_marketplace_deployment.types._prelude.timestamp.serialize_json(
                value["expiration_date"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutDeploymentParameterRequest:
    out: PutDeploymentParameterRequest = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "PutDeploymentParameterRequest.agreement_id required"
        )
    if "deploymentParameter" in data:
        import aws_sdk_marketplace_deployment.types.deployment_parameter_input

        out["deployment_parameter"] = (
            aws_sdk_marketplace_deployment.types.deployment_parameter_input.deserialize_json(
                data["deploymentParameter"]
            )
        )
    else:
        raise DeserializationError(
            "PutDeploymentParameterRequest.deployment_parameter required"
        )
    if "tags" in data:
        import aws_sdk_marketplace_deployment.types.tags_map

        out["tags"] = aws_sdk_marketplace_deployment.types.tags_map.deserialize_json(
            data["tags"]
        )
    if "expirationDate" in data:
        import aws_sdk_marketplace_deployment.types._prelude.timestamp

        out["expiration_date"] = (
            aws_sdk_marketplace_deployment.types._prelude.timestamp.deserialize_json(
                data["expirationDate"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
