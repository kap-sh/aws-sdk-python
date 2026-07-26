"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#OAuthFlowsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.o_auth_flow_type

OAuthFlowsType: TypeAlias = list[
    "capo_cognito_identity_provider.types.o_auth_flow_type.OAuthFlowType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuthFlowsType) -> list:
    import capo_cognito_identity_provider.types.o_auth_flow_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.o_auth_flow_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OAuthFlowsType:
    import capo_cognito_identity_provider.types.o_auth_flow_type

    out: OAuthFlowsType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.o_auth_flow_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
