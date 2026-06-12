"""Generated from Smithy shape ``com.amazonaws.appsync#GetDomainNameResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.domain_name_config


class GetDomainNameResponse(TypedDict):
    domain_name_config: NotRequired[
        "aws_sdk_appsync.types.domain_name_config.DomainNameConfig"
    ]
    """<p>The configuration for the <code>DomainName</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNameResponse) -> dict:
    out: dict = {}
    if "domain_name_config" in value:
        import aws_sdk_appsync.types.domain_name_config

        out["domainNameConfig"] = (
            aws_sdk_appsync.types.domain_name_config.serialize_json(
                value["domain_name_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDomainNameResponse:
    out: GetDomainNameResponse = {}  # type: ignore[typeddict-item]
    if "domainNameConfig" in data:
        import aws_sdk_appsync.types.domain_name_config

        out["domain_name_config"] = (
            aws_sdk_appsync.types.domain_name_config.deserialize_json(
                data["domainNameConfig"]
            )
        )
    return out
