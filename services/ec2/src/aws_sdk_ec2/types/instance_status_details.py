"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.status_name
    import aws_sdk_ec2.types.status_type


class InstanceStatusDetails(TypedDict, closed=True):
    impaired_since: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time when a status check failed. For an instance that was launched and impaired, this is the time when the instance was launched.</p>"""
    name: NotRequired["aws_sdk_ec2.types.status_name.StatusName"]
    """<p>The type of instance status.</p>"""
    status: NotRequired["aws_sdk_ec2.types.status_type.StatusType"]
    """<p>The status.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "impaired_since" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["impaired_since"], pairs, f"{prefix}.ImpairedSince"
        )
    if "name" in value:
        import aws_sdk_ec2.types.status_name

        aws_sdk_ec2.types.status_name.serialize_ec2_query(
            value["name"], pairs, f"{prefix}.Name"
        )
    if "status" in value:
        import aws_sdk_ec2.types.status_type

        aws_sdk_ec2.types.status_type.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> InstanceStatusDetails:
    out: InstanceStatusDetails = {}  # type: ignore[typeddict-item]
    child_impaired_since = el.find("ImpairedSince")
    if child_impaired_since is not None:
        import aws_sdk_ec2.types.date_time

        out["impaired_since"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_impaired_since
        )
    child_name = el.find("Name")
    if child_name is not None:
        import aws_sdk_ec2.types.status_name

        out["name"] = aws_sdk_ec2.types.status_name.deserialize_ec2_query(child_name)
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.status_type

        out["status"] = aws_sdk_ec2.types.status_type.deserialize_ec2_query(
            child_status
        )
    return out
