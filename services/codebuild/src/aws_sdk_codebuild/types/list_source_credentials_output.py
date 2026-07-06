"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSourceCredentialsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.source_credentials_infos


class ListSourceCredentialsOutput(TypedDict, closed=True):
    source_credentials_infos: NotRequired[
        "aws_sdk_codebuild.types.source_credentials_infos.SourceCredentialsInfos"
    ]
    """<p> A list of <code>SourceCredentialsInfo</code> objects. Each <code>SourceCredentialsInfo</code> object includes the authentication type, token ARN, and type of source provider for one set of credentials. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSourceCredentialsOutput) -> dict:
    out: dict = {}
    if "source_credentials_infos" in value:
        import aws_sdk_codebuild.types.source_credentials_infos

        out["sourceCredentialsInfos"] = (
            aws_sdk_codebuild.types.source_credentials_infos.serialize_aws_json_1_1(
                value["source_credentials_infos"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSourceCredentialsOutput:
    out: ListSourceCredentialsOutput = {}  # type: ignore[typeddict-item]
    if "sourceCredentialsInfos" in data:
        import aws_sdk_codebuild.types.source_credentials_infos

        out["source_credentials_infos"] = (
            aws_sdk_codebuild.types.source_credentials_infos.deserialize_aws_json_1_1(
                data["sourceCredentialsInfos"]
            )
        )
    return out
