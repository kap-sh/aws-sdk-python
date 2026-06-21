"""Generated from Smithy shape ``com.amazonaws.eventbridge#ApiDestinationHttpMethod``."""

from typing import Literal, TypeAlias, cast

ApiDestinationHttpMethod: TypeAlias = Literal[
    "POST",
    "GET",
    "HEAD",
    "OPTIONS",
    "PUT",
    "PATCH",
    "DELETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApiDestinationHttpMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApiDestinationHttpMethod:
    return cast(ApiDestinationHttpMethod, data)
