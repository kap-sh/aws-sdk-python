"""Generated from Smithy shape ``com.amazonaws.rds#DisableHttpEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DisableHttpEndpointRequest(TypedDict, closed=True):
    resource_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the DB cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DisableHttpEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> DisableHttpEndpointRequest:
    out: DisableHttpEndpointRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out
