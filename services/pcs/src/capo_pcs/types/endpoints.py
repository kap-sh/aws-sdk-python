"""Generated from Smithy shape ``com.amazonaws.pcs#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.endpoint

Endpoints: TypeAlias = list["capo_pcs.types.endpoint.Endpoint"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Endpoints) -> list:
    import capo_pcs.types.endpoint

    out: list = []
    for item in value:
        out.append(capo_pcs.types.endpoint.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Endpoints:
    import capo_pcs.types.endpoint

    out: Endpoints = []
    for item in data:
        out.append(capo_pcs.types.endpoint.deserialize_aws_json_1_0(item))
    return out
