"""Generated from Smithy shape ``com.amazonaws.rds#IPRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class IPRange(TypedDict):
    status: NotRequired["aws_sdk_rds.types.string.String"]
    r"""<p>The status of the IP range. Status can be \"authorizing\", \"authorized\", \"revoking\", and \"revoked\".</p>"""
    cidrip: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The IP range.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: IPRange, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "cidrip" in value:
        pairs.append((f"{prefix}.CIDRIP", str(value["cidrip"])))


def deserialize_query(el: Element) -> IPRange:
    out: IPRange = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_cidrip = el.find("CIDRIP")
    if child_cidrip is not None:
        out["cidrip"] = str(child_cidrip.text or "")
    return out
