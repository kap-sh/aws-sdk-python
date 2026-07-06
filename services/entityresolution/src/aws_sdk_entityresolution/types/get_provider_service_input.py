"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetProviderServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.provider_service_arn


class GetProviderServiceInput(TypedDict, closed=True):
    provider_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the provider. This name is typically the company name.</p>"""
    provider_service_name: (
        "aws_sdk_entityresolution.types.provider_service_arn.ProviderServiceArn"
    )
    """<p>The ARN (Amazon Resource Name) of the product that the provider service provides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProviderServiceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProviderServiceInput:
    out: GetProviderServiceInput = {}  # type: ignore[typeddict-item]
    return out
