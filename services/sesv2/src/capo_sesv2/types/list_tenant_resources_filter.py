"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantResourcesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.list_tenant_resources_filter_key
    import capo_sesv2.types.list_tenant_resources_filter_value

ListTenantResourcesFilter: TypeAlias = dict[
    "capo_sesv2.types.list_tenant_resources_filter_key.ListTenantResourcesFilterKey",
    "capo_sesv2.types.list_tenant_resources_filter_value.ListTenantResourcesFilterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ListTenantResourcesFilter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sesv2.types.list_tenant_resources_filter_key

        out[capo_sesv2.types.list_tenant_resources_filter_key.serialize_json(key)] = (
            value
        )
    return out


def deserialize_json(data: dict) -> ListTenantResourcesFilter:
    out: ListTenantResourcesFilter = {}
    for key, value in data.items():
        import capo_sesv2.types.list_tenant_resources_filter_key

        out[capo_sesv2.types.list_tenant_resources_filter_key.deserialize_json(key)] = (
            value
        )
    return out
