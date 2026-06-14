"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRootResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.credentials
    import aws_sdk_sts.types.source_identity_type


class AssumeRootResponse(TypedDict):
    credentials: NotRequired["aws_sdk_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    source_identity: NotRequired[
        "aws_sdk_sts.types.source_identity_type.sourceIdentityType"
    ]
    r"""<p>The source identity specified by the principal that is calling the <code>AssumeRoot</code> operation.</p> <p>You can use the <code>aws:SourceIdentity</code> condition key to control access based on the value of source identity. For more information about using source identity, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html\">Monitor and control actions taken with assumed roles</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRootResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "credentials" in value:
        import aws_sdk_sts.types.credentials

        aws_sdk_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{prefix}.Credentials"
        )
    if "source_identity" in value:
        pairs.append((f"{prefix}.SourceIdentity", str(value["source_identity"])))


def deserialize_query(el: Element) -> AssumeRootResponse:
    out: AssumeRootResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import aws_sdk_sts.types.credentials

        out["credentials"] = aws_sdk_sts.types.credentials.deserialize_query(
            child_credentials
        )
    child_source_identity = el.find("SourceIdentity")
    if child_source_identity is not None:
        out["source_identity"] = str(child_source_identity.text or "")
    return out
