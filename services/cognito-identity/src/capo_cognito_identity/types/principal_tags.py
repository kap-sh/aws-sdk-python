"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#PrincipalTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.principal_tag_id
    import capo_cognito_identity.types.principal_tag_value

PrincipalTags: TypeAlias = dict[
    "capo_cognito_identity.types.principal_tag_id.PrincipalTagID",
    "capo_cognito_identity.types.principal_tag_value.PrincipalTagValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PrincipalTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> PrincipalTags:
    out: PrincipalTags = {}
    for key, value in data.items():
        out[key] = value
    return out
