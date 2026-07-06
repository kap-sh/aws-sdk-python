"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SecurityConfigurationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.authorization_configuration


class SecurityConfigurationData(TypedDict, closed=True):
    authorization_configuration: NotRequired[
        "aws_sdk_emr_containers.types.authorization_configuration.AuthorizationConfiguration"
    ]
    """<p>Authorization-related configuration input for the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityConfigurationData) -> dict:
    out: dict = {}
    if "authorization_configuration" in value:
        import aws_sdk_emr_containers.types.authorization_configuration

        out["authorizationConfiguration"] = (
            aws_sdk_emr_containers.types.authorization_configuration.serialize_json(
                value["authorization_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityConfigurationData:
    out: SecurityConfigurationData = {}  # type: ignore[typeddict-item]
    if "authorizationConfiguration" in data:
        import aws_sdk_emr_containers.types.authorization_configuration

        out["authorization_configuration"] = (
            aws_sdk_emr_containers.types.authorization_configuration.deserialize_json(
                data["authorizationConfiguration"]
            )
        )
    return out
