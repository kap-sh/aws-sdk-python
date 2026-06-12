"""Generated from Smithy shape ``com.amazonaws.batch#FairsharePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.share_attributes_list


class FairsharePolicy(TypedDict):
    share_decay_seconds: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The amount of time (in seconds) to use to calculate a fair-share percentage for each share identifier in use. A value of zero (0) indicates the default minimum time window (600 seconds). The maximum supported value is 604800 (1 week).</p> <p>The decay allows for more recently run jobs to have more weight than jobs that ran earlier. Consider adjusting this number if you have jobs that (on average) run longer than ten minutes, or a large difference in job count or job run times between share identifiers, and the allocation of resources doesn't meet your needs.</p>"""
    compute_reservation: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>A value used to reserve some of the available maximum vCPU for share identifiers that aren't already used.</p> <p>The reserved ratio is <code>(<i>computeReservation</i>/100)^<i>ActiveFairShares</i> </code> where <code> <i>ActiveFairShares</i> </code> is the number of active share identifiers.</p> <p>For example, a <code>computeReservation</code> value of 50 indicates that Batch reserves 50% of the maximum available vCPU if there's only one share identifier. It reserves 25% if there are two share identifiers. It reserves 12.5% if there are three share identifiers. A <code>computeReservation</code> value of 25 indicates that Batch should reserve 25% of the maximum available vCPU if there's only one share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three share identifiers.</p> <p>The minimum value is 0 and the maximum value is 99.</p>"""
    share_distribution: NotRequired[
        "aws_sdk_batch.types.share_attributes_list.ShareAttributesList"
    ]
    """<p>An array of <code>SharedIdentifier</code> objects that contain the weights for the share identifiers for the fair-share policy. Share identifiers that aren't included have a default weight of <code>1.0</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FairsharePolicy) -> dict:
    out: dict = {}
    if "share_decay_seconds" in value:
        out["shareDecaySeconds"] = value["share_decay_seconds"]
    if "compute_reservation" in value:
        out["computeReservation"] = value["compute_reservation"]
    if "share_distribution" in value:
        import aws_sdk_batch.types.share_attributes_list

        out["shareDistribution"] = (
            aws_sdk_batch.types.share_attributes_list.serialize_json(
                value["share_distribution"]
            )
        )
    return out


def deserialize_json(data: dict) -> FairsharePolicy:
    out: FairsharePolicy = {}  # type: ignore[typeddict-item]
    if "shareDecaySeconds" in data:
        out["share_decay_seconds"] = data["shareDecaySeconds"]
    if "computeReservation" in data:
        out["compute_reservation"] = data["computeReservation"]
    if "shareDistribution" in data:
        import aws_sdk_batch.types.share_attributes_list

        out["share_distribution"] = (
            aws_sdk_batch.types.share_attributes_list.deserialize_json(
                data["shareDistribution"]
            )
        )
    return out
