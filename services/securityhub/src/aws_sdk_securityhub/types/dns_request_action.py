"""Generated from Smithy shape ``com.amazonaws.securityhub#DnsRequestAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class DnsRequestAction(TypedDict, closed=True):
    domain: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The DNS domain that is associated with the DNS request.</p> <p>Length Constraints: 128.</p>"""
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol that was used for the DNS request.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 64.</p>"""
    blocked: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the DNS request was blocked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsRequestAction) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "blocked" in value:
        out["Blocked"] = value["blocked"]
    return out


def deserialize_json(data: dict) -> DnsRequestAction:
    out: DnsRequestAction = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "Blocked" in data:
        out["blocked"] = data["Blocked"]
    return out
