"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name_list


class DescribeDomainsRequest(TypedDict, closed=True):
    domain_names: NotRequired[
        "aws_sdk_cloudsearch.types.domain_name_list.DomainNameList"
    ]
    """<p>The names of the domains you want to include in the response.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDomainsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "domain_names" in value:
        import aws_sdk_cloudsearch.types.domain_name_list

        aws_sdk_cloudsearch.types.domain_name_list.serialize_query(
            value["domain_names"], pairs, f"{prefix}.DomainNames"
        )


def deserialize_query(el: Element) -> DescribeDomainsRequest:
    out: DescribeDomainsRequest = {}  # type: ignore[typeddict-item]
    child_domain_names = el.find("DomainNames")
    if child_domain_names is not None:
        import aws_sdk_cloudsearch.types.domain_name_list

        out["domain_names"] = (
            aws_sdk_cloudsearch.types.domain_name_list.deserialize_query(
                child_domain_names
            )
        )
    return out
