"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListGlobalResolversOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.global_resolvers


class ListGlobalResolversOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    global_resolvers: (
        "aws_sdk_route53globalresolver.types.global_resolvers.GlobalResolvers"
    )
    """<p>Paginated list of Global Resolvers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGlobalResolversOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_route53globalresolver.types.global_resolvers

    out["globalResolvers"] = (
        aws_sdk_route53globalresolver.types.global_resolvers.serialize_json(
            value["global_resolvers"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListGlobalResolversOutput:
    out: ListGlobalResolversOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "globalResolvers" in data:
        import aws_sdk_route53globalresolver.types.global_resolvers

        out["global_resolvers"] = (
            aws_sdk_route53globalresolver.types.global_resolvers.deserialize_json(
                data["globalResolvers"]
            )
        )
    else:
        raise DeserializationError(
            "ListGlobalResolversOutput.global_resolvers required"
        )
    return out
