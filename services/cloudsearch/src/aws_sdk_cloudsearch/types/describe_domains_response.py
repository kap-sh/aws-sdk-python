"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_status_list


class DescribeDomainsResponse(TypedDict, closed=True):
    domain_status_list: "aws_sdk_cloudsearch.types.domain_status_list.DomainStatusList"


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDomainsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.domain_status_list

    aws_sdk_cloudsearch.types.domain_status_list.serialize_query(
        value["domain_status_list"], pairs, f"{prefix}.DomainStatusList"
    )


def deserialize_query(el: Element) -> DescribeDomainsResponse:
    out: DescribeDomainsResponse = {}  # type: ignore[typeddict-item]
    child_domain_status_list = el.find("DomainStatusList")
    if child_domain_status_list is not None:
        import aws_sdk_cloudsearch.types.domain_status_list

        out["domain_status_list"] = (
            aws_sdk_cloudsearch.types.domain_status_list.deserialize_query(
                child_domain_status_list
            )
        )
    else:
        raise DeserializationError(
            "DescribeDomainsResponse.domain_status_list required"
        )
    return out
