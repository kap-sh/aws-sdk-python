"""Generated from Smithy shape ``com.amazonaws.cloudsearch#CreateDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_status


class CreateDomainResponse(TypedDict):
    domain_status: NotRequired["aws_sdk_cloudsearch.types.domain_status.DomainStatus"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDomainResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "domain_status" in value:
        import aws_sdk_cloudsearch.types.domain_status

        aws_sdk_cloudsearch.types.domain_status.serialize_query(
            value["domain_status"], pairs, f"{prefix}.DomainStatus"
        )


def deserialize_query(el: Element) -> CreateDomainResponse:
    out: CreateDomainResponse = {}  # type: ignore[typeddict-item]
    child_domain_status = el.find("DomainStatus")
    if child_domain_status is not None:
        import aws_sdk_cloudsearch.types.domain_status

        out["domain_status"] = (
            aws_sdk_cloudsearch.types.domain_status.deserialize_query(
                child_domain_status
            )
        )
    return out
