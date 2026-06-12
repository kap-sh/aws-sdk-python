"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#HttpHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.http_header

HttpHeaderList: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.http_header.HttpHeader"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpHeaderList) -> list:
    import aws_sdk_cognito_identity_provider.types.http_header

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.http_header.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HttpHeaderList:
    import aws_sdk_cognito_identity_provider.types.http_header

    out: HttpHeaderList = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.http_header.deserialize_aws_json_1_1(
                item
            )
        )
    return out
