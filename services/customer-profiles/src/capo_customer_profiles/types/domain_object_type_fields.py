"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DomainObjectTypeFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.domain_object_type_field
    import capo_customer_profiles.types.domain_object_type_field_name

DomainObjectTypeFields: TypeAlias = dict[
    "capo_customer_profiles.types.domain_object_type_field_name.DomainObjectTypeFieldName",
    "capo_customer_profiles.types.domain_object_type_field.DomainObjectTypeField",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DomainObjectTypeFields) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_customer_profiles.types.domain_object_type_field

        out[key] = capo_customer_profiles.types.domain_object_type_field.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> DomainObjectTypeFields:
    out: DomainObjectTypeFields = {}
    for key, value in data.items():
        import capo_customer_profiles.types.domain_object_type_field

        out[key] = (
            capo_customer_profiles.types.domain_object_type_field.deserialize_json(
                value
            )
        )
    return out
