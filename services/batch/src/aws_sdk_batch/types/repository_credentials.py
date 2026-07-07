"""Generated from Smithy shape ``com.amazonaws.batch#RepositoryCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class RepositoryCredentials(TypedDict, closed=True):
    credentials_parameter: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the secret containing the private repository credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryCredentials) -> dict:
    out: dict = {}
    if "credentials_parameter" in value:
        out["credentialsParameter"] = value["credentials_parameter"]
    return out


def deserialize_json(data: dict) -> RepositoryCredentials:
    out: RepositoryCredentials = {}  # type: ignore[typeddict-item]
    if "credentialsParameter" in data:
        out["credentials_parameter"] = data["credentialsParameter"]
    return out
