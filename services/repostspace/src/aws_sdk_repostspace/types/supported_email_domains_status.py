"""Generated from Smithy shape ``com.amazonaws.repostspace#SupportedEmailDomainsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.allowed_domains_list
    import aws_sdk_repostspace.types.feature_enable_status


class SupportedEmailDomainsStatus(TypedDict):
    enabled: NotRequired[
        "aws_sdk_repostspace.types.feature_enable_status.FeatureEnableStatus"
    ]
    """<p/>"""
    allowed_domains: NotRequired[
        "aws_sdk_repostspace.types.allowed_domains_list.AllowedDomainsList"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportedEmailDomainsStatus) -> dict:
    out: dict = {}
    if "enabled" in value:
        import aws_sdk_repostspace.types.feature_enable_status

        out["enabled"] = aws_sdk_repostspace.types.feature_enable_status.serialize_json(
            value["enabled"]
        )
    if "allowed_domains" in value:
        import aws_sdk_repostspace.types.allowed_domains_list

        out["allowedDomains"] = (
            aws_sdk_repostspace.types.allowed_domains_list.serialize_json(
                value["allowed_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> SupportedEmailDomainsStatus:
    out: SupportedEmailDomainsStatus = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        import aws_sdk_repostspace.types.feature_enable_status

        out["enabled"] = (
            aws_sdk_repostspace.types.feature_enable_status.deserialize_json(
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
