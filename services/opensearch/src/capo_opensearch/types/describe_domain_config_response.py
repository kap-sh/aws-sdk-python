"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.domain_config


class DescribeDomainConfigResponse(TypedDict, closed=True):
    domain_config: "capo_opensearch.types.domain_config.DomainConfig"
    """<p>Container for the configuration of the OpenSearch Service domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainConfigResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.domain_config

    out["DomainConfig"] = capo_opensearch.types.domain_config.serialize_json(
        value["domain_config"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDomainConfigResponse:
    out: DescribeDomainConfigResponse = {}  # type: ignore[typeddict-item]
    if "DomainConfig" in data:
        import capo_opensearch.types.domain_config

        out["domain_config"] = capo_opensearch.types.domain_config.deserialize_json(
            data["DomainConfig"]
        )
    else:
        raise DeserializationError(
            "DescribeDomainConfigResponse.domain_config required"
        )
    return out
