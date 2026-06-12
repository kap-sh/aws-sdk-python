"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeScalingParametersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name


class DescribeScalingParametersRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeScalingParametersRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))


def deserialize_query(el: Element) -> DescribeScalingParametersRequest:
    out: DescribeScalingParametersRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError(
            "DescribeScalingParametersRequest.domain_name required"
        )
    return out
