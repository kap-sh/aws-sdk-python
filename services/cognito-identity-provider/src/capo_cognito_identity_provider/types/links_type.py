"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LinksType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.language_id_type
    import capo_cognito_identity_provider.types.link_url_type

LinksType: TypeAlias = dict[
    "capo_cognito_identity_provider.types.language_id_type.LanguageIdType",
    "capo_cognito_identity_provider.types.link_url_type.LinkUrlType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LinksType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LinksType:
    out: LinksType = {}
    for key, value in data.items():
        out[key] = value
    return out
