"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListDNSViewsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.dns_views


class ListDNSViewsOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    dns_views: "aws_sdk_route53globalresolver.types.dns_views.DNSViews"
    """<p>An array of information about the DNS views, such as whether DNSSEC is enabled, creation time, etc.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDNSViewsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_route53globalresolver.types.dns_views

    out["dnsViews"] = aws_sdk_route53globalresolver.types.dns_views.serialize_json(
        value["dns_views"]
    )
    return out


def deserialize_json(data: dict) -> ListDNSViewsOutput:
    out: ListDNSViewsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "dnsViews" in data:
        import aws_sdk_route53globalresolver.types.dns_views

        out["dns_views"] = (
            aws_sdk_route53globalresolver.types.dns_views.deserialize_json(
                data["dnsViews"]
            )
        )
    else:
        raise DeserializationError("ListDNSViewsOutput.dns_views required")
    return out
