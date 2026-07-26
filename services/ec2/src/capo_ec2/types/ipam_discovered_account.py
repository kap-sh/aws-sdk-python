"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_discovery_failure_reason
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamDiscoveredAccount(TypedDict, closed=True):
    account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The account ID.</p>"""
    discovery_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region that the account information is returned from. An account can be discovered in multiple regions and will have a separate discovered account for each Region.</p>"""
    failure_reason: NotRequired[
        "capo_ec2.types.ipam_discovery_failure_reason.IpamDiscoveryFailureReason"
    ]
    """<p>The resource discovery failure reason.</p>"""
    last_attempted_discovery_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last attempted resource discovery time.</p>"""
    last_successful_discovery_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last successful resource discovery time.</p>"""
    organizational_unit_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of an Organizational Unit in Amazon Web Services Organizations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredAccount, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_id" in value:
        pairs.append((f"{prefix}.AccountId", str(value["account_id"])))
    if "discovery_region" in value:
        pairs.append((f"{prefix}.DiscoveryRegion", str(value["discovery_region"])))
    if "failure_reason" in value:
        import capo_ec2.types.ipam_discovery_failure_reason

        capo_ec2.types.ipam_discovery_failure_reason.serialize_ec2_query(
            value["failure_reason"], pairs, f"{prefix}.FailureReason"
        )
    if "last_attempted_discovery_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_attempted_discovery_time"],
            pairs,
            f"{prefix}.LastAttemptedDiscoveryTime",
        )
    if "last_successful_discovery_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_successful_discovery_time"],
            pairs,
            f"{prefix}.LastSuccessfulDiscoveryTime",
        )
    if "organizational_unit_id" in value:
        pairs.append(
            (f"{prefix}.OrganizationalUnitId", str(value["organizational_unit_id"]))
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredAccount:
    out: IpamDiscoveredAccount = {}  # type: ignore[typeddict-item]
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_discovery_region = el.find("DiscoveryRegion")
    if child_discovery_region is not None:
        out["discovery_region"] = str(child_discovery_region.text or "")
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        import capo_ec2.types.ipam_discovery_failure_reason

        out["failure_reason"] = (
            capo_ec2.types.ipam_discovery_failure_reason.deserialize_ec2_query(
                child_failure_reason
            )
        )
    child_last_attempted_discovery_time = el.find("LastAttemptedDiscoveryTime")
    if child_last_attempted_discovery_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_attempted_discovery_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_attempted_discovery_time
            )
        )
    child_last_successful_discovery_time = el.find("LastSuccessfulDiscoveryTime")
    if child_last_successful_discovery_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_successful_discovery_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_successful_discovery_time
            )
        )
    child_organizational_unit_id = el.find("OrganizationalUnitId")
    if child_organizational_unit_id is not None:
        out["organizational_unit_id"] = str(child_organizational_unit_id.text or "")
    return out
