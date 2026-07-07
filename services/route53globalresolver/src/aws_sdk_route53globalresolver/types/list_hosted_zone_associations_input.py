"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListHostedZoneAssociationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_arn


class ListHostedZoneAssociationsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""
    resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>Amazon Resource Name (ARN) of the DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHostedZoneAssociationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHostedZoneAssociationsInput:
    out: ListHostedZoneAssociationsInput = {}  # type: ignore[typeddict-item]
    return out
