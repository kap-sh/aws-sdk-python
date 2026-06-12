"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_filter_name
    import aws_sdk_ses.types.receipt_ip_filter


class ReceiptFilter(TypedDict):
    name: "aws_sdk_ses.types.receipt_filter_name.ReceiptFilterName"
    """<p>The name of the IP address filter. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""
    ip_filter: "aws_sdk_ses.types.receipt_ip_filter.ReceiptIpFilter"
    """<p>A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Name", str(value["name"])))
    import aws_sdk_ses.types.receipt_ip_filter

    aws_sdk_ses.types.receipt_ip_filter.serialize_query(
        value["ip_filter"], pairs, f"{prefix}.IpFilter"
    )


def deserialize_query(el: Element) -> ReceiptFilter:
    out: ReceiptFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("ReceiptFilter.name required")
    child_ip_filter = el.find("IpFilter")
    if child_ip_filter is not None:
        import aws_sdk_ses.types.receipt_ip_filter

        out["ip_filter"] = aws_sdk_ses.types.receipt_ip_filter.deserialize_query(
            child_ip_filter
        )
    else:
        raise DeserializationError("ReceiptFilter.ip_filter required")
    return out
