"""Generated from Smithy shape ``com.amazonaws.organizations#ListHandshakesForOrganizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.handshakes
    import aws_sdk_organizations.types.next_token


class ListHandshakesForOrganizationResponse(TypedDict):
    handshakes: NotRequired["aws_sdk_organizations.types.handshakes.Handshakes"]
    """<p>An array of <code>Handshake</code>objects. Contains details for a handshake.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHandshakesForOrganizationResponse) -> dict:
    out: dict = {}
    if "handshakes" in value:
        import aws_sdk_organizations.types.handshakes

        out["Handshakes"] = (
            aws_sdk_organizations.types.handshakes.serialize_aws_json_1_1(
                value["handshakes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHandshakesForOrganizationResponse:
    out: ListHandshakesForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "Handshakes" in data:
        import aws_sdk_organizations.types.handshakes

        out["handshakes"] = (
            aws_sdk_organizations.types.handshakes.deserialize_aws_json_1_1(
                data["Handshakes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
