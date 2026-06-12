"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DNSViews``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.dns_view_summary

DNSViews: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.dns_view_summary.DNSViewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DNSViews) -> list:
    import aws_sdk_route53globalresolver.types.dns_view_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.dns_view_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DNSViews:
    import aws_sdk_route53globalresolver.types.dns_view_summary

    out: DNSViews = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.dns_view_summary.deserialize_json(item)
        )
    return out
