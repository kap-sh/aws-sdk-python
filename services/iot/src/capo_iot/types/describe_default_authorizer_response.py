"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDefaultAuthorizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.authorizer_description


class DescribeDefaultAuthorizerResponse(TypedDict, closed=True):
    authorizer_description: NotRequired[
        "capo_iot.types.authorizer_description.AuthorizerDescription"
    ]
    """<p>The default authorizer's description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDefaultAuthorizerResponse) -> dict:
    out: dict = {}
    if "authorizer_description" in value:
        import capo_iot.types.authorizer_description

        out["authorizerDescription"] = (
            capo_iot.types.authorizer_description.serialize_json(
                value["authorizer_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDefaultAuthorizerResponse:
    out: DescribeDefaultAuthorizerResponse = {}  # type: ignore[typeddict-item]
    if "authorizerDescription" in data:
        import capo_iot.types.authorizer_description

        out["authorizer_description"] = (
            capo_iot.types.authorizer_description.deserialize_json(
                data["authorizerDescription"]
            )
        )
    return out
