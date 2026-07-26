"""Generated from Smithy shape ``com.amazonaws.lightsail#HeaderEnum``."""

from typing import Literal, TypeAlias, cast

HeaderEnum: TypeAlias = Literal[
    "Accept",
    "Accept-Charset",
    "Accept-Datetime",
    "Accept-Encoding",
    "Accept-Language",
    "Authorization",
    "CloudFront-Forwarded-Proto",
    "CloudFront-Is-Desktop-Viewer",
    "CloudFront-Is-Mobile-Viewer",
    "CloudFront-Is-SmartTV-Viewer",
    "CloudFront-Is-Tablet-Viewer",
    "CloudFront-Viewer-Country",
    "Host",
    "Origin",
    "Referer",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HeaderEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HeaderEnum:
    return cast(HeaderEnum, data)
