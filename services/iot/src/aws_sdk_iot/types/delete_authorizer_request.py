"""Generated from Smithy shape ``com.amazonaws.iot#DeleteAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_name


class DeleteAuthorizerRequest(TypedDict, closed=True):
    authorizer_name: "aws_sdk_iot.types.authorizer_name.AuthorizerName"
    """<p>The name of the authorizer to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAuthorizerRequest:
    out: DeleteAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
