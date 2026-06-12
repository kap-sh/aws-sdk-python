"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ExplicitAuthFlowsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.explicit_auth_flows_type

ExplicitAuthFlowsListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.explicit_auth_flows_type.ExplicitAuthFlowsType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplicitAuthFlowsListType) -> list:
    import aws_sdk_cognito_identity_provider.types.explicit_auth_flows_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.explicit_auth_flows_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExplicitAuthFlowsListType:
    import aws_sdk_cognito_identity_provider.types.explicit_auth_flows_type

    out: ExplicitAuthFlowsListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.explicit_auth_flows_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
