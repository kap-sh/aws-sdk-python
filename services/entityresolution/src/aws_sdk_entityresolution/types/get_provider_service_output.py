"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetProviderServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.provider_component_schema
    import aws_sdk_entityresolution.types.provider_endpoint_configuration
    import aws_sdk_entityresolution.types.provider_id_name_space_configuration
    import aws_sdk_entityresolution.types.provider_intermediate_data_access_configuration
    import aws_sdk_entityresolution.types.provider_service_arn
    import aws_sdk_entityresolution.types.provider_service_display_name
    import aws_sdk_entityresolution.types.service_type


class GetProviderServiceOutput(TypedDict, closed=True):
    provider_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the provider. This name is typically the company name.</p>"""
    provider_service_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the product that the provider service provides. </p>"""
    provider_service_display_name: "aws_sdk_entityresolution.types.provider_service_display_name.ProviderServiceDisplayName"
    """<p>The display name of the provider service.</p>"""
    provider_service_type: "aws_sdk_entityresolution.types.service_type.ServiceType"
    """<p>The type of provider service.</p>"""
    provider_service_arn: (
        "aws_sdk_entityresolution.types.provider_service_arn.ProviderServiceArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the provider service.</p>"""
    provider_configuration_definition: NotRequired["object"]
    """<p>The definition of the provider configuration.</p>"""
    provider_id_name_space_configuration: NotRequired[
        "aws_sdk_entityresolution.types.provider_id_name_space_configuration.ProviderIdNameSpaceConfiguration"
    ]
    """<p>The provider configuration required for different ID namespace types.</p>"""
    provider_job_configuration: NotRequired["object"]
    """<p>Provider service job configurations.</p>"""
    provider_endpoint_configuration: "aws_sdk_entityresolution.types.provider_endpoint_configuration.ProviderEndpointConfiguration"
    """<p>The required configuration fields to use with the provider service.</p>"""
    anonymized_output: "bool"
    """<p>Specifies whether output data from the provider is anonymized. A value of <code>TRUE</code> means the output will be anonymized and you can't relate the data that comes back from the provider to the identifying input. A value of <code>FALSE</code> means the output won't be anonymized and you can relate the data that comes back from the provider to your source data. </p>"""
    provider_entity_output_definition: "object"
    """<p>The definition of the provider entity output.</p>"""
    provider_intermediate_data_access_configuration: NotRequired[
        "aws_sdk_entityresolution.types.provider_intermediate_data_access_configuration.ProviderIntermediateDataAccessConfiguration"
    ]
    """<p>The Amazon Web Services accounts and the S3 permissions that are required by some providers to create an S3 bucket for intermediate data storage.</p>"""
    provider_component_schema: NotRequired[
        "aws_sdk_entityresolution.types.provider_component_schema.ProviderComponentSchema"
    ]
    """<p>Input schema for the provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProviderServiceOutput) -> dict:
    out: dict = {}
    out["providerName"] = value["provider_name"]
    out["providerServiceName"] = value["provider_service_name"]
    out["providerServiceDisplayName"] = value["provider_service_display_name"]
    import aws_sdk_entityresolution.types.service_type

    out["providerServiceType"] = (
        aws_sdk_entityresolution.types.service_type.serialize_json(
            value["provider_service_type"]
        )
    )
    out["providerServiceArn"] = value["provider_service_arn"]
    if "provider_configuration_definition" in value:
        out["providerConfigurationDefinition"] = value[
            "provider_configuration_definition"
        ]
    if "provider_id_name_space_configuration" in value:
        import aws_sdk_entityresolution.types.provider_id_name_space_configuration

        out["providerIdNameSpaceConfiguration"] = (
            aws_sdk_entityresolution.types.provider_id_name_space_configuration.serialize_json(
                value["provider_id_name_space_configuration"]
            )
        )
    if "provider_job_configuration" in value:
        out["providerJobConfiguration"] = value["provider_job_configuration"]
    import aws_sdk_entityresolution.types.provider_endpoint_configuration

    out["providerEndpointConfiguration"] = (
        aws_sdk_entityresolution.types.provider_endpoint_configuration.serialize_json(
            value["provider_endpoint_configuration"]
        )
    )
    out["anonymizedOutput"] = value["anonymized_output"]
    out["providerEntityOutputDefinition"] = value["provider_entity_output_definition"]
    if "provider_intermediate_data_access_configuration" in value:
        import aws_sdk_entityresolution.types.provider_intermediate_data_access_configuration

        out["providerIntermediateDataAccessConfiguration"] = (
            aws_sdk_entityresolution.types.provider_intermediate_data_access_configuration.serialize_json(
                value["provider_intermediate_data_access_configuration"]
            )
        )
    if "provider_component_schema" in value:
        import aws_sdk_entityresolution.types.provider_component_schema

        out["providerComponentSchema"] = (
            aws_sdk_entityresolution.types.provider_component_schema.serialize_json(
                value["provider_component_schema"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetProviderServiceOutput:
    out: GetProviderServiceOutput = {}  # type: ignore[typeddict-item]
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    else:
        raise DeserializationError("GetProviderServiceOutput.provider_name required")
    if "providerServiceName" in data:
        out["provider_service_name"] = data["providerServiceName"]
    else:
        raise DeserializationError(
            "GetProviderServiceOutput.provider_service_name required"
        )
    if "providerServiceDisplayName" in data:
        out["provider_service_display_name"] = data["providerServiceDisplayName"]
    else:
        raise DeserializationError(
            "GetProviderServiceOutput.provider_service_display_name required"
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
            "GetProviderServiceOutput.provider_service_type required"
        )
    if "providerServiceArn" in data:
        out["provider_service_arn"] = data["providerServiceArn"]
    else:
        raise DeserializationError(
            "GetProviderServiceOutput.provider_service_arn required"
        )
    if "providerConfigurationDefinition" in data:
        out["provider_configuration_definition"] = data[
            "providerConfigurationDefinition"
        ]
    if "providerIdNameSpaceConfiguration" in data:
        import aws_sdk_entityresolution.types.provider_id_name_space_configuration

        out["provider_id_name_space_configuration"] = (
            aws_sdk_entityresolution.types.provider_id_name_space_configuration.deserialize_json(
                data["providerIdNameSpaceConfiguration"]
            )
        )
    if "providerJobConfiguration" in data:
        out["provider_job_configuration"] = data["providerJobConfiguration"]
    if "providerEndpointConfiguration" in data:
        import aws_sdk_entityresolution.types.provider_endpoint_configuration

        out["provider_endpoint_configuration"] = (
            aws_sdk_entityresolution.types.provider_endpoint_configuration.deserialize_json(
                data["providerEndpointConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetProviderServiceOutput.provider_endpoint_configuration required"
        )
    if "anonymizedOutput" in data:
        out["anonymized_output"] = data["anonymizedOutput"]
    else:
        raise DeserializationError(
            "GetProviderServiceOutput.anonymized_output required"
        )
    if "providerEntityOutputDefinition" in data:
        out["provider_entity_output_definition"] = data[
            "providerEntityOutputDefinition"
        ]
    else:
        raise DeserializationError(
            "GetProviderServiceOutput.provider_entity_output_definition required"
        )
    if "providerIntermediateDataAccessConfiguration" in data:
        import aws_sdk_entityresolution.types.provider_intermediate_data_access_configuration

        out["provider_intermediate_data_access_configuration"] = (
            aws_sdk_entityresolution.types.provider_intermediate_data_access_configuration.deserialize_json(
                data["providerIntermediateDataAccessConfiguration"]
            )
        )
    if "providerComponentSchema" in data:
        import aws_sdk_entityresolution.types.provider_component_schema

        out["provider_component_schema"] = (
            aws_sdk_entityresolution.types.provider_component_schema.deserialize_json(
                data["providerComponentSchema"]
            )
        )
    return out
