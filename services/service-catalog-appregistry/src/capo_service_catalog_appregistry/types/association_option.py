"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AssociationOption``."""

from typing import Literal, TypeAlias, cast

AssociationOption: TypeAlias = Literal[
    "APPLY_APPLICATION_TAG",
    "SKIP_APPLICATION_TAG",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationOption) -> str:
    return value


def deserialize_json(data: str) -> AssociationOption:
    return cast(AssociationOption, data)
