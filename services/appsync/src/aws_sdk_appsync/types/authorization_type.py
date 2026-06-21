"""Generated from Smithy shape ``com.amazonaws.appsync#AuthorizationType``."""

from typing import Literal, TypeAlias, cast

AuthorizationType: TypeAlias = Literal["AWS_IAM",]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationType:
    return cast(AuthorizationType, data)
