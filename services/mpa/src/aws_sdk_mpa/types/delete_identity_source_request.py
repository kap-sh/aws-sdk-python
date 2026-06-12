"""Generated from Smithy shape ``com.amazonaws.mpa#DeleteIdentitySourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.string


class DeleteIdentitySourceRequest(TypedDict):
    identity_source_arn: "aws_sdk_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for identity source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdentitySourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIdentitySourceRequest:
    out: DeleteIdentitySourceRequest = {}  # type: ignore[typeddict-item]
    return out
