"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxConnectionStringResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.signed_kx_connection_string


class GetKxConnectionStringResponse(TypedDict):
    signed_connection_string: NotRequired[
        "aws_sdk_finspace.types.signed_kx_connection_string.SignedKxConnectionString"
    ]
    """<p>The signed connection string that you can use to connect to clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxConnectionStringResponse) -> dict:
    out: dict = {}
    if "signed_connection_string" in value:
        out["signedConnectionString"] = value["signed_connection_string"]
    return out


def deserialize_json(data: dict) -> GetKxConnectionStringResponse:
    out: GetKxConnectionStringResponse = {}  # type: ignore[typeddict-item]
    if "signedConnectionString" in data:
        out["signed_connection_string"] = data["signedConnectionString"]
    return out
