"""Generated from Smithy shape ``com.amazonaws.mediatailor#SecretsManagerAccessTokenConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class SecretsManagerAccessTokenConfiguration(TypedDict, closed=True):
    header_name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The name of the HTTP header used to supply the access token in requests to the source location.</p>"""
    secret_arn: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the access token.</p>"""
    secret_string_key: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    r"""<p>The AWS Secrets Manager <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html#SecretsManager-CreateSecret-request-SecretString.html\">SecretString</a> key associated with the access token. MediaTailor uses the key to look up SecretString key and value pair containing the access token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerAccessTokenConfiguration) -> dict:
    out: dict = {}
    if "header_name" in value:
        out["HeaderName"] = value["header_name"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "secret_string_key" in value:
        out["SecretStringKey"] = value["secret_string_key"]
    return out


def deserialize_json(data: dict) -> SecretsManagerAccessTokenConfiguration:
    out: SecretsManagerAccessTokenConfiguration = {}  # type: ignore[typeddict-item]
    if "HeaderName" in data:
        out["header_name"] = data["HeaderName"]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "SecretStringKey" in data:
        out["secret_string_key"] = data["SecretStringKey"]
    return out
