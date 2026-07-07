"""Generated from Smithy shape ``com.amazonaws.rds#EnableHttpEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class EnableHttpEndpointRequest(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the DB cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableHttpEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> EnableHttpEndpointRequest:
    out: EnableHttpEndpointRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out
