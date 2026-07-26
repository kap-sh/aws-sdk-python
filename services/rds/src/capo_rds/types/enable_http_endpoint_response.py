"""Generated from Smithy shape ``com.amazonaws.rds#EnableHttpEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.string


class EnableHttpEndpointResponse(TypedDict, closed=True):
    resource_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN of the DB cluster.</p>"""
    http_endpoint_enabled: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the HTTP endpoint is enabled or disabled for the DB cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableHttpEndpointResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "http_endpoint_enabled" in value:
        pairs.append(
            (
                f"{prefix}.HttpEndpointEnabled",
                "true" if value["http_endpoint_enabled"] else "false",
            )
        )


def deserialize_query(el: Element) -> EnableHttpEndpointResponse:
    out: EnableHttpEndpointResponse = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_http_endpoint_enabled = el.find("HttpEndpointEnabled")
    if child_http_endpoint_enabled is not None:
        out["http_endpoint_enabled"] = (
            child_http_endpoint_enabled.text or ""
        ).lower() == "true"
    return out
