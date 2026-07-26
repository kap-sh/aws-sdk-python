"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomFieldsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.custom_fields_filter
    import capo_connectcases.types.custom_fields_filter_list
    import capo_connectcases.types.field_filter


class _CustomFieldsFilter_field(TypedDict, closed=True):
    field: "capo_connectcases.types.field_filter.FieldFilter"


_CustomFieldsFilter_not = TypedDict(
    "_CustomFieldsFilter_not",
    {
        "not": "capo_connectcases.types.custom_fields_filter.CustomFieldsFilter",
    },
    closed=True,
)


class _CustomFieldsFilter_andAll(TypedDict, closed=True):
    andAll: "capo_connectcases.types.custom_fields_filter_list.CustomFieldsFilterList"


class _CustomFieldsFilter_orAll(TypedDict, closed=True):
    orAll: "capo_connectcases.types.custom_fields_filter_list.CustomFieldsFilterList"


CustomFieldsFilter: TypeAlias = (
    _CustomFieldsFilter_field
    | _CustomFieldsFilter_not
    | _CustomFieldsFilter_andAll
    | _CustomFieldsFilter_orAll
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomFieldsFilter) -> dict:
    if "field" in value:
        import capo_connectcases.types.field_filter

        return {
            "field": capo_connectcases.types.field_filter.serialize_json(value["field"])
        }
    elif "not" in value:
        import capo_connectcases.types.custom_fields_filter

        return {
            "not": capo_connectcases.types.custom_fields_filter.serialize_json(
                value["not"]
            )
        }
    elif "andAll" in value:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "andAll": capo_connectcases.types.custom_fields_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "orAll": capo_connectcases.types.custom_fields_filter_list.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("CustomFieldsFilter: no variant present")


def deserialize_json(data: dict) -> CustomFieldsFilter:
    if "field" in data:
        import capo_connectcases.types.field_filter

        return {
            "field": capo_connectcases.types.field_filter.deserialize_json(
                data["field"]
            )
        }
    elif "not" in data:
        import capo_connectcases.types.custom_fields_filter

        return {
            "not": capo_connectcases.types.custom_fields_filter.deserialize_json(
                data["not"]
            )
        }
    elif "andAll" in data:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "andAll": capo_connectcases.types.custom_fields_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif "orAll" in data:
        import capo_connectcases.types.custom_fields_filter_list

        return {
            "orAll": capo_connectcases.types.custom_fields_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    else:
        raise DeserializationError("CustomFieldsFilter: no recognized variant key")
