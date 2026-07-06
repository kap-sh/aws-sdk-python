"""Generated from Smithy shape ``com.amazonaws.appsync#CreateResolverResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resolver


class CreateResolverResponse(TypedDict, closed=True):
    resolver: NotRequired["aws_sdk_appsync.types.resolver.Resolver"]
    """<p>The <code>Resolver</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResolverResponse) -> dict:
    out: dict = {}
    if "resolver" in value:
        import aws_sdk_appsync.types.resolver

        out["resolver"] = aws_sdk_appsync.types.resolver.serialize_json(
            value["resolver"]
        )
    return out


def deserialize_json(data: dict) -> CreateResolverResponse:
    out: CreateResolverResponse = {}  # type: ignore[typeddict-item]
    if "resolver" in data:
        import aws_sdk_appsync.types.resolver

        out["resolver"] = aws_sdk_appsync.types.resolver.deserialize_json(
            data["resolver"]
        )
    return out
