"""Generated from Smithy shape ``com.amazonaws.glue#GetSecurityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.security_configuration


class GetSecurityConfigurationResponse(TypedDict, closed=True):
    security_configuration: NotRequired[
        "capo_glue.types.security_configuration.SecurityConfiguration"
    ]
    """<p>The requested security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSecurityConfigurationResponse) -> dict:
    out: dict = {}
    if "security_configuration" in value:
        import capo_glue.types.security_configuration

        out["SecurityConfiguration"] = (
            capo_glue.types.security_configuration.serialize_aws_json_1_1(
                value["security_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSecurityConfigurationResponse:
    out: GetSecurityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "SecurityConfiguration" in data:
        import capo_glue.types.security_configuration

        out["security_configuration"] = (
            capo_glue.types.security_configuration.deserialize_aws_json_1_1(
                data["SecurityConfiguration"]
            )
        )
    return out
