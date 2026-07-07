"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateOutpostResolverResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.outpost_resolver


class CreateOutpostResolverResponse(TypedDict, closed=True):
    outpost_resolver: NotRequired[
        "aws_sdk_route53resolver.types.outpost_resolver.OutpostResolver"
    ]
    """<p>Information about the <code>CreateOutpostResolver</code> request, including the status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOutpostResolverResponse) -> dict:
    out: dict = {}
    if "outpost_resolver" in value:
        import aws_sdk_route53resolver.types.outpost_resolver

        out["OutpostResolver"] = (
            aws_sdk_route53resolver.types.outpost_resolver.serialize_aws_json_1_1(
                value["outpost_resolver"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOutpostResolverResponse:
    out: CreateOutpostResolverResponse = {}  # type: ignore[typeddict-item]
    if "OutpostResolver" in data:
        import aws_sdk_route53resolver.types.outpost_resolver

        out["outpost_resolver"] = (
            aws_sdk_route53resolver.types.outpost_resolver.deserialize_aws_json_1_1(
                data["OutpostResolver"]
            )
        )
    return out
