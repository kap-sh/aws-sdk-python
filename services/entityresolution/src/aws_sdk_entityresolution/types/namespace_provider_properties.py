"""Generated from Smithy shape ``com.amazonaws.entityresolution#NamespaceProviderProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.provider_service_arn


class NamespaceProviderProperties(TypedDict, closed=True):
    provider_service_arn: (
        "aws_sdk_entityresolution.types.provider_service_arn.ProviderServiceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the provider service.</p>"""
    provider_configuration: NotRequired["object"]
    """<p>An object which defines any additional configurations required by the provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceProviderProperties) -> dict:
    out: dict = {}
    out["providerServiceArn"] = value["provider_service_arn"]
    if "provider_configuration" in value:
        out["providerConfiguration"] = value["provider_configuration"]
    return out


def deserialize_json(data: dict) -> NamespaceProviderProperties:
    out: NamespaceProviderProperties = {}  # type: ignore[typeddict-item]
    if "providerServiceArn" in data:
        out["provider_service_arn"] = data["providerServiceArn"]
    else:
        raise DeserializationError(
            "NamespaceProviderProperties.provider_service_arn required"
        )
    if "providerConfiguration" in data:
        out["provider_configuration"] = data["providerConfiguration"]
    return out
