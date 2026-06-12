"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCorsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsCorsConfiguration(TypedDict):
    allow_origins: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The allowed origins for CORS requests.</p>"""
    allow_credentials: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the CORS request includes credentials.</p>"""
    expose_headers: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The exposed headers for CORS requests.</p>"""
    max_age: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of seconds for which the browser caches preflight request results.</p>"""
    allow_methods: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The allowed methods for CORS requests.</p>"""
    allow_headers: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The allowed headers for CORS requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCorsConfiguration) -> dict:
    out: dict = {}
    if "allow_origins" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["AllowOrigins"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["allow_origins"]
            )
        )
    if "allow_credentials" in value:
        out["AllowCredentials"] = value["allow_credentials"]
    if "expose_headers" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["ExposeHeaders"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["expose_headers"]
            )
        )
    if "max_age" in value:
        out["MaxAge"] = value["max_age"]
    if "allow_methods" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["AllowMethods"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["allow_methods"]
            )
        )
    if "allow_headers" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["AllowHeaders"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["allow_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCorsConfiguration:
    out: AwsCorsConfiguration = {}  # type: ignore[typeddict-item]
    if "AllowOrigins" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["allow_origins"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["AllowOrigins"]
            )
        )
    if "AllowCredentials" in data:
        out["allow_credentials"] = data["AllowCredentials"]
    if "ExposeHeaders" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["expose_headers"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["ExposeHeaders"]
            )
        )
    if "MaxAge" in data:
        out["max_age"] = data["MaxAge"]
    if "AllowMethods" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["allow_methods"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["AllowMethods"]
            )
        )
    if "AllowHeaders" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["allow_headers"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["AllowHeaders"]
            )
        )
    return out
