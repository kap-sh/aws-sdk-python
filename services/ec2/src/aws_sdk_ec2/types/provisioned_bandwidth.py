"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionedBandwidth``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string


class ProvisionedBandwidth(TypedDict):
    provision_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>Reserved.</p>"""
    provisioned: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    request_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>Reserved.</p>"""
    requested: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProvisionedBandwidth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "provision_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["provision_time"], pairs, f"{prefix}.ProvisionTime"
        )
    if "provisioned" in value:
        pairs.append((f"{prefix}.Provisioned", str(value["provisioned"])))
    if "request_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["request_time"], pairs, f"{prefix}.RequestTime"
        )
    if "requested" in value:
        pairs.append((f"{prefix}.Requested", str(value["requested"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_ec2_query(el: Element) -> ProvisionedBandwidth:
    out: ProvisionedBandwidth = {}  # type: ignore[typeddict-item]
    child_provision_time = el.find("ProvisionTime")
    if child_provision_time is not None:
        import aws_sdk_ec2.types.date_time

        out["provision_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_provision_time
        )
    child_provisioned = el.find("Provisioned")
    if child_provisioned is not None:
        out["provisioned"] = str(child_provisioned.text or "")
    child_request_time = el.find("RequestTime")
    if child_request_time is not None:
        import aws_sdk_ec2.types.date_time

        out["request_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_request_time
        )
    child_requested = el.find("Requested")
    if child_requested is not None:
        out["requested"] = str(child_requested.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
