"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationAccessScopesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.scopes
    import aws_sdk_sso_admin.types.token


class ListApplicationAccessScopesResponse(TypedDict):
    scopes: "aws_sdk_sso_admin.types.scopes.Scopes"
    """<p>An array list of access scopes and their authorized targets that are associated with the application.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationAccessScopesResponse) -> dict:
    out: dict = {}
    import aws_sdk_sso_admin.types.scopes

    out["Scopes"] = aws_sdk_sso_admin.types.scopes.serialize_aws_json_1_1(
        value["scopes"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationAccessScopesResponse:
    out: ListApplicationAccessScopesResponse = {}  # type: ignore[typeddict-item]
    if "Scopes" in data:
        import aws_sdk_sso_admin.types.scopes

        out["scopes"] = aws_sdk_sso_admin.types.scopes.deserialize_aws_json_1_1(
            data["Scopes"]
        )
    else:
        raise DeserializationError(
            "ListApplicationAccessScopesResponse.scopes required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
