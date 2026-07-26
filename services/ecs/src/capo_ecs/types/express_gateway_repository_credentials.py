"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayRepositoryCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class ExpressGatewayRepositoryCredentials(TypedDict, closed=True):
    credentials_parameter: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secret containing the private repository credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayRepositoryCredentials) -> dict:
    out: dict = {}
    if "credentials_parameter" in value:
        out["credentialsParameter"] = value["credentials_parameter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayRepositoryCredentials:
    out: ExpressGatewayRepositoryCredentials = {}  # type: ignore[typeddict-item]
    if "credentialsParameter" in data:
        out["credentials_parameter"] = data["credentialsParameter"]
    return out
