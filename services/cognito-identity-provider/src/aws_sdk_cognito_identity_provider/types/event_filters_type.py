"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventFiltersType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.event_filter_type

EventFiltersType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.event_filter_type.EventFilterType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventFiltersType) -> list:
    import aws_sdk_cognito_identity_provider.types.event_filter_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.event_filter_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventFiltersType:
    import aws_sdk_cognito_identity_provider.types.event_filter_type

    out: EventFiltersType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.event_filter_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
