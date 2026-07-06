"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_marketplace_catalog.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.ami_product_filters
    import aws_sdk_marketplace_catalog.types.container_product_filters
    import aws_sdk_marketplace_catalog.types.data_product_filters
    import aws_sdk_marketplace_catalog.types.machine_learning_product_filters
    import aws_sdk_marketplace_catalog.types.offer_filters
    import aws_sdk_marketplace_catalog.types.offer_set_filters
    import aws_sdk_marketplace_catalog.types.resale_authorization_filters
    import aws_sdk_marketplace_catalog.types.saa_s_product_filters


class _EntityTypeFilters_DataProductFilters(TypedDict, closed=True):
    DataProductFilters: (
        "aws_sdk_marketplace_catalog.types.data_product_filters.DataProductFilters"
    )


class _EntityTypeFilters_SaaSProductFilters(TypedDict, closed=True):
    SaaSProductFilters: (
        "aws_sdk_marketplace_catalog.types.saa_s_product_filters.SaaSProductFilters"
    )


class _EntityTypeFilters_AmiProductFilters(TypedDict, closed=True):
    AmiProductFilters: (
        "aws_sdk_marketplace_catalog.types.ami_product_filters.AmiProductFilters"
    )


class _EntityTypeFilters_OfferFilters(TypedDict, closed=True):
    OfferFilters: "aws_sdk_marketplace_catalog.types.offer_filters.OfferFilters"


class _EntityTypeFilters_ContainerProductFilters(TypedDict, closed=True):
    ContainerProductFilters: "aws_sdk_marketplace_catalog.types.container_product_filters.ContainerProductFilters"


class _EntityTypeFilters_ResaleAuthorizationFilters(TypedDict, closed=True):
    ResaleAuthorizationFilters: "aws_sdk_marketplace_catalog.types.resale_authorization_filters.ResaleAuthorizationFilters"


class _EntityTypeFilters_MachineLearningProductFilters(TypedDict, closed=True):
    MachineLearningProductFilters: "aws_sdk_marketplace_catalog.types.machine_learning_product_filters.MachineLearningProductFilters"


class _EntityTypeFilters_OfferSetFilters(TypedDict, closed=True):
    OfferSetFilters: (
        "aws_sdk_marketplace_catalog.types.offer_set_filters.OfferSetFilters"
    )


EntityTypeFilters: TypeAlias = (
    _EntityTypeFilters_DataProductFilters
    | _EntityTypeFilters_SaaSProductFilters
    | _EntityTypeFilters_AmiProductFilters
    | _EntityTypeFilters_OfferFilters
    | _EntityTypeFilters_ContainerProductFilters
    | _EntityTypeFilters_ResaleAuthorizationFilters
    | _EntityTypeFilters_MachineLearningProductFilters
    | _EntityTypeFilters_OfferSetFilters
)


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeFilters) -> dict:
    if "DataProductFilters" in value:
        import aws_sdk_marketplace_catalog.types.data_product_filters

        return {
            "DataProductFilters": aws_sdk_marketplace_catalog.types.data_product_filters.serialize_json(
                value["DataProductFilters"]
            )
        }
    elif "SaaSProductFilters" in value:
        import aws_sdk_marketplace_catalog.types.saa_s_product_filters

        return {
            "SaaSProductFilters": aws_sdk_marketplace_catalog.types.saa_s_product_filters.serialize_json(
                value["SaaSProductFilters"]
            )
        }
    elif "AmiProductFilters" in value:
        import aws_sdk_marketplace_catalog.types.ami_product_filters

        return {
            "AmiProductFilters": aws_sdk_marketplace_catalog.types.ami_product_filters.serialize_json(
                value["AmiProductFilters"]
            )
        }
    elif "OfferFilters" in value:
        import aws_sdk_marketplace_catalog.types.offer_filters

        return {
            "OfferFilters": aws_sdk_marketplace_catalog.types.offer_filters.serialize_json(
                value["OfferFilters"]
            )
        }
    elif "ContainerProductFilters" in value:
        import aws_sdk_marketplace_catalog.types.container_product_filters

        return {
            "ContainerProductFilters": aws_sdk_marketplace_catalog.types.container_product_filters.serialize_json(
                value["ContainerProductFilters"]
            )
        }
    elif "ResaleAuthorizationFilters" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_filters

        return {
            "ResaleAuthorizationFilters": aws_sdk_marketplace_catalog.types.resale_authorization_filters.serialize_json(
                value["ResaleAuthorizationFilters"]
            )
        }
    elif "MachineLearningProductFilters" in value:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_filters

        return {
            "MachineLearningProductFilters": aws_sdk_marketplace_catalog.types.machine_learning_product_filters.serialize_json(
                value["MachineLearningProductFilters"]
            )
        }
    elif "OfferSetFilters" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_filters

        return {
            "OfferSetFilters": aws_sdk_marketplace_catalog.types.offer_set_filters.serialize_json(
                value["OfferSetFilters"]
            )
        }
    else:
        raise SerializationError("EntityTypeFilters: no variant present")


def deserialize_json(data: dict) -> EntityTypeFilters:
    if "DataProductFilters" in data:
        import aws_sdk_marketplace_catalog.types.data_product_filters

        return {
            "DataProductFilters": aws_sdk_marketplace_catalog.types.data_product_filters.deserialize_json(
                data["DataProductFilters"]
            )
        }
    elif "SaaSProductFilters" in data:
        import aws_sdk_marketplace_catalog.types.saa_s_product_filters

        return {
            "SaaSProductFilters": aws_sdk_marketplace_catalog.types.saa_s_product_filters.deserialize_json(
                data["SaaSProductFilters"]
            )
        }
    elif "AmiProductFilters" in data:
        import aws_sdk_marketplace_catalog.types.ami_product_filters

        return {
            "AmiProductFilters": aws_sdk_marketplace_catalog.types.ami_product_filters.deserialize_json(
                data["AmiProductFilters"]
            )
        }
    elif "OfferFilters" in data:
        import aws_sdk_marketplace_catalog.types.offer_filters

        return {
            "OfferFilters": aws_sdk_marketplace_catalog.types.offer_filters.deserialize_json(
                data["OfferFilters"]
            )
        }
    elif "ContainerProductFilters" in data:
        import aws_sdk_marketplace_catalog.types.container_product_filters

        return {
            "ContainerProductFilters": aws_sdk_marketplace_catalog.types.container_product_filters.deserialize_json(
                data["ContainerProductFilters"]
            )
        }
    elif "ResaleAuthorizationFilters" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_filters

        return {
            "ResaleAuthorizationFilters": aws_sdk_marketplace_catalog.types.resale_authorization_filters.deserialize_json(
                data["ResaleAuthorizationFilters"]
            )
        }
    elif "MachineLearningProductFilters" in data:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_filters

        return {
            "MachineLearningProductFilters": aws_sdk_marketplace_catalog.types.machine_learning_product_filters.deserialize_json(
                data["MachineLearningProductFilters"]
            )
        }
    elif "OfferSetFilters" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_filters

        return {
            "OfferSetFilters": aws_sdk_marketplace_catalog.types.offer_set_filters.deserialize_json(
                data["OfferSetFilters"]
            )
        }
    else:
        raise DeserializationError("EntityTypeFilters: no recognized variant key")
