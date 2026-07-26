"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#Options``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.association_option

Options: TypeAlias = list[
    "capo_service_catalog_appregistry.types.association_option.AssociationOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: Options) -> list:
    import capo_service_catalog_appregistry.types.association_option

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog_appregistry.types.association_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> Options:
    import capo_service_catalog_appregistry.types.association_option

    out: Options = []
    for item in data:
        out.append(
            capo_service_catalog_appregistry.types.association_option.deserialize_json(
                item
            )
        )
    return out
