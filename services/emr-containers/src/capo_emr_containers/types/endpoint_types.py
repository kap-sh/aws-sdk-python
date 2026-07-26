"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EndpointTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.endpoint_type

EndpointTypes: TypeAlias = list["capo_emr_containers.types.endpoint_type.EndpointType"]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> EndpointTypes:
    return list(data)
