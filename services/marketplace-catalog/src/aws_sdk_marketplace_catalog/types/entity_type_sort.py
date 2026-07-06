"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntityTypeSort``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_marketplace_catalog.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.ami_product_sort
    import aws_sdk_marketplace_catalog.types.container_product_sort
    import aws_sdk_marketplace_catalog.types.data_product_sort
    import aws_sdk_marketplace_catalog.types.machine_learning_product_sort
    import aws_sdk_marketplace_catalog.types.offer_set_sort
    import aws_sdk_marketplace_catalog.types.offer_sort
    import aws_sdk_marketplace_catalog.types.resale_authorization_sort
    import aws_sdk_marketplace_catalog.types.saa_s_product_sort


class _EntityTypeSort_DataProductSort(TypedDict, closed=True):
    DataProductSort: (
        "aws_sdk_marketplace_catalog.types.data_product_sort.DataProductSort"
    )


class _EntityTypeSort_SaaSProductSort(TypedDict, closed=True):
    SaaSProductSort: (
        "aws_sdk_marketplace_catalog.types.saa_s_product_sort.SaaSProductSort"
    )


class _EntityTypeSort_AmiProductSort(TypedDict, closed=True):
    AmiProductSort: "aws_sdk_marketplace_catalog.types.ami_product_sort.AmiProductSort"


class _EntityTypeSort_OfferSort(TypedDict, closed=True):
    OfferSort: "aws_sdk_marketplace_catalog.types.offer_sort.OfferSort"


class _EntityTypeSort_ContainerProductSort(TypedDict, closed=True):
    ContainerProductSort: (
        "aws_sdk_marketplace_catalog.types.container_product_sort.ContainerProductSort"
    )


class _EntityTypeSort_ResaleAuthorizationSort(TypedDict, closed=True):
    ResaleAuthorizationSort: "aws_sdk_marketplace_catalog.types.resale_authorization_sort.ResaleAuthorizationSort"


class _EntityTypeSort_MachineLearningProductSort(TypedDict, closed=True):
    MachineLearningProductSort: "aws_sdk_marketplace_catalog.types.machine_learning_product_sort.MachineLearningProductSort"


class _EntityTypeSort_OfferSetSort(TypedDict, closed=True):
    OfferSetSort: "aws_sdk_marketplace_catalog.types.offer_set_sort.OfferSetSort"


EntityTypeSort: TypeAlias = (
    _EntityTypeSort_DataProductSort
    | _EntityTypeSort_SaaSProductSort
    | _EntityTypeSort_AmiProductSort
    | _EntityTypeSort_OfferSort
    | _EntityTypeSort_ContainerProductSort
    | _EntityTypeSort_ResaleAuthorizationSort
    | _EntityTypeSort_MachineLearningProductSort
    | _EntityTypeSort_OfferSetSort
)


# --- restJson1 ser/de ---
def serialize_json(value: EntityTypeSort) -> dict:
    if "DataProductSort" in value:
        import aws_sdk_marketplace_catalog.types.data_product_sort

        return {
            "DataProductSort": aws_sdk_marketplace_catalog.types.data_product_sort.serialize_json(
                value["DataProductSort"]
            )
        }
    elif "SaaSProductSort" in value:
        import aws_sdk_marketplace_catalog.types.saa_s_product_sort

        return {
            "SaaSProductSort": aws_sdk_marketplace_catalog.types.saa_s_product_sort.serialize_json(
                value["SaaSProductSort"]
            )
        }
    elif "AmiProductSort" in value:
        import aws_sdk_marketplace_catalog.types.ami_product_sort

        return {
            "AmiProductSort": aws_sdk_marketplace_catalog.types.ami_product_sort.serialize_json(
                value["AmiProductSort"]
            )
        }
    elif "OfferSort" in value:
        import aws_sdk_marketplace_catalog.types.offer_sort

        return {
            "OfferSort": aws_sdk_marketplace_catalog.types.offer_sort.serialize_json(
                value["OfferSort"]
            )
        }
    elif "ContainerProductSort" in value:
        import aws_sdk_marketplace_catalog.types.container_product_sort

        return {
            "ContainerProductSort": aws_sdk_marketplace_catalog.types.container_product_sort.serialize_json(
                value["ContainerProductSort"]
            )
        }
    elif "ResaleAuthorizationSort" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_sort

        return {
            "ResaleAuthorizationSort": aws_sdk_marketplace_catalog.types.resale_authorization_sort.serialize_json(
                value["ResaleAuthorizationSort"]
            )
        }
    elif "MachineLearningProductSort" in value:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_sort

        return {
            "MachineLearningProductSort": aws_sdk_marketplace_catalog.types.machine_learning_product_sort.serialize_json(
                value["MachineLearningProductSort"]
            )
        }
    elif "OfferSetSort" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_sort

        return {
            "OfferSetSort": aws_sdk_marketplace_catalog.types.offer_set_sort.serialize_json(
                value["OfferSetSort"]
            )
        }
    else:
        raise SerializationError("EntityTypeSort: no variant present")


def deserialize_json(data: dict) -> EntityTypeSort:
    if "DataProductSort" in data:
        import aws_sdk_marketplace_catalog.types.data_product_sort

        return {
            "DataProductSort": aws_sdk_marketplace_catalog.types.data_product_sort.deserialize_json(
                data["DataProductSort"]
            )
        }
    elif "SaaSProductSort" in data:
        import aws_sdk_marketplace_catalog.types.saa_s_product_sort

        return {
            "SaaSProductSort": aws_sdk_marketplace_catalog.types.saa_s_product_sort.deserialize_json(
                data["SaaSProductSort"]
            )
        }
    elif "AmiProductSort" in data:
        import aws_sdk_marketplace_catalog.types.ami_product_sort

        return {
            "AmiProductSort": aws_sdk_marketplace_catalog.types.ami_product_sort.deserialize_json(
                data["AmiProductSort"]
            )
        }
    elif "OfferSort" in data:
        import aws_sdk_marketplace_catalog.types.offer_sort

        return {
            "OfferSort": aws_sdk_marketplace_catalog.types.offer_sort.deserialize_json(
                data["OfferSort"]
            )
        }
    elif "ContainerProductSort" in data:
        import aws_sdk_marketplace_catalog.types.container_product_sort

        return {
            "ContainerProductSort": aws_sdk_marketplace_catalog.types.container_product_sort.deserialize_json(
                data["ContainerProductSort"]
            )
        }
    elif "ResaleAuthorizationSort" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_sort

        return {
            "ResaleAuthorizationSort": aws_sdk_marketplace_catalog.types.resale_authorization_sort.deserialize_json(
                data["ResaleAuthorizationSort"]
            )
        }
    elif "MachineLearningProductSort" in data:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_sort

        return {
            "MachineLearningProductSort": aws_sdk_marketplace_catalog.types.machine_learning_product_sort.deserialize_json(
                data["MachineLearningProductSort"]
            )
        }
    elif "OfferSetSort" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_sort

        return {
            "OfferSetSort": aws_sdk_marketplace_catalog.types.offer_set_sort.deserialize_json(
                data["OfferSetSort"]
            )
        }
    else:
        raise DeserializationError("EntityTypeSort: no recognized variant key")
