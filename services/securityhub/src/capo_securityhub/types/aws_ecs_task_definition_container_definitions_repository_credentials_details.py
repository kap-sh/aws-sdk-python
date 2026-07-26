"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails(
    TypedDict, closed=True
):
    credentials_parameter: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the secret that contains the private repository credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails,
) -> dict:
    out: dict = {}
    if "credentials_parameter" in value:
        out["CredentialsParameter"] = value["credentials_parameter"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails = {}  # type: ignore[typeddict-item]
    if "CredentialsParameter" in data:
        out["credentials_parameter"] = data["CredentialsParameter"]
    return out
