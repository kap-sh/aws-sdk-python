"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateOutpostResolverResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.outpost_resolver


class UpdateOutpostResolverResponse(TypedDict):
    outpost_resolver: NotRequired[
        "aws_sdk_route53resolver.types.outpost_resolver.OutpostResolver"
    ]
    """<p>The response to an <code>UpdateOutpostResolver</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOutpostResolverResponse) -> dict:
    out: dict = {}
    if "outpost_resolver" in value:
        import aws_sdk_route53resolver.types.outpost_resolver

        out["OutpostResolver"] = (
            aws_sdk_route53resolver.types.outpost_resolver.serialize_aws_json_1_1(
                value["outpost_resolver"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOutpostResolverResponse:
    out: UpdateOutpostResolverResponse = {}  # type: ignore[typeddict-item]
    if "OutpostResolver" in data:
        import aws_sdk_route53resolver.types.outpost_resolver

        out["outpost_resolver"] = (
            aws_sdk_route53resolver.types.outpost_resolver.deserialize_aws_json_1_1(
                data["OutpostResolver"]
            )
        )
    return out
