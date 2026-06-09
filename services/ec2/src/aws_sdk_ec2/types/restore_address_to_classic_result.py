"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreAddressToClassicResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.status
    import aws_sdk_ec2.types.string


class RestoreAddressToClassicResult(TypedDict):
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Elastic IP address.</p>"""
    status: NotRequired["aws_sdk_ec2.types.status.Status"]
    """<p>The move status for the IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreAddressToClassicResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))
    if "status" in value:
        import aws_sdk_ec2.types.status

        aws_sdk_ec2.types.status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> RestoreAddressToClassicResult:
    out: RestoreAddressToClassicResult = {}  # type: ignore[typeddict-item]
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.status

        out["status"] = aws_sdk_ec2.types.status.deserialize_ec2_query(child_status)
    return out
