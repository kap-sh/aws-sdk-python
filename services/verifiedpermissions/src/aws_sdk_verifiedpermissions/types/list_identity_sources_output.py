"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListIdentitySourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.identity_sources
    import aws_sdk_verifiedpermissions.types.next_token


class ListIdentitySourcesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_verifiedpermissions.types.next_token.NextToken"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""
    identity_sources: (
        "aws_sdk_verifiedpermissions.types.identity_sources.IdentitySources"
    )
    """<p>The list of identity sources stored in the specified policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListIdentitySourcesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_verifiedpermissions.types.identity_sources

    out["identitySources"] = (
        aws_sdk_verifiedpermissions.types.identity_sources.serialize_aws_json_1_0(
            value["identity_sources"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListIdentitySourcesOutput:
    out: ListIdentitySourcesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "identitySources" in data:
        import aws_sdk_verifiedpermissions.types.identity_sources

        out["identity_sources"] = (
            aws_sdk_verifiedpermissions.types.identity_sources.deserialize_aws_json_1_0(
                data["identitySources"]
            )
        )
    else:
        raise DeserializationError(
            "ListIdentitySourcesOutput.identity_sources required"
        )
    return out
