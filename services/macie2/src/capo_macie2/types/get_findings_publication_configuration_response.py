"""Generated from Smithy shape ``com.amazonaws.macie2#GetFindingsPublicationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.security_hub_configuration


class GetFindingsPublicationConfigurationResponse(TypedDict, closed=True):
    security_hub_configuration: NotRequired[
        "capo_macie2.types.security_hub_configuration.SecurityHubConfiguration"
    ]
    """<p>The configuration settings that determine which findings are published to Security Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsPublicationConfigurationResponse) -> dict:
    out: dict = {}
    if "security_hub_configuration" in value:
        import capo_macie2.types.security_hub_configuration

        out["securityHubConfiguration"] = (
            capo_macie2.types.security_hub_configuration.serialize_json(
                value["security_hub_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFindingsPublicationConfigurationResponse:
    out: GetFindingsPublicationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "securityHubConfiguration" in data:
        import capo_macie2.types.security_hub_configuration

        out["security_hub_configuration"] = (
            capo_macie2.types.security_hub_configuration.deserialize_json(
                data["securityHubConfiguration"]
            )
        )
    return out
