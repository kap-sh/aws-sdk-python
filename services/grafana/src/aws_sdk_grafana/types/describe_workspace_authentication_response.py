"""Generated from Smithy shape ``com.amazonaws.grafana#DescribeWorkspaceAuthenticationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_grafana.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_grafana.types.authentication_description

class DescribeWorkspaceAuthenticationResponse(TypedDict):
    authentication: "aws_sdk_grafana.types.authentication_description.AuthenticationDescription"
    """<p>A structure containing information about the authentication methods used in the workspace.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceAuthenticationResponse) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.authentication_description
    out["authentication"] = aws_sdk_grafana.types.authentication_description.serialize_json(value["authentication"])
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceAuthenticationResponse:
    out: DescribeWorkspaceAuthenticationResponse = {}  # type: ignore[typeddict-item]
    if "authentication" in data:
        import aws_sdk_grafana.types.authentication_description
        out["authentication"] = aws_sdk_grafana.types.authentication_description.deserialize_json(data["authentication"])
    else:
        raise DeserializationError("DescribeWorkspaceAuthenticationResponse.authentication required")
    return out