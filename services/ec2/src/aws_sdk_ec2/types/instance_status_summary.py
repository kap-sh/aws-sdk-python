"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_details_list
    import aws_sdk_ec2.types.summary_status


class InstanceStatusSummary(TypedDict):
    details: NotRequired[
        "aws_sdk_ec2.types.instance_status_details_list.InstanceStatusDetailsList"
    ]
    """<p>The system instance health or application instance health.</p>"""
    status: NotRequired["aws_sdk_ec2.types.summary_status.SummaryStatus"]
    """<p>The status.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStatusSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "details" in value:
        import aws_sdk_ec2.types.instance_status_details_list

        aws_sdk_ec2.types.instance_status_details_list.serialize_ec2_query(
            value["details"], pairs, f"{prefix}.Details"
        )
    if "status" in value:
        import aws_sdk_ec2.types.summary_status

        aws_sdk_ec2.types.summary_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> InstanceStatusSummary:
    out: InstanceStatusSummary = {}  # type: ignore[typeddict-item]
    if el.find("Details") is not None:
        import aws_sdk_ec2.types.instance_status_details_list

        out["details"] = (
            aws_sdk_ec2.types.instance_status_details_list.deserialize_ec2_query(
                el, "Details"
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.summary_status

        out["status"] = aws_sdk_ec2.types.summary_status.deserialize_ec2_query(
            child_status
        )
    return out
