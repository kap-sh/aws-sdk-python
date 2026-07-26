"""Generated from Smithy shape ``com.amazonaws.glue#AuthenticationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.authentication_type

AuthenticationTypes: TypeAlias = list[
    "capo_glue.types.authentication_type.AuthenticationType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationTypes) -> list:
    import capo_glue.types.authentication_type

    out: list = []
    for item in value:
        out.append(capo_glue.types.authentication_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AuthenticationTypes:
    import capo_glue.types.authentication_type

    out: AuthenticationTypes = []
    for item in data:
        out.append(capo_glue.types.authentication_type.deserialize_aws_json_1_1(item))
    return out
