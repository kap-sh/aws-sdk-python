"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantResourcesFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The key used to filter tenant resources. Currently, the only supported filter key is <code>RESOURCE_TYPE</code>.</p>"""
ListTenantResourcesFilterKey: TypeAlias = Literal["RESOURCE_TYPE",]


# --- restJson1 ser/de ---
def serialize_json(value: ListTenantResourcesFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ListTenantResourcesFilterKey:
    return cast(ListTenantResourcesFilterKey, data)
