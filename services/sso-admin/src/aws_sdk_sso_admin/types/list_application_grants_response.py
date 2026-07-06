"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationGrantsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.grants
    import aws_sdk_sso_admin.types.token


class ListApplicationGrantsResponse(TypedDict, closed=True):
    grants: "aws_sdk_sso_admin.types.grants.Grants"
    """<p>An array list of structures that describe the requested grants.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationGrantsResponse) -> dict:
    out: dict = {}
    import aws_sdk_sso_admin.types.grants

    out["Grants"] = aws_sdk_sso_admin.types.grants.serialize_aws_json_1_1(
        value["grants"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationGrantsResponse:
    out: ListApplicationGrantsResponse = {}  # type: ignore[typeddict-item]
    if "Grants" in data:
        import aws_sdk_sso_admin.types.grants

        out["grants"] = aws_sdk_sso_admin.types.grants.deserialize_aws_json_1_1(
            data["Grants"]
        )
    else:
        raise DeserializationError("ListApplicationGrantsResponse.grants required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
