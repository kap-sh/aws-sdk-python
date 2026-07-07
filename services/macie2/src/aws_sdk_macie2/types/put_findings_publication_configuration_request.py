"""Generated from Smithy shape ``com.amazonaws.macie2#PutFindingsPublicationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.security_hub_configuration


class PutFindingsPublicationConfigurationRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    security_hub_configuration: NotRequired[
        "aws_sdk_macie2.types.security_hub_configuration.SecurityHubConfiguration"
    ]
    """<p>The configuration settings that determine which findings to publish to Security Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFindingsPublicationConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "security_hub_configuration" in value:
        import aws_sdk_macie2.types.security_hub_configuration

        out["securityHubConfiguration"] = (
            aws_sdk_macie2.types.security_hub_configuration.serialize_json(
                value["security_hub_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutFindingsPublicationConfigurationRequest:
    out: PutFindingsPublicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "securityHubConfiguration" in data:
        import aws_sdk_macie2.types.security_hub_configuration

        out["security_hub_configuration"] = (
            aws_sdk_macie2.types.security_hub_configuration.deserialize_json(
                data["securityHubConfiguration"]
            )
        )
    return out
