"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.endpoint

Endpoints: TypeAlias = list["capo_emr_containers.types.endpoint.Endpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: Endpoints) -> list:
    import capo_emr_containers.types.endpoint

    out: list = []
    for item in value:
        out.append(capo_emr_containers.types.endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> Endpoints:
    import capo_emr_containers.types.endpoint

    out: Endpoints = []
    for item in data:
        out.append(capo_emr_containers.types.endpoint.deserialize_json(item))
    return out
