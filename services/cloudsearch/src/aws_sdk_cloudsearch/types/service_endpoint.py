"""Generated from Smithy shape ``com.amazonaws.cloudsearch#ServiceEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.service_url


class ServiceEndpoint(TypedDict, closed=True):
    endpoint: NotRequired["aws_sdk_cloudsearch.types.service_url.ServiceUrl"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceEndpoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "endpoint" in value:
        pairs.append((f"{prefix}.Endpoint", str(value["endpoint"])))


def deserialize_query(el: Element) -> ServiceEndpoint:
    out: ServiceEndpoint = {}  # type: ignore[typeddict-item]
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    return out
