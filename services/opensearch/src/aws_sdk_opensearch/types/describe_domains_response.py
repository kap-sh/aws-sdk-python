"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_status_list


class DescribeDomainsResponse(TypedDict, closed=True):
    domain_status_list: "aws_sdk_opensearch.types.domain_status_list.DomainStatusList"
    """<p>The status of the requested domains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainsResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.domain_status_list

    out["DomainStatusList"] = (
        aws_sdk_opensearch.types.domain_status_list.serialize_json(
            value["domain_status_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeDomainsResponse:
    out: DescribeDomainsResponse = {}  # type: ignore[typeddict-item]
    if "DomainStatusList" in data:
        import aws_sdk_opensearch.types.domain_status_list

        out["domain_status_list"] = (
            aws_sdk_opensearch.types.domain_status_list.deserialize_json(
                data["DomainStatusList"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDomainsResponse.domain_status_list required"
        )
    return out
