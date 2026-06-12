"""Generated from Smithy shape ``com.amazonaws.outposts#ListOutpostsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.availability_zone_id_list
    import aws_sdk_outposts.types.availability_zone_list
    import aws_sdk_outposts.types.life_cycle_status_list
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.token


class ListOutpostsInput(TypedDict):
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    life_cycle_status_filter: NotRequired[
        "aws_sdk_outposts.types.life_cycle_status_list.LifeCycleStatusList"
    ]
    """<p>Filters the results by the lifecycle status.</p>"""
    availability_zone_filter: NotRequired[
        "aws_sdk_outposts.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>Filters the results by Availability Zone (for example, <code>us-east-1a</code>).</p>"""
    availability_zone_id_filter: NotRequired[
        "aws_sdk_outposts.types.availability_zone_id_list.AvailabilityZoneIdList"
    ]
    """<p>Filters the results by AZ ID (for example, <code>use1-az1</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutpostsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOutpostsInput:
    out: ListOutpostsInput = {}  # type: ignore[typeddict-item]
    return out
