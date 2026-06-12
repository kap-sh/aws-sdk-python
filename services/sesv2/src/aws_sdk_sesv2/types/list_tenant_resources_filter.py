"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantResourcesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.list_tenant_resources_filter_key
    import aws_sdk_sesv2.types.list_tenant_resources_filter_value

ListTenantResourcesFilter: TypeAlias = dict[
    "aws_sdk_sesv2.types.list_tenant_resources_filter_key.ListTenantResourcesFilterKey",
    "aws_sdk_sesv2.types.list_tenant_resources_filter_value.ListTenantResourcesFilterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ListTenantResourcesFilter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sesv2.types.list_tenant_resources_filter_key

        out[
            aws_sdk_sesv2.types.list_tenant_resources_filter_key.serialize_json(key)
        ] = value
    return out


def deserialize_json(data: dict) -> ListTenantResourcesFilter:
    out: ListTenantResourcesFilter = {}
    for key, value in data.items():
        import aws_sdk_sesv2.types.list_tenant_resources_filter_key

        out[
            aws_sdk_sesv2.types.list_tenant_resources_filter_key.deserialize_json(key)
        ] = value
    return out
