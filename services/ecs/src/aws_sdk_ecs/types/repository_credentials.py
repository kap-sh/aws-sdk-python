"""Generated from Smithy shape ``com.amazonaws.ecs#RepositoryCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class RepositoryCredentials(TypedDict, closed=True):
    credentials_parameter: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the secret containing the private repository credentials.</p> <note> <p>When you use the Amazon ECS API, CLI, or Amazon Web Services SDK, if the secret exists in the same Region as the task that you're launching then you can use either the full ARN or the name of the secret. When you use the Amazon Web Services Management Console, you must specify the full ARN of the secret.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryCredentials) -> dict:
    out: dict = {}
    out["credentialsParameter"] = value["credentials_parameter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryCredentials:
    out: RepositoryCredentials = {}  # type: ignore[typeddict-item]
    if "credentialsParameter" in data:
        out["credentials_parameter"] = data["credentialsParameter"]
    else:
        raise DeserializationError(
            "RepositoryCredentials.credentials_parameter required"
        )
    return out
