"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOption``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_marketplace_discovery.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.amazon_machine_image_fulfillment_option
    import aws_sdk_marketplace_discovery.types.api_fulfillment_option
    import aws_sdk_marketplace_discovery.types.cloud_formation_fulfillment_option
    import aws_sdk_marketplace_discovery.types.container_fulfillment_option
    import aws_sdk_marketplace_discovery.types.data_exchange_fulfillment_option
    import aws_sdk_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option
    import aws_sdk_marketplace_discovery.types.eks_add_on_fulfillment_option
    import aws_sdk_marketplace_discovery.types.helm_fulfillment_option
    import aws_sdk_marketplace_discovery.types.professional_services_fulfillment_option
    import aws_sdk_marketplace_discovery.types.saas_fulfillment_option
    import aws_sdk_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option
    import aws_sdk_marketplace_discovery.types.sage_maker_model_fulfillment_option


class _FulfillmentOption_amazonMachineImageFulfillmentOption(TypedDict):
    amazonMachineImageFulfillmentOption: "aws_sdk_marketplace_discovery.types.amazon_machine_image_fulfillment_option.AmazonMachineImageFulfillmentOption"


class _FulfillmentOption_apiFulfillmentOption(TypedDict):
    apiFulfillmentOption: "aws_sdk_marketplace_discovery.types.api_fulfillment_option.ApiFulfillmentOption"


class _FulfillmentOption_cloudFormationFulfillmentOption(TypedDict):
    cloudFormationFulfillmentOption: "aws_sdk_marketplace_discovery.types.cloud_formation_fulfillment_option.CloudFormationFulfillmentOption"


class _FulfillmentOption_containerFulfillmentOption(TypedDict):
    containerFulfillmentOption: "aws_sdk_marketplace_discovery.types.container_fulfillment_option.ContainerFulfillmentOption"


class _FulfillmentOption_helmFulfillmentOption(TypedDict):
    helmFulfillmentOption: "aws_sdk_marketplace_discovery.types.helm_fulfillment_option.HelmFulfillmentOption"


class _FulfillmentOption_eksAddOnFulfillmentOption(TypedDict):
    eksAddOnFulfillmentOption: "aws_sdk_marketplace_discovery.types.eks_add_on_fulfillment_option.EksAddOnFulfillmentOption"


class _FulfillmentOption_ec2ImageBuilderComponentFulfillmentOption(TypedDict):
    ec2ImageBuilderComponentFulfillmentOption: "aws_sdk_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option.Ec2ImageBuilderComponentFulfillmentOption"


class _FulfillmentOption_dataExchangeFulfillmentOption(TypedDict):
    dataExchangeFulfillmentOption: "aws_sdk_marketplace_discovery.types.data_exchange_fulfillment_option.DataExchangeFulfillmentOption"


class _FulfillmentOption_professionalServicesFulfillmentOption(TypedDict):
    professionalServicesFulfillmentOption: "aws_sdk_marketplace_discovery.types.professional_services_fulfillment_option.ProfessionalServicesFulfillmentOption"


class _FulfillmentOption_saasFulfillmentOption(TypedDict):
    saasFulfillmentOption: "aws_sdk_marketplace_discovery.types.saas_fulfillment_option.SaasFulfillmentOption"


class _FulfillmentOption_sageMakerAlgorithmFulfillmentOption(TypedDict):
    sageMakerAlgorithmFulfillmentOption: "aws_sdk_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option.SageMakerAlgorithmFulfillmentOption"


class _FulfillmentOption_sageMakerModelFulfillmentOption(TypedDict):
    sageMakerModelFulfillmentOption: "aws_sdk_marketplace_discovery.types.sage_maker_model_fulfillment_option.SageMakerModelFulfillmentOption"


