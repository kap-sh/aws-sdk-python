"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainInformationContainer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.aws_domain_information


class DomainInformationContainer(TypedDict, closed=True):
    aws_domain_information: NotRequired[
        "capo_opensearch.types.aws_domain_information.AWSDomainInformation"
    ]
    """<p>Information about an Amazon OpenSearch Service domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainInformationContainer) -> dict:
    out: dict = {}
    if "aws_domain_information" in value:
        import capo_opensearch.types.aws_domain_information

        out["AWSDomainInformation"] = (
            capo_opensearch.types.aws_domain_information.serialize_json(
                value["aws_domain_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainInformationContainer:
    out: DomainInformationContainer = {}  # type: ignore[typeddict-item]
    if "AWSDomainInformation" in data:
        import capo_opensearch.types.aws_domain_information

        out["aws_domain_information"] = (
            capo_opensearch.types.aws_domain_information.deserialize_json(
                data["AWSDomainInformation"]
            )
        )
    return out
