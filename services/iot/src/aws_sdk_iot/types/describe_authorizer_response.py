"""Generated from Smithy shape ``com.amazonaws.iot#DescribeAuthorizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_description


class DescribeAuthorizerResponse(TypedDict, closed=True):
    authorizer_description: NotRequired[
        "aws_sdk_iot.types.authorizer_description.AuthorizerDescription"
    ]
    """<p>The authorizer description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuthorizerResponse) -> dict:
    out: dict = {}
    if "authorizer_description" in value:
        import aws_sdk_iot.types.authorizer_description

        out["authorizerDescription"] = (
            aws_sdk_iot.types.authorizer_description.serialize_json(
                value["authorizer_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAuthorizerResponse:
    out: DescribeAuthorizerResponse = {}  # type: ignore[typeddict-item]
    if "authorizerDescription" in data:
        import aws_sdk_iot.types.authorizer_description

        out["authorizer_description"] = (
            aws_sdk_iot.types.authorizer_description.deserialize_json(
                data["authorizerDescription"]
            )
        )
    return out
