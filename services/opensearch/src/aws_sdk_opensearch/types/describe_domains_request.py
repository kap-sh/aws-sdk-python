"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name_list


class DescribeDomainsRequest(TypedDict):
    domain_names: "aws_sdk_opensearch.types.domain_name_list.DomainNameList"
    """<p>Array of OpenSearch Service domain names that you want information about. You must specify at least one domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainsRequest) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.domain_name_list

    out["DomainNames"] = aws_sdk_opensearch.types.domain_name_list.serialize_json(
        value["domain_names"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDomainsRequest:
    out: DescribeDomainsRequest = {}  # type: ignore[typeddict-item]
    if "DomainNames" in data:
        import aws_sdk_opensearch.types.domain_name_list

        out["domain_names"] = (
            aws_sdk_opensearch.types.domain_name_list.deserialize_json(
                data["DomainNames"]
            )
        )
    else:
        raise DeserializationError("DescribeDomainsRequest.domain_names required")
    return out
