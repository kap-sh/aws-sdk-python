"""Generated from Smithy shape ``com.amazonaws.repostspace#SupportedEmailDomainsParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.allowed_domains_list
    import aws_sdk_repostspace.types.feature_enable_parameter


class SupportedEmailDomainsParameters(TypedDict):
    enabled: NotRequired[
        "aws_sdk_repostspace.types.feature_enable_parameter.FeatureEnableParameter"
    ]
    """<p/>"""
    allowed_domains: NotRequired[
        "aws_sdk_repostspace.types.allowed_domains_list.AllowedDomainsList"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportedEmailDomainsParameters) -> dict:
    out: dict = {}
    if "enabled" in value:
        import aws_sdk_repostspace.types.feature_enable_parameter

        out["enabled"] = (
            aws_sdk_repostspace.types.feature_enable_parameter.serialize_json(
                value["enabled"]
            )
        )
    if "allowed_domains" in value:
        import aws_sdk_repostspace.types.allowed_domains_list

        out["allowedDomains"] = (
            aws_sdk_repostspace.types.allowed_domains_list.serialize_json(
                value["allowed_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> SupportedEmailDomainsParameters:
    out: SupportedEmailDomainsParameters = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        import aws_sdk_repostspace.types.feature_enable_parameter

        out["enabled"] = (
            aws_sdk_repostspace.types.feature_enable_parameter.deserialize_json(
                data["enabled"]
            )
        )
    if "allowedDomains" in data:
        import aws_sdk_repostspace.types.allowed_domains_list

        out["allowed_domains"] = (
            aws_sdk_repostspace.types.allowed_domains_list.deserialize_json(
                data["allowedDomains"]
            )
        )
    return out
