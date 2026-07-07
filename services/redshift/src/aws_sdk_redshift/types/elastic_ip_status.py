"""Generated from Smithy shape ``com.amazonaws.redshift#ElasticIpStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class ElasticIpStatus(TypedDict, closed=True):
    elastic_ip: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The elastic IP (EIP) address for the cluster.</p>"""
    status: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The status of the elastic IP (EIP) address.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ElasticIpStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "elastic_ip" in value:
        pairs.append((f"{prefix}.ElasticIp", str(value["elastic_ip"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> ElasticIpStatus:
    out: ElasticIpStatus = {}  # type: ignore[typeddict-item]
    child_elastic_ip = el.find("ElasticIp")
    if child_elastic_ip is not None:
        out["elastic_ip"] = str(child_elastic_ip.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
