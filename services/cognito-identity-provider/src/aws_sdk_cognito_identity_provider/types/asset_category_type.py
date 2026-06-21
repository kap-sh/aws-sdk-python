"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssetCategoryType``."""

from typing import Literal, TypeAlias, cast

AssetCategoryType: TypeAlias = Literal[
    "FAVICON_ICO",
    "FAVICON_SVG",
    "EMAIL_GRAPHIC",
    "SMS_GRAPHIC",
    "AUTH_APP_GRAPHIC",
    "PASSWORD_GRAPHIC",
    "PASSKEY_GRAPHIC",
    "PAGE_HEADER_LOGO",
    "PAGE_HEADER_BACKGROUND",
    "PAGE_FOOTER_LOGO",
    "PAGE_FOOTER_BACKGROUND",
    "PAGE_BACKGROUND",
    "FORM_BACKGROUND",
    "FORM_LOGO",
    "IDP_BUTTON_ICON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetCategoryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssetCategoryType:
    return cast(AssetCategoryType, data)
