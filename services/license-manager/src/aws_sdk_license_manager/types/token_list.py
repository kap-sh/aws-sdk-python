"""Generated from Smithy shape ``com.amazonaws.licensemanager#TokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.token_data

TokenList: TypeAlias = list["aws_sdk_license_manager.types.token_data.TokenData"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TokenList) -> list:
    import aws_sdk_license_manager.types.token_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.token_data.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TokenList:
    import aws_sdk_license_manager.types.token_data

    out: TokenList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.token_data.deserialize_aws_json_1_1(item)
        )
    return out
