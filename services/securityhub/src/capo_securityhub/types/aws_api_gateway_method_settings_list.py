"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayMethodSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_api_gateway_method_settings

AwsApiGatewayMethodSettingsList: TypeAlias = list[
    "capo_securityhub.types.aws_api_gateway_method_settings.AwsApiGatewayMethodSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayMethodSettingsList) -> list:
    import capo_securityhub.types.aws_api_gateway_method_settings

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_api_gateway_method_settings.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsApiGatewayMethodSettingsList:
    import capo_securityhub.types.aws_api_gateway_method_settings

    out: AwsApiGatewayMethodSettingsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_api_gateway_method_settings.deserialize_json(
                item
            )
        )
    return out
