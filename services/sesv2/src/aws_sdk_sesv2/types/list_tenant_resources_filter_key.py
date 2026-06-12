"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantResourcesFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The key used to filter tenant resources. Currently, the only supported filter key is <code>RESOURCE_TYPE</code>.</p>"""
ListTenantResourcesFilterKey: TypeAlias = Literal["RESOURCE_TYPE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RESOURCE_TYPE",))


def serialize_json(value: ListTenantResourcesFilterKey) -> str:
    return value


def deserialize_json(data: str) -> ListTenantResourcesFilterKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListTenantResourcesFilterKey value: {data!r}"
        )
    return cast(ListTenantResourcesFilterKey, data)
