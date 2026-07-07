"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateContainerServiceRegistryLoginRequest``."""

from typing_extensions import TypedDict


class CreateContainerServiceRegistryLoginRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerServiceRegistryLoginRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerServiceRegistryLoginRequest:
    out: CreateContainerServiceRegistryLoginRequest = {}  # type: ignore[typeddict-item]
    return out
