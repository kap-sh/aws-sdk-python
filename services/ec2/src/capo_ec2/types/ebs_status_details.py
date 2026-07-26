"""Generated from Smithy shape ``com.amazonaws.ec2#EbsStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.status_name
    import capo_ec2.types.status_type


class EbsStatusDetails(TypedDict, closed=True):
    impaired_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the attached EBS status check failed.</p>"""
    name: NotRequired["capo_ec2.types.status_name.StatusName"]
    """<p>The name of the attached EBS status check.</p>"""
    status: NotRequired["capo_ec2.types.status_type.StatusType"]
    """<p>The result of the attached EBS status check.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "impaired_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["impaired_since"], pairs, f"{prefix}.ImpairedSince"
        )
    if "name" in value:
        import capo_ec2.types.status_name

        capo_ec2.types.status_name.serialize_ec2_query(
            value["name"], pairs, f"{prefix}.Name"
        )
    if "status" in value:
        import capo_ec2.types.status_type

        capo_ec2.types.status_type.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> EbsStatusDetails:
    out: EbsStatusDetails = {}  # type: ignore[typeddict-item]
    child_impaired_since = el.find("ImpairedSince")
    if child_impaired_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["impaired_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_impaired_since
            )
        )
    child_name = el.find("Name")
    if child_name is not None:
        import capo_ec2.types.status_name

        out["name"] = capo_ec2.types.status_name.deserialize_ec2_query(child_name)
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.status_type

        out["status"] = capo_ec2.types.status_type.deserialize_ec2_query(child_status)
    return out
