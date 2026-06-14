"""Generated from Smithy shape ``com.amazonaws.sagemaker#GitConfigForUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.secret_arn


class GitConfigForUpdate(TypedDict):
    secret_arn: NotRequired["aws_sdk_sagemaker.types.secret_arn.SecretArn"]
    r"""<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of <code>AWSCURRENT</code> and must be in the following format:</p> <p> <code>{\"username\": <i>UserName</i>, \"password\": <i>Password</i>}</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitConfigForUpdate) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GitConfigForUpdate:
    out: GitConfigForUpdate = {}  # type: ignore[typeddict-item]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    return out
