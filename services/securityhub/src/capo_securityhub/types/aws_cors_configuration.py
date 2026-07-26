"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCorsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string_list


class AwsCorsConfiguration(TypedDict, closed=True):
    allow_origins: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The allowed origins for CORS requests.</p>"""
    allow_credentials: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the CORS request includes credentials.</p>"""
    expose_headers: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The exposed headers for CORS requests.</p>"""
    max_age: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of seconds for which the browser caches preflight request results.</p>"""
    allow_methods: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The allowed methods for CORS requests.</p>"""
    allow_headers: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The allowed headers for CORS requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCorsConfiguration) -> dict:
    out: dict = {}
    if "allow_origins" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AllowOrigins"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["allow_origins"]
            )
        )
    if "allow_credentials" in value:
        out["AllowCredentials"] = value["allow_credentials"]
    if "expose_headers" in value:
        import capo_securityhub.types.non_empty_string_list

        out["ExposeHeaders"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["expose_headers"]
            )
        )
    if "max_age" in value:
        out["MaxAge"] = value["max_age"]
    if "allow_methods" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AllowMethods"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["allow_methods"]
            )
        )
    if "allow_headers" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AllowHeaders"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["allow_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCorsConfiguration:
    out: AwsCorsConfiguration = {}  # type: ignore[typeddict-item]
    if "AllowOrigins" in data:
        import capo_securityhub.types.non_empty_string_list

        out["allow_origins"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AllowOrigins"]
            )
        )
    if "AllowCredentials" in data:
        out["allow_credentials"] = data["AllowCredentials"]
    if "ExposeHeaders" in data:
        import capo_securityhub.types.non_empty_string_list

        out["expose_headers"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["ExposeHeaders"]
            )
        )
    if "MaxAge" in data:
        out["max_age"] = data["MaxAge"]
    if "AllowMethods" in data:
        import capo_securityhub.types.non_empty_string_list

        out["allow_methods"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AllowMethods"]
            )
        )
    if "AllowHeaders" in data:
        import capo_securityhub.types.non_empty_string_list

        out["allow_headers"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AllowHeaders"]
            )
        )
    return out
