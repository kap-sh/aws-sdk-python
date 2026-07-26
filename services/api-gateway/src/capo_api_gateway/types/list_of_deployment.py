"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfDeployment``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.deployment

ListOfDeployment: TypeAlias = list["capo_api_gateway.types.deployment.Deployment"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDeployment) -> list:
    import capo_api_gateway.types.deployment

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfDeployment:
    import capo_api_gateway.types.deployment

    out: ListOfDeployment = []
    for item in data:
        out.append(capo_api_gateway.types.deployment.deserialize_json(item))
    return out
