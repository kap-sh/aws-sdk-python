"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetOutpostResolverResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.outpost_resolver


class GetOutpostResolverResponse(TypedDict, closed=True):
    outpost_resolver: NotRequired[
        "capo_route53resolver.types.outpost_resolver.OutpostResolver"
    ]
    """<p>Information about the <code>GetOutpostResolver</code> request, including the status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOutpostResolverResponse) -> dict:
    out: dict = {}
    if "outpost_resolver" in value:
        import capo_route53resolver.types.outpost_resolver

        out["OutpostResolver"] = (
            capo_route53resolver.types.outpost_resolver.serialize_aws_json_1_1(
                value["outpost_resolver"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOutpostResolverResponse:
    out: GetOutpostResolverResponse = {}  # type: ignore[typeddict-item]
    if "OutpostResolver" in data:
        import capo_route53resolver.types.outpost_resolver

        out["outpost_resolver"] = (
            capo_route53resolver.types.outpost_resolver.deserialize_aws_json_1_1(
                data["OutpostResolver"]
            )
        )
    return out
