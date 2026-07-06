"""Generated from Smithy shape ``com.amazonaws.organizations#CancelHandshakeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.handshake


class CancelHandshakeResponse(TypedDict, closed=True):
    handshake: NotRequired["aws_sdk_organizations.types.handshake.Handshake"]
    """<p>A <code>Handshake</code> object. Contains for the handshake that you canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelHandshakeResponse) -> dict:
    out: dict = {}
    if "handshake" in value:
        import aws_sdk_organizations.types.handshake

        out["Handshake"] = aws_sdk_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelHandshakeResponse:
    out: CancelHandshakeResponse = {}  # type: ignore[typeddict-item]
    if "Handshake" in data:
        import aws_sdk_organizations.types.handshake

        out["handshake"] = (
            aws_sdk_organizations.types.handshake.deserialize_aws_json_1_1(
                data["Handshake"]
            )
        )
    return out
