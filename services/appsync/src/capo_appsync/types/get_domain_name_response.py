"""Generated from Smithy shape ``com.amazonaws.appsync#GetDomainNameResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.domain_name_config


class GetDomainNameResponse(TypedDict, closed=True):
    domain_name_config: NotRequired[
        "capo_appsync.types.domain_name_config.DomainNameConfig"
    ]
    """<p>The configuration for the <code>DomainName</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNameResponse) -> dict:
    out: dict = {}
    if "domain_name_config" in value:
        import capo_appsync.types.domain_name_config

        out["domainNameConfig"] = capo_appsync.types.domain_name_config.serialize_json(
            value["domain_name_config"]
        )
    return out


def deserialize_json(data: dict) -> GetDomainNameResponse:
    out: GetDomainNameResponse = {}  # type: ignore[typeddict-item]
    if "domainNameConfig" in data:
        import capo_appsync.types.domain_name_config

        out["domain_name_config"] = (
            capo_appsync.types.domain_name_config.deserialize_json(
                data["domainNameConfig"]
            )
        )
    return out
