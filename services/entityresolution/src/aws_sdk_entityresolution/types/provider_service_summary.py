"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderServiceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.provider_service_arn
    import aws_sdk_entityresolution.types.provider_service_display_name
    import aws_sdk_entityresolution.types.service_type


class ProviderServiceSummary(TypedDict):
    provider_service_arn: (
        "aws_sdk_entityresolution.types.provider_service_arn.ProviderServiceArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>providerService</code>.</p>"""
    provider_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the provider. This name is typically the company name.</p>"""
    provider_service_display_name: "aws_sdk_entityresolution.types.provider_service_display_name.ProviderServiceDisplayName"
    """<p>The display name of the provider service.</p>"""
    provider_service_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the product that the provider service provides.</p>"""
    provider_service_type: "aws_sdk_entityresolution.types.service_type.ServiceType"
    """<p>The type of provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderServiceSummary) -> dict:
    out: dict = {}
    out["providerServiceArn"] = value["provider_service_arn"]
    out["providerName"] = value["provider_name"]
    out["providerServiceDisplayName"] = value["provider_service_display_name"]
    out["providerServiceName"] = value["provider_service_name"]
    import aws_sdk_entityresolution.types.service_type

    out["providerServiceType"] = (
        aws_sdk_entityresolution.types.service_type.serialize_json(
            value["provider_service_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProviderServiceSummary:
    out: ProviderServiceSummary = {}  # type: ignore[typeddict-item]
    if "providerServiceArn" in data:
        out["provider_service_arn"] = data["providerServiceArn"]
    else:
        raise DeserializationError(
            "ProviderServiceSummary.provider_service_arn required"
        )
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    else:
        raise DeserializationError("ProviderServiceSummary.provider_name required")
    if "providerServiceDisplayName" in data:
        out["provider_service_display_name"] = data["providerServiceDisplayName"]
    else:
        raise DeserializationError(
            "ProviderServiceSummary.provider_service_display_name required"
        )
    if "providerServiceName" in data:
        out["provider_service_name"] = data["providerServiceName"]
    else:
        raise DeserializationError(
            "ProviderServiceSummary.provider_service_name required"
        )
    if "providerServiceType" in data:
        import aws_sdk_entityresolution.types.service_type

        out["provider_service_type"] = (
            aws_sdk_entityresolution.types.service_type.deserialize_json(
                data["providerServiceType"]
            )
        )
    else:
        raise DeserializationError(
            "ProviderServiceSummary.provider_service_type required"
        )
    return out
