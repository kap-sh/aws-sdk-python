"""Generated from Smithy shape ``com.amazonaws.appsync#DeleteGraphqlApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class DeleteGraphqlApiRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGraphqlApiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGraphqlApiRequest:
    out: DeleteGraphqlApiRequest = {}  # type: ignore[typeddict-item]
    return out