FulfillmentOption: TypeAlias = (
    _FulfillmentOption_amazonMachineImageFulfillmentOption
    | _FulfillmentOption_apiFulfillmentOption
    | _FulfillmentOption_cloudFormationFulfillmentOption
    | _FulfillmentOption_containerFulfillmentOption
    | _FulfillmentOption_helmFulfillmentOption
    | _FulfillmentOption_eksAddOnFulfillmentOption
    | _FulfillmentOption_ec2ImageBuilderComponentFulfillmentOption
    | _FulfillmentOption_dataExchangeFulfillmentOption
    | _FulfillmentOption_professionalServicesFulfillmentOption
    | _FulfillmentOption_saasFulfillmentOption
    | _FulfillmentOption_sageMakerAlgorithmFulfillmentOption
    | _FulfillmentOption_sageMakerModelFulfillmentOption
)


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentOption) -> dict:
    if "amazonMachineImageFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.amazon_machine_image_fulfillment_option

        return {
            "amazonMachineImageFulfillmentOption": aws_sdk_marketplace_discovery.types.amazon_machine_image_fulfillment_option.serialize_json(
                value["amazonMachineImageFulfillmentOption"]
            )
        }
    elif "apiFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.api_fulfillment_option

        return {
            "apiFulfillmentOption": aws_sdk_marketplace_discovery.types.api_fulfillment_option.serialize_json(
                value["apiFulfillmentOption"]
            )
        }
    elif "cloudFormationFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.cloud_formation_fulfillment_option

        return {
            "cloudFormationFulfillmentOption": aws_sdk_marketplace_discovery.types.cloud_formation_fulfillment_option.serialize_json(
                value["cloudFormationFulfillmentOption"]
            )
        }
    elif "containerFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.container_fulfillment_option

        return {
            "containerFulfillmentOption": aws_sdk_marketplace_discovery.types.container_fulfillment_option.serialize_json(
                value["containerFulfillmentOption"]
            )
        }
    elif "helmFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.helm_fulfillment_option

        return {
            "helmFulfillmentOption": aws_sdk_marketplace_discovery.types.helm_fulfillment_option.serialize_json(
                value["helmFulfillmentOption"]
            )
        }
    elif "eksAddOnFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.eks_add_on_fulfillment_option

        return {
            "eksAddOnFulfillmentOption": aws_sdk_marketplace_discovery.types.eks_add_on_fulfillment_option.serialize_json(
                value["eksAddOnFulfillmentOption"]
            )
        }
    elif "ec2ImageBuilderComponentFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option

        return {
            "ec2ImageBuilderComponentFulfillmentOption": aws_sdk_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option.serialize_json(
                value["ec2ImageBuilderComponentFulfillmentOption"]
            )
        }
    elif "dataExchangeFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.data_exchange_fulfillment_option

        return {
            "dataExchangeFulfillmentOption": aws_sdk_marketplace_discovery.types.data_exchange_fulfillment_option.serialize_json(
                value["dataExchangeFulfillmentOption"]
            )
        }
    elif "professionalServicesFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.professional_services_fulfillment_option

        return {
            "professionalServicesFulfillmentOption": aws_sdk_marketplace_discovery.types.professional_services_fulfillment_option.serialize_json(
                value["professionalServicesFulfillmentOption"]
            )
        }
    elif "saasFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.saas_fulfillment_option

        return {
            "saasFulfillmentOption": aws_sdk_marketplace_discovery.types.saas_fulfillment_option.serialize_json(
                value["saasFulfillmentOption"]
            )
        }
    elif "sageMakerAlgorithmFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option

        return {
            "sageMakerAlgorithmFulfillmentOption": aws_sdk_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option.serialize_json(
                value["sageMakerAlgorithmFulfillmentOption"]
            )
        }
    elif "sageMakerModelFulfillmentOption" in value:
        import aws_sdk_marketplace_discovery.types.sage_maker_model_fulfillment_option

        return {
            "sageMakerModelFulfillmentOption": aws_sdk_marketplace_discovery.types.sage_maker_model_fulfillment_option.serialize_json(
                value["sageMakerModelFulfillmentOption"]
            )
        }
    else:
        raise SerializationError("FulfillmentOption: no variant present")


def deserialize_json(data: dict) -> FulfillmentOption:
    if "amazonMachineImageFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.amazon_machine_image_fulfillment_option

        return {
            "amazonMachineImageFulfillmentOption": aws_sdk_marketplace_discovery.types.amazon_machine_image_fulfillment_option.deserialize_json(
                data["amazonMachineImageFulfillmentOption"]
            )
        }
    elif "apiFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.api_fulfillment_option

        return {
            "apiFulfillmentOption": aws_sdk_marketplace_discovery.types.api_fulfillment_option.deserialize_json(
                data["apiFulfillmentOption"]
            )
        }
    elif "cloudFormationFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.cloud_formation_fulfillment_option

        return {
            "cloudFormationFulfillmentOption": aws_sdk_marketplace_discovery.types.cloud_formation_fulfillment_option.deserialize_json(
                data["cloudFormationFulfillmentOption"]
            )
        }
    elif "containerFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.container_fulfillment_option

        return {
            "containerFulfillmentOption": aws_sdk_marketplace_discovery.types.container_fulfillment_option.deserialize_json(
                data["containerFulfillmentOption"]
            )
        }
    elif "helmFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.helm_fulfillment_option

        return {
            "helmFulfillmentOption": aws_sdk_marketplace_discovery.types.helm_fulfillment_option.deserialize_json(
                data["helmFulfillmentOption"]
            )
        }
    elif "eksAddOnFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.eks_add_on_fulfillment_option

        return {
            "eksAddOnFulfillmentOption": aws_sdk_marketplace_discovery.types.eks_add_on_fulfillment_option.deserialize_json(
                data["eksAddOnFulfillmentOption"]
            )
        }
    elif "ec2ImageBuilderComponentFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option

        return {
            "ec2ImageBuilderComponentFulfillmentOption": aws_sdk_marketplace_discovery.types.ec2_image_builder_component_fulfillment_option.deserialize_json(
                data["ec2ImageBuilderComponentFulfillmentOption"]
            )
        }
    elif "dataExchangeFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.data_exchange_fulfillment_option

        return {
            "dataExchangeFulfillmentOption": aws_sdk_marketplace_discovery.types.data_exchange_fulfillment_option.deserialize_json(
                data["dataExchangeFulfillmentOption"]
            )
        }
    elif "professionalServicesFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.professional_services_fulfillment_option

        return {
            "professionalServicesFulfillmentOption": aws_sdk_marketplace_discovery.types.professional_services_fulfillment_option.deserialize_json(
                data["professionalServicesFulfillmentOption"]
            )
        }
    elif "saasFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.saas_fulfillment_option

        return {
            "saasFulfillmentOption": aws_sdk_marketplace_discovery.types.saas_fulfillment_option.deserialize_json(
                data["saasFulfillmentOption"]
            )
        }
    elif "sageMakerAlgorithmFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option

        return {
            "sageMakerAlgorithmFulfillmentOption": aws_sdk_marketplace_discovery.types.sage_maker_algorithm_fulfillment_option.deserialize_json(
                data["sageMakerAlgorithmFulfillmentOption"]
            )
        }
    elif "sageMakerModelFulfillmentOption" in data:
        import aws_sdk_marketplace_discovery.types.sage_maker_model_fulfillment_option

        return {
            "sageMakerModelFulfillmentOption": aws_sdk_marketplace_discovery.types.sage_maker_model_fulfillment_option.deserialize_json(
                data["sageMakerModelFulfillmentOption"]
            )
        }
    else:
        raise DeserializationError("FulfillmentOption: no recognized variant key")
