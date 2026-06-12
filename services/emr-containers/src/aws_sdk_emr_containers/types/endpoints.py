"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.endpoint

Endpoints: TypeAlias = list["aws_sdk_emr_containers.types.endpoint.Endpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: Endpoints) -> list:
    import aws_sdk_emr_containers.types.endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_emr_containers.types.endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> Endpoints:
    import aws_sdk_emr_containers.types.endpoint

    out: Endpoints = []
    for item in data:
        out.append(aws_sdk_emr_containers.types.endpoint.deserialize_json(item))
    return out
