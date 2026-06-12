"""Generated from Smithy shape ``com.amazonaws.appsync#AuthorizationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.authorization_type
    import aws_sdk_appsync.types.aws_iam_config


class AuthorizationConfig(TypedDict):
    authorization_type: "aws_sdk_appsync.types.authorization_type.AuthorizationType"
    """<p>The authorization type that the HTTP endpoint requires.</p> <ul> <li> <p> <b>AWS_IAM</b>: The authorization type is Signature Version 4 (SigV4).</p> </li> </ul>"""
    aws_iam_config: NotRequired["aws_sdk_appsync.types.aws_iam_config.AwsIamConfig"]
    """<p>The Identity and Access Management (IAM) settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationConfig) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.authorization_type

    out["authorizationType"] = aws_sdk_appsync.types.authorization_type.serialize_json(
        value["authorization_type"]
    )
    if "aws_iam_config" in value:
        import aws_sdk_appsync.types.aws_iam_config

        out["awsIamConfig"] = aws_sdk_appsync.types.aws_iam_config.serialize_json(
            value["aws_iam_config"]
        )
    return out


def deserialize_json(data: dict) -> AuthorizationConfig:
    out: AuthorizationConfig = {}  # type: ignore[typeddict-item]
    if "authorizationType" in data:
        import aws_sdk_appsync.types.authorization_type

        out["authorization_type"] = (
            aws_sdk_appsync.types.authorization_type.deserialize_json(
                data["authorizationType"]
            )
        )
    else:
        raise DeserializationError("AuthorizationConfig.authorization_type required")
    if "awsIamConfig" in data:
        import aws_sdk_appsync.types.aws_iam_config

        out["aws_iam_config"] = aws_sdk_appsync.types.aws_iam_config.deserialize_json(
            data["awsIamConfig"]
        )
    return out
